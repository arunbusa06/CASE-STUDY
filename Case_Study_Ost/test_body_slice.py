import docx

doc = docx.Document('CSR_clean.docx')
body = doc._element.body

print(f"Initial body length: {len(body)}")
# Find where the 2-column section starts (after index 175)
# In inspect_body_children earlier, index 175 was p with sectPr
print("Element 175 tag:", body[175].tag)
print("Element 176 tag:", body[176].tag)
print("Last element tag:", body[-1].tag)
