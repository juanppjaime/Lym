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

valor = numeros | dir | ori
param =  '(' + ((valor) + ZeroOrMore(Literal(",") + (valor))) | Empty() + ')'
LVacia = oneOf(["nop("])
LSimpleValor = oneOf(["walk(","leap(","drop(","get(","grab(","letGo("])
LSimpleDir = oneOf(["turn("])
LSimpleOri = oneOf(["turnto("])
LDobleValorValor =  oneOf(["jump("])
LDobleValorDir =  oneOf(["walk(","leap("])
LDobleValorOri =  oneOf(["leap("])
comando = (LVacia | (LSimpleValor + numeros) | (LSimpleDir + dir) | (LSimpleOri + ori) | (LDobleValorValor + numeros + ',' + numeros) | (LDobleValorDir + numeros + ',' + dir) | (LDobleValorOri + numeros + ',' + ori )) + ')'  

#Condiciones
facing = 'facing(' + ori + ')' 
can = 'can(' + comando + ')'
nott = 'not:' + facing | can

condicion = facing | can | nott

# Bloque
bloque = '{' + ((comando) + ZeroOrMore(Literal(";") + (comando))) | Empty() + '}'

#IF
iff = 'if' + condicion + bloque + 'else' + bloque

#While
whilee = 'while' + condicion + bloque

#Repeat
repeat = 'repeat' + numeros + 'times' + bloque

#Defvar
defVar = 'defVar' + nombre + numeros

#DefProc
DefProc = 'defProc' + nombre + param + bloque

#Llamado
llamado = bloque

pattern = ZeroOrMore(defVar) + ZeroOrMore(DefProc)
input_text = """
defVar nom 1
defVar y 0
defVar one 0
defProc putCB (5 , north )
{
drop(5);
letGo (3);
walk(5)
}
defProc goNorth()
{
while can(walk(1 , north ) ) { walk(1 , north ) }
}
defProc goWest ()
{
    if can(walk(1 , west ) ) { walk(1 , west ) } e l s e nop ()
}
{
jump (3 ,3) ;
putCB (2 ,1)
}
"""

# Analizar una cadena
result = pattern.parseString(input_text)
if result:
    print("La palabra 'sigue' sigue a 'esto'")
else:
    print("La palabra 'sigue' no sigue a 'esto'")

for match, start, stop in pattern.scanString(input_text):
  print(match,start,match)



  

            