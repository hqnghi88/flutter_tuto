import pypdf

reader = pypdf.PdfReader("/Users/hqnghi/git/flutter_tuto/Flutter Apprentice New Version.pdf")
start_page = 261 # Page 262 (0-indexed is 261)
end_page = 314   # Page 314 (0-indexed is 313, end_page is exclusive so 314)

with open("/Users/hqnghi/git/flutter_tuto/chapter7_text.txt", "w") as f:
    for page_num in range(start_page, end_page):
        f.write(f"--- PAGE {page_num + 1} ---\n")
        f.write(reader.pages[page_num].extract_text())
        f.write("\n\n")
print("Extracted Chapter 7 to chapter7_text.txt")
