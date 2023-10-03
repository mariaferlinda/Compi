
def leer(archivo:str) ->list :
    x = open(archivo,"r")
    lista = x.readlines()
    rresultado = list()
    simbolos = [";",".","{","}","(",")","[","]","+","++",'"',"=","<","-"," "]
    for j in lista:
        keeplinea = ""
        for m in j:
            if m == " ":
                rresultado.append(keeplinea)
                keeplinea = ""
            elif m in simbolos:
                rresultado.append(keeplinea)
                rresultado.append(m)
                keeplinea = ""
            else:
                keeplinea += m
    return rresultado

def corchete (rresultado:list) -> list :
    final = list()
    dicc = dict()
    numerito = 1
    for j in rresultado:
        if j not in dicc:
            dicc[j] = f'[{numerito}, {j}]'
            numerito += 1
            final.append(dicc[j])
        else:
            final.append(dicc[j])
    return final


if __name__ == "__main__":
    tt = leer("codigo.txt")
    tt2 = corchete(tt)
    for i in tt2:
        print (i)