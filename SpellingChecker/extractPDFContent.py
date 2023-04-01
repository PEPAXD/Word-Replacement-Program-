import PyPDF2

#OPEN PDF, READ AND APP TO ARRAY
def extracText(pdf_file: str) -> [str]:
    with open(pdf_file + ".pdf", 'rb') as pdf:

        reader = PyPDF2.PdfReader(pdf, strict=False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)

        return pdf_text

#ARRAY ---> VAR_TEXT[STR]
def print_PDF_Text(extracted_text):
    my_texto = ''

    for text in extracted_text:
        print("\n"+text)
        my_texto += text + "\n\n"

    return my_texto
