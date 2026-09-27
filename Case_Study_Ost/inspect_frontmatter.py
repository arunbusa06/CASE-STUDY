import zipfile
import xml.etree.ElementTree as ET

z = zipfile.ZipFile('CSR.docx')
doc_xml = z.read('word/document.xml')
root = ET.fromstring(doc_xml)
W = '{http://purl.oclc.org/ooxml/wordprocessingml/main}'

body = root.find(W + 'body')
current_sec = 0

print("=== DETAILED SECTION 0 & 1 INSPECTION ===")
for child in body:
    tag = child.tag[len(W):]
    if tag == 'p':
        texts = [t.text for t in child.iter(W + 't') if t.text]
        txt = ''.join(texts).strip()
        pPr = child.find(W + 'pPr')
        pStyle = pPr.find(W + 'pStyle').attrib.get(W + 'val') if pPr is not None and pPr.find(W + 'pStyle') is not None else ''
        jc = pPr.find(W + 'jc').attrib.get(W + 'val') if pPr is not None and pPr.find(W + 'jc') is not None else ''
        sectPr = child.find(f'.//{W}sectPr')
        if current_sec <= 1:
            print(f"Sec {current_sec} P [{pStyle}] [jc={jc}]: {txt}")
        if sectPr is not None:
            current_sec += 1
            if current_sec > 1:
                break
    elif tag == 'tbl':
        if current_sec <= 1:
            print(f"Sec {current_sec} TBL:")
            for r in child.findall(W + 'tr'):
                cells = [' '.join(''.join(t.text for t in cell.iter(W + 't') if t.text).split()) for cell in r.findall(W + 'tc')]
                print("   | " + " | ".join(cells))
