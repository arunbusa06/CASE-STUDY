import zipfile
import xml.etree.ElementTree as ET

z = zipfile.ZipFile('CSR.docx')
doc_xml = z.read('word/document.xml')
root = ET.fromstring(doc_xml)

NS = {
    'w': 'http://purl.oclc.org/ooxml/wordprocessingml/main',
    'a': 'http://purl.oclc.org/ooxml/drawingml/main',
    'r': 'http://purl.oclc.org/ooxml/officeDocument/relationships',
}

# Find all drawings and see their surrounding text
for p in root.iter('{http://purl.oclc.org/ooxml/wordprocessingml/main}p'):
    texts = [t.text for t in p.iter('{http://purl.oclc.org/ooxml/wordprocessingml/main}t') if t.text]
    txt = ''.join(texts).strip()
    
    # check blip
    blips = p.findall('.//{http://purl.oclc.org/ooxml/drawingml/main}blip')
    if blips:
        for b in blips:
            embed = b.attrib.get('{http://purl.oclc.org/ooxml/officeDocument/relationships}embed')
            print(f"IMAGE EMBED: {embed}, surrounding text: {txt[:60]}")
    elif txt.startswith('Fig') or txt.startswith('TABLE') or txt.startswith('Table'):
        print(f"CAPTION: {txt[:100]}")

print("\n=== DUMPING STRUCTURE AND SECTIONS ===")
# Let's inspect sections and body children
body = root.find('{http://purl.oclc.org/ooxml/wordprocessingml/main}body')
print(f"Body children count: {len(body)}")
counts = {}
for child in body:
    tag = child.tag.split('}')[-1]
    counts[tag] = counts.get(tag, 0) + 1
print("Body child tags:", counts)
