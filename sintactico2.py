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

def p_block_code(p):
    '''block_code               : def_const_or_var
                                | print_data
                                | boolean_operation
                                | arithmetic_operation
    '''

def p_all_block_code(p):
    '''all_block_code           : block_code
                                | block_code all_block_code        
    '''

# Tipos de datos disponibles

def p_data_type(p):
    '''data_type                : CHARTYPE
                                | STRINGTYPE
                                | FLOATTYPE
                                | DECIMALTYPE
                                | INTTYPE
                                | BOOLTYPE
    '''

# Valores disponibles

def p_value_string(p):
    '''value_string             : STRING
                                | CHAR
                                | concatenation
    '''

def p_value_boolean(p):
    '''value_boolean            : BOOLTRUE
                                | BOOLFALSE
                                | VARIABLE
                                | comparison_operation
    '''

def p_value_numeric(p):
    '''value_numeric            : INTEGER
                                | FLOAT_NUMBER
                                | DECIMAL_NUMBER
                                | VARIABLE
    '''

def p_print_data(p):
    '''print_data               : PRINT LPARENT STRING RPARENT DOTANDCOMMA
                                | PRINT LPARENT VARIABLE RPARENT DOTANDCOMMA
    '''

def p_read_data(p):
    '''read_data                : READ LPARENT RPARENT DOTANDCOMMA
    '''

def p_concatenation(p):
    '''concatenation            : STRING
                                | STRING PLUS concatenation
    '''

def p_value(p):
    '''value                    : value_numeric
                                | value_boolean
                                | value_string
                                | VARIABLE
                                | read_data
    '''

# Operaciones logicas y aritmeticas

def p_arithmetic_operation(p):
    '''arithmetic_operation     : value_numeric
                                | value_numeric arithmetic_operator arithmetic_operation
    '''

def p_arithmetic_operator(p):
    '''arithmetic_operator      : PLUS
                                | MINUS
                                | TIMES
                                | DIVIDE
                                | PERCENT
    '''

def p_comparison_operation(p):
    '''comparison_operation     : value_numeric
                                | value_numeric comparison_operator comparison_operation
    '''

def p_comparison_operator(p):
    '''comparison_operator      : GREATER_THAN
                                | SMALLER_THAN
                                | EQUAL_COMPARATION
                                | INEQUALITY
                                | GREATER_THAN_OR_EQUAL
                                | SMALLER_THAN_OR_EQUAL
    '''

def p_boolean_operation(p):
    '''boolean_operation        : value_boolean
                                | LOGICNOT value_boolean
                                | value_boolean boolean_operator boolean_operation
    '''

def p_boolean_operator(p):
    '''boolean_operator         : LOGICAND
                                | LOGICOR
    '''

# Definicion de variables y constantes

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
    '''assignation_key_value    : data_type VARIABLE ASSIGNATION value
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
        x >= 34 && x == 34
        x <= 34 || x == 34
        x > 34
        x < 34
        x != 34
        x == 34
        123 / 123123 + 5345 * 123124 - 4365
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