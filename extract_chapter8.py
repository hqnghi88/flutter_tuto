import pypdf

reader = pypdf.PdfReader("/Users/hqnghi/git/flutter_tuto/Flutter Apprentice New Version.pdf")
start_page = 314 # Page 315 (0-indexed is 314)
end_page = 351   # Page 351 (0-indexed is 350, end_page is exclusive so 351)

with open("/Users/hqnghi/git/flutter_tuto/chapter8_text.txt", "w") as f:
    for page_num in range(start_page, end_page):
        f.write(f"--- PAGE {page_num + 1} ---\n")
        f.write(reader.pages[page_num].extract_text())
        f.write("\n\n")
print("Extracted Chapter 8 to chapter8_text.txt")
