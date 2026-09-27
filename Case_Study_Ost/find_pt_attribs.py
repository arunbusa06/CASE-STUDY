import zipfile
import re

z = zipfile.ZipFile('CSR_standard.docx')
doc_xml = z.read('word/document.xml').decode('utf-8')

# Find patterns like w:w="...pt" or similar
matches = set(re.findall(r'w:\w+=[\x22\x27][^\x22\x27]*pt[\x22\x27]', doc_xml))
print(f"Total pt attributes found in document.xml: {len(matches)}")
for m in sorted(list(matches))[:30]:
    print(m)
