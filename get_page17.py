import pypdf

reader = pypdf.PdfReader("/Users/hqnghi/git/flutter_tuto/Flutter Apprentice New Version.pdf")
print(reader.pages[16].extract_text())
