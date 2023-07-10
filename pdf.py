import fitz


def merge_files(a: str, b: str) -> None:
    try:
        doc_a = fitz.open(a)  # open the 1st document
    except:
        print(f"Error opening file {a}")
    try:
        doc_b = fitz.open(b)  # open the 2nd document
        doc_a.insert_pdf(doc_b)  # merge the docs
        doc_a.save("merged.pdf")  # save the merged document
        print("Files merged.")
    except:
        print(f"Error opening file {b}")


def delete_pages(file_name: str, page_nb: int) -> None:
    try:
        doc = fitz.open(file_name)  # open the document
    except:
        print(f"Error opening file {file_name}")
    try:
        doc.delete_page(page_nb - 1)
        doc.save("deleted.pdf")  # save the deleted page document
        print("Page deleted.")
    except:
        print(f"Error deleting page {page_nb}")


def main():
    doc_a = input("1st file? ")
    doc_b = input("2nd file? ")
    merge_files(doc_a, doc_b)

    # doc = input("File name? ")
    # page_nb = int(input("Page number? "))
    # delete_pages(doc, page_nb)


main()
