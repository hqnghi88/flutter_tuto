import pypdf

reader = pypdf.PdfReader("/Users/hqnghi/git/flutter_tuto/Flutter Apprentice New Version.pdf")
print("Total pages:", len(reader.pages))

# Print outline if available
try:
    outline = reader.outline
    def print_outline(outline_list, indent=0):
        for item in outline_list:
            if isinstance(item, list):
                print_outline(item, indent + 2)
            else:
                title = item.get('/Title', 'Untitled')
                page_num = reader.get_destination_page_number(item)
                print(" " * indent + f"- {title} (Page {page_num + 1})")
    print_outline(outline)
except Exception as e:
    print("Could not print outline:", e)
