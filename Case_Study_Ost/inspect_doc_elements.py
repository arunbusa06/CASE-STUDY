import docx

doc = docx.Document('CSR_standard.docx')
print("Total paragraphs in doc:", len(doc.paragraphs))
print("Total tables in doc:", len(doc.tables))
print("Total sections in doc:", len(doc.sections))

for i, s in enumerate(doc.sections):
    print(f"Section {i}: start_type={s.start_type}, cols={s._sectPr.xpath('./w:cols/@w:num')}")
    print(f"  Header pars: {[p.text for p in s.header.paragraphs if p.text]}")
    print(f"  Footer pars: {[p.text for p in s.footer.paragraphs if p.text]}")

# Let's inspect the first 25 paragraphs
print("\n--- First 30 paragraphs ---")
for i, p in enumerate(doc.paragraphs[:30]):
    print(f"P{i} ({p.style.name}): '{p.text}'")

# Let's inspect table 0, 1, 2, 3
print("\n--- Tables info ---")
for i, tbl in enumerate(doc.tables):
    rows = len(tbl.rows)
    cols = len(tbl.columns)
    first_cell = tbl.cell(0, 0).text.strip().replace('\n', ' ')[:40]
    print(f"Table {i}: {rows} rows x {cols} cols, first cell='{first_cell}'")
