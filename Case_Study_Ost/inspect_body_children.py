import docx

doc = docx.Document('CSR_standard.docx')
body = doc._element.body

print(f"Total elements in body: {len(body)}")
for idx, el in enumerate(body):
    tag = el.tag.split('}')[-1]
    if tag == 'tbl':
        tbl = docx.table.Table(el, doc)
        first_txt = tbl.cell(0, 0).text.strip().replace('\n', ' ')[:40]
        print(f"[{idx}] TBL: {first_txt}")
    elif tag == 'p':
        p = docx.text.paragraph.Paragraph(el, doc)
        txt = p.text.strip()
        sectPr = el.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}sectPr')
        has_sect = " [HAS SECTPR]" if sectPr is not None else ""
        if txt:
            if any(txt.startswith(x) for x in ['TITLE', 'Software Development Company', 'RUBRICS', 'Notes', 'Ms. Priyanka', 'Course Name', 'Abstract', 'Keywords', 'I. Introduction', 'REFERENCES', 'Appendix']):
                print(f"[{idx}] P ({p.style.name}): '{txt[:70]}'{has_sect}")
        elif has_sect:
            print(f"[{idx}] P (empty){has_sect}")
