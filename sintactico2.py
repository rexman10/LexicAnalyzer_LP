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
    '''all_block_code           : block_code
                                | block_code all_block_code  
    '''

def p_block_code(p):
    '''block_code               : def_const_or_var
    '''

def p_def_const_or_var(p):
    '''def_const_or_var         : constant_assignation
                                | variable_assignation
    '''

def p_constant_assignation(p):
    '''constant_assignation     : access_modifiers CONST assignation_type_value_multiple DOTANDCOMMA
                                | CONST assignation_type_value_multiple DOTANDCOMMA
    '''

def p_variable_assignation(p):
    '''variable_assignation     : access_modifiers assignation_type_value_multiple DOTANDCOMMA
                                | CONST assignation_type_value_multiple DOTANDCOMMA
    '''

def p_access_modifiers(p):
    '''access_modifiers         : PUBLIC
                                | PRIVATE
    '''

def p_assignation_type_value(p):
    '''assignation_type_value   : INTTYPE assignation_int
                                | STRINGTYPE assignation_string
                                | FLOATTYPE assignation_float
                                | BOOLTYPE assignation_true
                                | BOOLTYPE assignation_false
    '''

def p_assignation_int(p):
    '''assignation_int          : VARIABLE ASSIGNATION INTEGER      '''

def p_assignation_string(p):
    '''assignation_string       : VARIABLE ASSIGNATION STRING       '''

def p_assignation_float(p):
    '''assignation_float        : VARIABLE ASSIGNATION FLOAT_NUMBER '''

def p_assignation_true(p):
    '''assignation_true         : VARIABLE ASSIGNATION BOOLTRUE     '''

def p_assignation_false(p):
    '''assignation_false        : VARIABLE ASSIGNATION BOOLFALSE     '''


def p_assignation_type_value_multiple(p):
    '''assignation_type_value_multiple          : INTTYPE assignation_int_multiple
                                                | STRINGTYPE assignation_string_multiple
                                                | FLOATTYPE assignation_float_multiple
                                                | BOOLTYPE assignation_true_multiple
                                                | BOOLTYPE assignation_false_multiple
    '''
   
def p_assignation_int_multiple(p):
    '''assignation_int_multiple                 : assignation_int
                                                | assignation_int COMMA assignation_int_multiple
    '''

def p_assignation_string_multiple(p):
    '''assignation_string_multiple              : assignation_string
                                                | assignation_string COMMA assignation_string_multiple
    '''

def p_assignation_float_multiple(p):
    '''assignation_float_multiple               : assignation_float
                                                | assignation_float COMMA assignation_float_multiple
    '''

def p_assignation_true_multiple(p):
    '''assignation_true_multiple                : assignation_true
                                                | assignation_true COMMA assignation_true_multiple
    '''

def p_assignation_false_multiple(p):
    '''assignation_false_multiple               : assignation_false
                                                | assignation_false COMMA assignation_false_multiple
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
        int var = 4;
        int var2 = 5 , var3 = 6;
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