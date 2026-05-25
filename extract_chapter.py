import pypdf

reader = pypdf.PdfReader("/Users/hqnghi/git/flutter_tuto/Flutter Apprentice New Version.pdf")
start_page = 80 # Page 81 (0-indexed is 80)
end_page = 124   # Page 125 (0-indexed is 124)

with open("/Users/hqnghi/git/flutter_tuto/chapter3_text.txt", "w") as f:
    for page_num in range(start_page, end_page + 1):
        f.write(f"--- PAGE {page_num + 1} ---\n")
        f.write(reader.pages[page_num].extract_text())
        f.write("\n\n")
print("Extracted Chapter 3 to chapter3_text.txt")
