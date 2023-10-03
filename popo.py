
def leer(archivo:str) ->list :
    x = open(archivo,"r")
    lista = x.readlines()
    rresultado = list()
    simbolos = [";",".","{","}","(",")","[","]","+","++","=","<","-"]
    numeros = []
    for j in lista:
        keeplinea = ""
        cintaodr = 1
        for m in j:
            if m == " " and cintaodr < 2:
                rresultado.append(keeplinea)
                keeplinea = ""
            elif m in simbolos :
                rresultado.append(keeplinea)
                rresultado.append(m)
                keeplinea = ""
            elif m == '"':
                if cintaodr < 2:
                    rresultado.append(m)
                    rresultado.append("constante")
                    cintaodr += 1
                else:
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