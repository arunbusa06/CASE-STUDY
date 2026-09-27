import docx

doc = docx.Document('CSR_standard.docx')
body = doc._element.body

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

for idx, el in enumerate(body):
    sects = el.findall(f'.//{W}sectPr')
    if sects:
        for s in sects:
            cols = s.xpath('./w:cols/@w:num')
            print(f"Body index {idx} ({el.tag.split('}')[-1]}) has sectPr in pPr: cols={cols}")
    if el.tag.endswith('sectPr'):
        cols = el.xpath('./w:cols/@w:num')
        print(f"Body index {idx} is sectPr: cols={cols}")
