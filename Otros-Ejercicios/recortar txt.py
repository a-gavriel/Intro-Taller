import fileinput


#borra todo el archivo para escribir de 0
def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()
    


def recortartxt():
    arch_contc = open ("arch.txt","r+")
    filecontent = ""
    filecontent1 = "0101010101" + "0101010101" + "0101010101" 
    filecontent2 = filecontent1 + filecontent1 + filecontent1
    filecontent3 = filecontent2 + filecontent2  
    linea = arch_contc.readline()  #lee primera linea
    
    while linea !="":
        #filecontent+=linea[:-2]+"\n" #borra parte del string
        a = linea[2:]
        filecontent += a 
        linea = arch_contc.readline()  #lee siguiente linea
        
    deleteContent(arch_contc)
    
    arch_contc.write(filecontent)
    arch_contc.close()

    
    
recortartxt()
