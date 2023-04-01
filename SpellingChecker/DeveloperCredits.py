import inspect #CHECK DATACODE
import SpellingChecker #LOCATE TARGET_CODE "__MODULE__"
import extractPDFContent

#CONTAR FUNCIONES Y RETORNAR NUMERO
def count_functions(module):

    function_list = inspect.getmembers(module, inspect.isfunction)
    number = len(function_list)

    return number

#FUNCION IMPRIMIR CREDITOS AL PROGRAMADOR
def printCodeMaster(defNumber):

    #PROJECT-DATA
    proyectName = "SpellingChecker"
    developer = "MAURO PEPA"
    proyectVersion = "1.1"

    developerCretis = "\n"+proyectName+ " - BY "+developer+" - V"+proyectVersion+"."+defNumber
    print(developerCretis)

    LongNumberStick = "-"*len(developerCretis)
    print(LongNumberStick)

def printCredits():

    #MODULES PROYECTS
    defNumber = count_functions(SpellingChecker) + count_functions(extractPDFContent)

    printCodeMaster(str(defNumber))
