#The slate3k library have to be downloaded grom the terminal 
import slate3k as slate #This library its the one that let me manipulte the pdfs
import pathlib #This library let me go to each one of the documents in an specific folder

#this is the key/id list so I can find the data that i needed in the text
idList=["SUBDISTRITO","CLAVE CATASTRAL","ZONIFICACIÓN","UBICACIÓN","SUPERFICIE EN CARTOGRAFÍA","SUPERFICIE LEGAL","SUPERFICIE EDIFICADA","SUPERFICIE DE DESPLANTE","COS","CUS","SUPERFICIE MÁXIMA PERMITIDA POR COS","SUPERFICIE MÁXIMA PERMITIDA POR CUS"]

generalList=[]#The data of each pdf will be saved in this list 

#This function its just to correct a problem with a character in the string 
def synCor(Obj):
    for i in range(len(Obj)):
        if "m²" in Obj[i]: #<----That character
            m=Obj[i].split(" ")
            Obj[i]=m[0]
    return Obj 

#This function will compare the string of the argument with the ones in idList
def isInidList(id):
    if id in idList:
        return True
    else:
        return False

#This is one function will let you manipulate the text inside a pdf 
def get_info(path):
    with open(path,'rb') as f:
        pageText = slate.PDF(f)
    texto=str(pageText)
#Here you will maniulate the text as a list that have arrays 
    listaDataG=texto.split("\\n")
    rowList=[]
    
    cont=0
    cantID=len(idList)
    idCont=0
    
#Here is where the data extraction is

    while cont<=len(listaDataG):
        if cont == 0:
            cont=cont+2
            rowList.append(listaDataG[cont])
        elif isInidList(listaDataG[cont]):
            rowList.append(listaDataG[cont+2])
            cont=cont+1
            idCont=idCont+1       
        elif idCont>=cantID:
            break
        else:
            cont=cont+1
#Before saving the data, we correct the syntaxis
    rowList=synCor(rowList)
    row=",".join(rowList)
#This "row" is all the information that I need to extract from the pdf, and its always in the same order
    return row+"\n"
       
#This function let me do the loop in the folder, so i can analyse all the documents with the termination ".pdf"
def loopFromDir(path):
    listFiles =list( pathlib.Path(path).glob('*.pdf'))
    for fileName in listFiles:
       
       mapKeys =get_info(fileName)
       #Here is where all the information will be saved
       generalList.append(mapKeys)
 
    return generalList

#And finally this function will put all the information in a .txt document 
def writeData(path):
    if __name__ == '__main__':
        Data= loopFromDir(path)
    
    f = open("DataSantaTere.txt","w")

    f.writelines(Data)
    f.close()


#The parameter that you have to give here is the direction of the FOLDER that contains all the pdfs that you need
path = '/home/carlosfl/Desktop/Programacion/Proyecto de Probabilidad/PDFs Santa Tere/' 
writeData(path)#Finally we call all the functions just with this one :D