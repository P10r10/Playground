import fitz


def merge_files(a: str, b: str):
    try:
        doc_a = fitz.open(a)  # open the 1st document
    except:
        print(f"Error opening file {a}")
    try:
        doc_b = fitz.open(b)  # open the 2nd document
        doc_a.insert_pdf(doc_b)  # merge the docs
        doc_a.save("merged.pdf")  # save the merged document
    except:
        print(f"Error opening file {b}")
    print("Files merged.")


def main():
    doc_a = input("1st file? ")
    doc_b = input("2nd file? ")
    merge_files(doc_a, doc_b)


main()
