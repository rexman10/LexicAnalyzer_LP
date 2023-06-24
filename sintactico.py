import ply.yacc as yacc

from main import tokens

""" Ejemplos con los que probar:
using System public class clase1 { adas } 
using System public class clase1 { try{ acacsacasc } catch (exception e){ dsadas } }
 """
 
def p_program(p):
    'program : block_using block_publicClass'

def p_block_using(p):
    'block_using : USING SYSTEM'

def p_block_publicClass(p):
    'block_publicClass : PUBLIC CLASS VARIABLE LKEY block_code RKEY'

""" def p_block_try_catch(p):
    '''block_try_catch : try_catch_simply
                        | try_catch_finaly
    ''' """

def p_data_type(p):
    '''data_type    : CHARTYPE
                    | STRINGTYPE
                    | FLOATTYPE
                    | DECIMALTYPE
                    | INTTYPE
                    | BOOLTYPE
    '''

def p_access_modifiers(p):
    '''access_modifiers : PUBLIC
                        | PRIVATE
    '''

def p_arithmetic_operation(p):
    '''arithmetic_operation : value_numeric
                            | value_numeric arithmetic_operator arithmetic_operation
    '''

def p_value_numeric(p):
    '''value_numeric    : INTEGER
                        | FLOAT_NUMBER
                        | DECIMAL_NUMBER
                        | VARIABLE
    '''

def p_value_logic(p):
    '''value_logic  : BOOLTRUE
                    | BOOLFALSE
                    | VARIABLE
    '''

def p_logic_operation(p):
    '''logic_operation  : value_logic
                        | value_logic logic_operator logic_operation
    '''

def p_concatenation(p):
    '''concatenation    : STRING
                        | STRING PLUS concatenation
    '''

def p_value_string(p):
    '''value_string : STRING
                    | CHAR
                    | VARIABLE
                    | READ LPARENT RPARENT
                    | concatenation
    '''

def p_value(p):
    '''value    : value_numeric
                | value_logic
                | value_string
    '''

def p_logic_operator(p):
    '''logic_operator   : GREATER_THAN
                        | SMALLER_THAN
                        | EQUAL_COMPARATION
                        | INEQUALITY
                        | GREATER_THAN_OR_EQUAL
                        | SMALLER_THAN_OR_EQUAL
                        | LOGICAND
                        | LOGICOR
                        | LOGICNOT
                        | LOGICXOR
    '''

def p_arithmetic_operator(p):
    '''arithmetic_operator  : PLUS
                            | MINUS
                            | TIMES
                            | DIVIDE
                            | PERCENT
    '''
def p_constant_assignation(p):
    '''constant_assignation : access_modifiers CONST data_type VARIABLE ASSIGNATION value
                            | CONST data_type VARIABLE ASSIGNATION value
    '''

def p_variable_assignation_simple(p):
    '''variable_assignation_simple  : access_modifiers data_type VARIABLE ASSIGNATION value
                                    | data_type VARIABLE ASSIGNATION value
                                    | data_type VARIABLE
                                    | VARIABLE ASSIGNATION value
    '''

def p_variable_multivalue(p):
    '''variable_multivalue  : variable_assignation_simple
                            | variable_assignation_simple COMMA variable_multivalue
    '''

def p_variable_assignation_multiline(p):
    '''variable_assignation_multiline   : 
    '''

def p_block_code(p):
    '''block_code : VARIABLE
                    | try_catch_simply
    '''

def p_try_catch_simply(p):
    'try_catch_simply : TRY LKEY block_code RKEY CATCH LPARENT EXCEPTION VARIABLE RPARENT LKEY block_code RKEY'
    



def p_error(p):
    if p:
         print("Error de sintaxis en token:", p.type)
         #sintactico.errok()
    else:
         print("Syntax error at EOF")

# Build the parser
sintactico = yacc.yacc()

while True:
   try:
       s = input('C# > ')
   except EOFError:
       break
   if not s: continue
   result = sintactico.parse(s)
   if result!=None: print(result)