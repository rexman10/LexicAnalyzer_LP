import ply.yacc as yacc
from lexico import tokens

errores=[]


def p_program(p):
    'program                    : USING SYSTEM DOTANDCOMMA block_publicClass'

def p_block_publicClass(p):
    '''block_publicClass        : PUBLIC CLASS VARIABLE LKEY block_main_method RKEY
    '''

def p_block_main_method(p):
    '''block_main_method        : STATIC VOID MAIN LPARENT STRINGTYPE LBRACKET RBRACKET VARIABLE RPARENT LKEY all_block_code RKEY
    '''

def p_all_block_code(p):
    '''all_block_code           : def_const_or_var        
    '''

def p_def_const_or_var(p):
    '''def_const_or_var         : variable_assignation
    '''

def p_variable_assignation(p):
    '''variable_assignation     : access_modifiers assignation_key_value DOTANDCOMMA
                                | assignation_key_value DOTANDCOMMA
    '''

def p_access_modifiers(p):
    '''access_modifiers         : PUBLIC
                                | PRIVATE
    '''

def p_assignation_key_value(p):
    '''assignation_key_value    : INTTYPE VARIABLE ASSIGNATION INTEGER
    '''

def p_error(p):
    if p:
         print("Error de sintaxis en token:", p.type, "in: ", p.lexpos, p.value)
         #sintactico.errok()
    else:
         print("Syntax error at EOF")


# Build the parser
sintactico = yacc.yacc()

datos = '''
using System;
public class clase1 {
    static void Main (string[] args) {
        int var = "hola";
    }
}
'''

print(datos)

def analizar_sintactico_string(content):
    result = sintactico.parse(content)
    #return result is not None
    if result!=None:
        print(result)
        return result

var = analizar_sintactico_string(datos)