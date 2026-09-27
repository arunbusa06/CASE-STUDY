import zipfile
import xml.etree.ElementTree as ET

z = zipfile.ZipFile('CSR.docx')
doc_xml = z.read('word/document.xml')
root = ET.fromstring(doc_xml)
W = '{http://purl.oclc.org/ooxml/wordprocessingml/main}'

sects = root.findall(f'.//{W}sectPr')
print(f"Total sectPr elements: {len(sects)}")

for i, s in enumerate(sects):
    pgSz = s.find(W + 'pgSz')
    pgMar = s.find(W + 'pgMar')
    cols = s.find(W + 'cols')
    headerRefs = [h.attrib for h in s.findall(W + 'headerReference')]
    footerRefs = [f.attrib for f in s.findall(W + 'footerReference')]
    
    w = pgSz.attrib.get(W + 'w', '') if pgSz is not None else ''
    h = pgSz.attrib.get(W + 'h', '') if pgSz is not None else ''
    num_cols = cols.attrib.get(W + 'num', '1') if cols is not None else '1'
    
    print(f"--- Section {i} ---")
    print(f"  Page Size: w={w}, h={h}")
    if pgMar is not None:
        top = pgMar.attrib.get(W + 'top', '')
        bottom = pgMar.attrib.get(W + 'bottom', '')
        left = pgMar.attrib.get(W + 'left', '')
        right = pgMar.attrib.get(W + 'right', '')
        print(f"  Margins: top={top}, bottom={bottom}, left={left}, right={right}")
    print(f"  Columns: {num_cols}")
    print(f"  Headers: {headerRefs}")
    print(f"  Footers: {footerRefs}")
