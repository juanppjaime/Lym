import pyparsing as pp
from pyparsing import *
import sys


exit = 0
'''
num = '0' or  '1' or '2'
ssn = num + '-' + num + '-' + num
'''
numeros = oneOf(["1","2","3","4","5","6","7","8","9","0"])
dash = '-'
'numeros y existe'
dir = oneOf(['left','right','front','back'])
ori = oneOf(['south','north','west','east'])
nombre = Word(alphas) 

valor = Word(alphanums)
param =  ('(' + ((valor) + ZeroOrMore(Literal(",") + (valor))) + ')') | "()"
LVacia = oneOf(["nop("])
LSimpleValor = oneOf(["walk(","leap(","drop(","get(","grab(","letGo("])
LSimpleDir = oneOf(["turn("])
LSimpleOri = oneOf(["turnto("])
LDobleValorValor =  oneOf(["jump("])
LDobleValorDir =  oneOf(["walk(","leap("])
LDobleValorOri =  oneOf(["leap(","walk("])
comando = (LVacia + ")" | (LSimpleValor + numeros + ")") | (LSimpleDir + dir + ")") | (LSimpleOri + ori + ")") | (LDobleValorValor + numeros + ',' + numeros + ")") | (LDobleValorDir) + numeros + "," + dir + ")" | (LDobleValorOri + numeros + ',' + ori + ")") ) 
comando2 = (LVacia  | (LSimpleValor + valor) | (LSimpleDir + valor) | (LSimpleOri + valor) | (LDobleValorValor + valor + ',' + valor) | (LDobleValorDir + valor + ',' + valor) | (LDobleValorOri + valor + ',' + valor )) + ')'  
LCompleta = [] 

#Condiciones
facing = 'facing(' + ori + ')' 
can = 'can(' + comando + ')' 
nott = 'not:' + facing | can

condicion = facing | can | nott

# Bloque con numeros , dir u ori
bloque = '{' + ((comando) + ZeroOrMore(Literal(";") + (comando))) + '}'

#Bloque con parametros

bloque2 = '{' + ((comando2) + ZeroOrMore(Literal(";") + (comando2))) + '}'

#Bloque llamado

#IF
iff = 'if' + condicion + bloque + 'else' + comando|bloque

#While
whilee = 'while' + condicion + bloque

#Repeat
repeat = 'repeat' + numeros + 'times' + bloque

#Bloque condicional
bloque_condicional = '{' + (iff | whilee | repeat) + '}'

#Bloque general

bloque_general = "{" + ((iff | whilee | repeat|comando2) + (ZeroOrMore(Literal(";") + (comando2 |iff | whilee | repeat)))) + "}"

#Defvar
defVar = 'defVar' + nombre + numeros

#DefProc
defProc = 'defProc' + nombre + param + ZeroOrMore(bloque_general) 

#Llamado

pattern2 = ZeroOrMore(defVar) + ZeroOrMore(defProc)  

def read():
    f = open("prueba.txt", "r")
    input_text = f.read()
    f.close()
    return input_text

#input_text = "."
input_text = read()
#//Verificar que el input cumpla con las reglas de la gramatica

## Lista Param Procesos

def calcularParam(j,pos,dict):
    contador = 1
    pos2 = pos+1
    while j[pos2] != "{":
        if j[pos2] == "()":
            contador = 0
            break
        if (j[pos2] == ","):
            contador += 1
        pos2 += 1
    dict[j[pos+1]]=contador  
    
try:
    j = pattern2.parseString(input_text)
    pos = 0
    LCompletaParam = {}
    while pos<len(j):
        if j[pos] == "defProc":
            LCompleta.append(j[pos+1])
            calcularParam(j,pos,LCompletaParam)         
        pos+=1
    
    pos=0
    
    
     #Bloque función

    bloque_funcion =  (oneOf(LCompleta)) + ("()"| ("(" + (numeros|dir|ori) + ZeroOrMore(Literal(",") + (numeros|dir|ori)) + ")"))
    bloque_llamado = ((comando|bloque_funcion) + ZeroOrMore(Literal(";") + (comando|bloque_funcion)))
    #A = oneOf(["putCB","goNorth","goWest"])
    llamado =  "{" + bloque_llamado + "}" 
    pattern = ZeroOrMore(defVar) + ZeroOrMore(defProc) + ZeroOrMore(llamado) 
    
    j = pattern.parseString(input_text)
    
    validacion = []
    while pos <len(j):
        aux = LCompleta
        if j[pos] in aux and j[pos-1] != "defProc":

            contador = 1
            pos2 = pos+1
            while j[pos2] != ';' and j[pos2] != '}':
                if j[pos2] == "()":
                    contador = 0
                    break
                if (j[pos2] == ","):
                    contador += 1
                pos2 += 1
            validacion.append(j[pos])
            validacion.append(contador)          
        pos+=1
            
    pos = 0
    while pos < len(validacion):
        if validacion[pos] in LCompletaParam and validacion[pos+1] != LCompletaParam[validacion[pos]]:
            print("No")
            exit = 1
        pos += 1
except pp.ParseException as e:
    print("No")

if exit == 1:
    sys.exit(1)
try: 

    e = pattern.parseString(input_text)
    sumatoria = 0
    #print(LCompleta)
    

    for i in e:
        sumatoria += len(i)
    longitud = (input_text.replace(" ", ""))
    longitud2= (longitud.replace("\n", ""))
    if sumatoria == (len(longitud2)):
        print("Yes")
    else:
        print("No")
        #print(e)
        #print(sumatoria)
except pp.ParseException as e:
    print("No")



  

            