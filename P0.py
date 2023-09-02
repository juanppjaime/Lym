import pyparsing as pp
from pyparsing import *

'''
num = '0' or  '1' or '2'
ssn = num + '-' + num + '-' + num
'''
numeros = oneOf(["1","2","3","4","5","6","7","8","9","0"])
dash = '-'
'numeros y existe'
dir = oneOf(['left','right','front','back'])
ori = oneOf(['south','north','west','east'])
nombre = Word(alphanums) 

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

#Condiciones
facing = 'facing(' + ori + ')' 
can = 'can(' + comando + ')' 
nott = 'not:' + facing | can

condicion = facing | can | nott

# Bloque con numeros , dir u ori
bloque = '{' + ((comando) + ZeroOrMore(Literal(";") + (comando))) + '}'

#Bloque con parametros

bloque2 = '{' + ((comando2) + ZeroOrMore(Literal(";") + (comando2))) + '}'

#IF
iff = 'if' + condicion + bloque + 'else' + bloque

#While
whilee = 'while' + condicion + bloque

#Repeat
repeat = 'repeat' + numeros + 'times' + bloque

#Bloque condicional
bloque_condicional = '{' + iff | whilee | repeat + '}'

#Defvar
defVar = 'defVar' + nombre + numeros

#DefProc
defProc = 'defProc' + nombre + param + ZeroOrMore(iff|bloque2) 

#Llamado
llamado = bloque

pattern = ZeroOrMore(defVar) + ZeroOrMore(defProc) 
input_text = """
defVar nom 1
defVar y 0
defVar one 0
defProc putCB (a,n)
{
drop(5);
letGo(3);
walk(5)
}
defProc goNorth()
ifcan(walk(1,west)){walk(1,west)}elsenop()
defProc goWest (6,south)
{
drop(5);
letGo(3);
walk(9)
}
defProc goWest (6,south)
{
jump (3,3);
putCB (2,1)
}
"""
#input_text = input_text.replace(" ","")
# Analizar una cadena
result = pattern.parseString(input_text)
if result:
    print("La palabra 'sigue' sigue a 'esto'")
else:
    print("La palabra 'sigue' no sigue a 'esto'")

for match, start, stop in pattern.scanString(input_text):
  print(match,start,match)



  

            