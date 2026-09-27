import zipfile
import xml.etree.ElementTree as ET

z = zipfile.ZipFile('CSR.docx')
styles_xml = z.read('word/styles.xml')
root_styles = ET.fromstring(styles_xml)

W = '{http://purl.oclc.org/ooxml/wordprocessingml/main}'

print("=== STYLES IN CSR.docx ===")
for s in root_styles.findall(W + 'style'):
    s_id = s.attrib.get(W + 'styleId')
    name_el = s.find(W + 'name')
    name = name_el.attrib.get(W + 'val') if name_el is not None else ''
    rPr = s.find(W + 'rPr')
    font = ''
    size = ''
    color = ''
    bold = False
    if rPr is not None:
        rFonts = rPr.find(W + 'rFonts')
        if rFonts is not None:
            font = rFonts.attrib.get(W + 'ascii', '')
        sz = rPr.find(W + 'sz')
        if sz is not None:
            size = f"{int(sz.attrib.get(W + 'val', 0)) / 2}pt"
        col = rPr.find(W + 'color')
        if col is not None:
            color = col.attrib.get(W + 'val', '')
        b = rPr.find(W + 'b')
        if b is not None:
            bold = True
    print(f"Style: {s_id} ('{name}') -> Font: {font}, Size: {size}, Bold: {bold}, Color: {color}")
