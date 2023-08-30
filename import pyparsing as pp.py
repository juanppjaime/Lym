import pyparsing as pp
from pyparsing import *

'''
num = '0' or  '1' or '2'
ssn = num + '-' + num + '-' + num
'''

dash = '-'
'nums y existe'
dir = Literal['left','right','front','back']
ori = Literal['south','north','west','east']
nombre = Word(alphanums) 

valor = Word
param =  '(' + ((valor) + ZeroOrMore(Literal(",") + (valor))) | Empty + ')'
LVacia = ["nop("]
LSimpleValor = ["walk(","leap(","drop(","get(","grab(","letGo("]
LSimpleDir = ["turn("]
LSimpleOri = ["turnto("]
LDobleValorValor =  ["jump("]
LDobleValorDir =  ["walk(","leap("]
LDobleValorOri =  ["leap("]
comando = (LVacia | LSimpleValor + nums | LSimpleDir + dir | LSimpleOri + ori | LDobleValorValor + nums + ',' + nums | LDobleValorDir + nums + ',' + dir | LDobleValorOri + nums + ',' + ori ) + ')'  

#Condiciones
facing = 'facing(' + ori + ')' 
can = 'can(' + comando + ')'
nott = 'not:' + facing | can

condicion = facing | can | nott

# Bloque
bloque = '{' + ((comando) + ZeroOrMore(Literal(";") + (comando))) | Empty + '}'

#IF
iff = 'if' + condicion + bloque + 'else' + bloque

#While
whilee = 'while' + condicion + bloque

#Repeat
repeat = 'repeat' + nums + 'times' + bloque

#Defvar
defVar = 'defVar' + nombre + nums

#DefProc
DefProc = 'defProc' + nombre + param + bloque

#Llamado
llamado = bloque

ssn_parser = Combine(
  Word(nums, exact=3)
  + dash
  + Word(nums, exact=2)
  + dash
  + Word(nums, exact=4)
)   

input_string = """
  xxx 225-92-8416 yyy
  103-33-3929 zzz 028-91-0122
"""

for match, start, stop in ssn_parser.scanString(input_string):
  print(match)
  
  

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