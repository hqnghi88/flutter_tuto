import pypdf

reader = pypdf.PdfReader("/Users/hqnghi/git/flutter_tuto/Flutter Apprentice New Version.pdf")
start_page = 191 # Page 192 (0-indexed is 191)
end_page = 261   # Page 262 (0-indexed is 261)

with open("/Users/hqnghi/git/flutter_tuto/chapter6_text.txt", "w") as f:
    for page_num in range(start_page, end_page):
        f.write(f"--- PAGE {page_num + 1} ---\n")
        f.write(reader.pages[page_num].extract_text())
        f.write("\n\n")
print("Extracted Chapter 6 to chapter6_text.txt")
