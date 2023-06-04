import fitz


def merge_files(a: str, b: str):
    try:
        doc_a = fitz.open(a)  # open the 1st document
    except:
        print(f"Erro na abertura do ficheiro {a}")
    try:
        doc_b = fitz.open(b)  # open the 2nd document
        print("DEB")
        doc_a.insert_pdf(doc_b)  # merge the docs
        doc_a.save("merged.pdf")  # save the merged document
    except:
        print(f"Erro na abertura do ficheiro {b}")


def main():
    doc_a = input("Qual o nome do primeiro ficheiro? ")
    doc_b = input("Qual o nome do segundo ficheiro? ")
    merge_files(doc_a, doc_b)


main()
