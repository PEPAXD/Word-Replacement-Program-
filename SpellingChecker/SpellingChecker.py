import DeveloperCredits
import extractPDFContent
import os

#REPLACE TARGET WORD
def replace_word(extractTexto):

    texto = extractPDFContent.print_PDF_Text(extractTexto)
    wordToReplace = input("\nESCRIBA LA PALABRA QUE QUIERE REEMPLAZAR EN EL TEXTO ANTERIOR ---> ")
    wordReplacement = input("ESCRIBA LA PALABRA QUE REEMPLAZARA LA OPCION ANTERIOR ---> ")

    os.system('cls')

    newTexto = "\n"+texto.replace(wordToReplace, wordReplacement)
    print(newTexto)

    return newTexto

def txtFile(pdfFileName, newText):
    print("CREATE ---> "+pdfFileName+".txt\n")

    file = open(pdfFileName + "-copy", "w")
    file.write(newText)
    file.close()

def endScript():
    input("PRESS ENTER TO FINISH SCRIPT...")

if __name__ == '__main__':

    DeveloperCredits.printCredits()
    pdfFileName = 'pdf-test'
    newText = replace_word(extractPDFContent.extracText(pdfFileName))
    txtFile(pdfFileName, newText)
    endScript()
