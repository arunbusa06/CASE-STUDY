import zipfile
import xml.etree.ElementTree as ET

z = zipfile.ZipFile('CSR.docx')
doc_xml = z.read('word/document.xml')
root = ET.fromstring(doc_xml)
W = '{http://purl.oclc.org/ooxml/wordprocessingml/main}'

body = root.find(W + 'body')
current_sec = 0

for child in body:
    tag = child.tag[len(W):]
    if tag == 'p':
        texts = [t.text for t in child.iter(W + 't') if t.text]
        txt = ''.join(texts).strip()
        sectPr = child.find(f'.//{W}sectPr')
        if txt:
            if any(txt.startswith(x) for x in ['TITLE', 'RUBRICS', 'Software Development', 'Course Name', 'Abstract', 'Keywords', 'I. Introduction', 'II.', 'III.', 'IV.', 'V.', 'VI.', 'VII.', 'VIII.', 'IX.', 'X.', 'XI.', 'XII.', 'REFERENCES', 'Appendix']):
                print(f"Sec {current_sec} | P: {txt[:80]}")
        if sectPr is not None:
            print(f"=== END OF SECTION {current_sec} ===")
            current_sec += 1
    elif tag == 'tbl':
        # print first row of table
        row1 = child.find(W + 'tr')
        if row1 is not None:
            c_txt = [''.join(t.text for t in cell.iter(W + 't') if t.text) for cell in row1.findall(W + 'tc')]
            print(f"Sec {current_sec} | TBL: {' | '.join(c_txt)[:80]}")
print(f"=== FINAL SECTION {current_sec} END ===")
