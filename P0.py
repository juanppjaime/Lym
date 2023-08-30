comandos_simples = ["walk(","leap(","turn(","turnto","drop(","get(","grab(","letGo(","nop(",]
valores_iniciales = ["0","1","2","3","4","5","6","7","8","9"]
comandos_dobles = ["walk(","leap(","jump("]
parentesis_cierre = [")"]
parentesis_abrir = ["("]
corchete_abrir = ["{"]
corchete_cerrar = ["}"]
coma=[","]
comandos_normales = ["M","R","C","B","c","P"]
declaraciones_variables = ["defVar"]
declaraciones_procedimientos = ["defProc"]
variables = ["nomb","ramb"]
nombre_procedimiento = ["goNorth","PUTCB"]
direcciones=["north", "south","west","east"]

def mensaje(mensaje):
    
    Lista_mensaje = []
    palabra=""
    contador = 0
    resultado = True
    
    for i in mensaje:
        
        palabra+=i
        
        if palabra in comandos_simples or palabra in comandos_dobles or palabra in parentesis_cierre or palabra in corchete_abrir or palabra in corchete_cerrar or palabra in comandos_normales or palabra in declaraciones_variables or palabra in variables or palabra in declaraciones_procedimientos or palabra in valores_iniciales or palabra in parentesis_abrir or palabra in nombre_procedimiento:
            
            Lista_mensaje.append(palabra)
            
            palabra = ""
            
    while contador<=(len(Lista_mensaje)-2):
        
        if Lista_mensaje[0] != "defVar":
            
            resultado = False
        
        if Lista_mensaje[contador] in  declaraciones_variables and Lista_mensaje[contador+1] not in variables:
            
            resultado = False
            
        if Lista_mensaje[contador] in variables and Lista_mensaje[contador+1] not in valores_iniciales:
            
            resultado = False
            
        if Lista_mensaje[contador] in  valores_iniciales and (Lista_mensaje[contador+1] not in declaraciones_procedimientos) and (Lista_mensaje[contador+1] not in declaraciones_variables):
           
            resultado = False
            
        if Lista_mensaje[contador] in  declaraciones_procedimientos and Lista_mensaje[contador+1] not in nombre_procedimiento:
            
            resultado = False
            
        if Lista_mensaje[contador] in  nombre_procedimiento and Lista_mensaje[contador+1] not in parentesis_abrir:
            
            resultado = False
            
        if Lista_mensaje[contador] in  parentesis_abrir and Lista_mensaje[contador+1] not in parentesis_cierre and Lista_mensaje[contador+1] not in comandos_normales:
            
            resultado = False
            
        if Lista_mensaje[contador] in  comandos_normales and Lista_mensaje[contador+1] not in parentesis_cierre and Lista_mensaje[contador+1] not in coma:
        
            resultado = False
            
        if Lista_mensaje[contador] in  coma and Lista_mensaje[contador+1] not in comandos_normales and Lista_mensaje[contador+1] not in direcciones:
   
            resultado = False
            
        if Lista_mensaje[contador] in  corchete_abrir and Lista_mensaje[contador+1] not in comandos_simples and Lista_mensaje[contador+1] not in comandos_dobles:
            
            resultado = False
            
        if Lista_mensaje[contador] in comandos_simples and Lista_mensaje[contador+1] not in parentesis_abrir and Lista_mensaje[contador+2] not in comandos_normales and Lista_mensaje[contador+3] not in parentesis_cierre:
            
            resultado= False
            
        contador+=1
            
    print(resultado)
    print(Lista_mensaje)
    
    
mensajillo = "defVarnomb1defVarramb2defProcgoNorth1"

mensaje(mensajillo)
            