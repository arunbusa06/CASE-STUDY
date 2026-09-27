import zipfile
import xml.etree.ElementTree as ET

z = zipfile.ZipFile('CSR.docx')
doc_xml = z.read('word/document.xml')
root = ET.fromstring(doc_xml)

W = '{http://purl.oclc.org/ooxml/wordprocessingml/main}'
body = root.find(W + 'body')

with open('extracted_csr_content.txt', 'w', encoding='utf-8') as out:
    for child in body:
        tag = child.tag[len(W):]
        if tag == 'p':
            texts = [t.text for t in child.iter(W + 't') if t.text]
            txt = ''.join(texts).strip()
            pStyle = child.find(f'.//{W}pStyle')
            s_val = pStyle.attrib.get(f'{W}val', '') if pStyle is not None else ''
            
            # check section break
            sect = child.find(f'.//{W}sectPr')
            sect_str = ' [SECTION BREAK]' if sect is not None else ''
            
            # check drawings
            blip = child.find(f'.//{{http://purl.oclc.org/ooxml/drawingml/main}}blip')
            blip_str = f' [IMAGE: {blip.attrib.get("{http://purl.oclc.org/ooxml/officeDocument/relationships}embed")}]' if blip is not None else ''
            
            if txt or sect_str or blip_str:
                out.write(f'P ({s_val}): {txt}{sect_str}{blip_str}\n')
        elif tag == 'tbl':
            out.write('--- TABLE START ---\n')
            for row in child.findall(W + 'tr'):
                row_cells = []
                for cell in row.findall(W + 'tc'):
                    cell_texts = [t.text for t in cell.iter(W + 't') if t.text]
                    row_cells.append(' '.join(''.join(cell_texts).split()))
                out.write(' | '.join(row_cells) + '\n')
            out.write('--- TABLE END ---\n')

print("Content extracted successfully!")
