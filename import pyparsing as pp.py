import pyparsing as pp
from pyparsing import *

'''
num = '0' or  '1' or '2'
ssn = num + '-' + num + '-' + num
'''

dash = '-'
'nums y existe'
dir = oneOf(['left','right','front','back'])
ori = oneOf(['south','north','west','east'])
nombre = Word(alphanums) 

valor = nums | dir | ori
param =  '(' + ((valor) + ZeroOrMore(Literal(",") + (valor))) | Empty() + ')'
LVacia = oneOf(["nop("])
LSimpleValor = oneOf(["walk(","leap(","drop(","get(","grab(","letGo("])
LSimpleDir = oneOf(["turn("])
LSimpleOri = oneOf(["turnto("])
LDobleValorValor =  oneOf(["jump("])
LDobleValorDir =  oneOf(["walk(","leap("])
LDobleValorOri =  oneOf(["leap("])
comando = (LVacia | (LSimpleValor + nums) | (LSimpleDir + dir) | (LSimpleOri + ori) | (LDobleValorValor + nums + ',' + nums) | (LDobleValorDir + nums + ',' + dir) | (LDobleValorOri + nums + ',' + ori )) + ')'  

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
repeat = 'repeat' + nums + 'times' + bloque

#Defvar
defVar = 'defVar' + 'nom' + (nums)

#DefProc
DefProc = 'defProc' + nombre + param + bloque

#Llamado
llamado = bloque

ssn_parser = Combine(
 ZeroOrMore(defVar)
 +
 ZeroOrMore(DefProc)
 +
 llamado
)   

input_string = """defVarnom1
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

for match, start, stop in ssn_parser.scanString(input_string):
  print(match,start,match)
  
  

'''
greet = pp.Word(pp.upper) + "," + pp.Word(pp.upper) + "!"
for greeting_str in [
    "HELLO, WORLD!",
    "HI, THERE!",
    "HEY, EVERYONE!",
]:
    greeting = greet.parse_string("Hello world")
    print(greeting)
    
'''