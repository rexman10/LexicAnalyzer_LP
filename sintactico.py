import ply.yacc as yacc

from main import tokens

""" Ejemplos con los que probar:
using System; public class clase1 { adas } 
using System; public class clase1 { try{ acacsacasc } catch (exception e){ dsadas } }
using System; public class clase1 { try{ acacsacasc } catch (exception e){ dsadas } finally { final } }
using System; public class clase1 { const int var2 = 14 ; }
using System; public class clase1 { const int var2 = 14 , var3 = 15 ; }
using System; public class clase1 { int var2 = 14 ; }
using System; public class clase1 { int var2 = 14 ; var3 = var2 ; }
using System; public class clase1 { int var2 = 14 ; var3 = var2 ; var5 = 4 ; }
using System; public class clase1 { const int var2 = 14 ; var3 = var2 ; int var5 = 4 ; }
using System; public class clase1 { const int var2 = 14 ; var3 = var2 ; const int var5 = 4 ; }
"""
 
def p_program(p):
    'program : block_using block_publicClass'

def p_block_using(p):
    'block_using : USING SYSTEM DOTANDCOMMA'

def p_block_publicClass(p):
    'block_publicClass : PUBLIC CLASS VARIABLE LKEY block_code RKEY'



def p_block_code(p):
    '''block_code : def_const_or_var
                    | block_try_catch
                    | VARIABLE
    '''




""" Declaracion de variables y constantes """

def p_def_const_or_var(p):
    '''def_const_or_var : constant_assignation
                        | variable_assignation
    '''

def p_variable_assignation(p):
    '''variable_assignation : access_modifiers all_asignations
                            | all_asignations

    '''

def p_constant_assignation(p):
    '''constant_assignation : access_modifiers CONST all_asignations
                            | CONST all_asignations
                            | CONST data_type assignation_key_value COMMA some_assignation_constant
    '''

def p_all_asignations(p):
    '''all_asignations : assignation_with_datatype
                        | assignation_without_datatype
    '''

def p_assignation_with_datatype(p):
    '''assignation_with_datatype : data_type assignation_key_value DOTANDCOMMA
                            | data_type assignation_key_value DOTANDCOMMA assignation_with_datatype   
                            | data_type assignation_key_value DOTANDCOMMA assignation_without_datatype                     
    '''

def p_assignation_without_datatype(p):
    '''assignation_without_datatype : assignation_key_value DOTANDCOMMA
                                    | assignation_key_value DOTANDCOMMA assignation_without_datatype
                                    | assignation_key_value DOTANDCOMMA assignation_with_datatype
    '''

def p_some_assignation_constant(p):
    '''some_assignation_constant : assignation_key_value DOTANDCOMMA
                                | assignation_key_value COMMA some_assignation_constant
    '''

def p_assignation_key_value(p):
    'assignation_key_value : VARIABLE ASSIGNATION value'

def p_data_type(p):
    '''data_type    : CHARTYPE
                    | STRINGTYPE
                    | FLOATTYPE
                    | DECIMALTYPE
                    | INTTYPE
                    | BOOLTYPE
    '''




""" Tipo de valores validos para asignar """

def p_value(p):
    '''value    : value_numeric
                | value_logic
                | value_string
    '''

def p_value_string(p):
    '''value_string : STRING
                    | CHAR
                    | VARIABLE
                    | READ LPARENT RPARENT
                    | concatenation
    '''

def p_value_logic(p):
    '''value_logic  : BOOLTRUE
                    | BOOLFALSE
    '''

def p_value_numeric(p):
    '''value_numeric    : INTEGER
                        | FLOAT_NUMBER
                        | DECIMAL_NUMBER
    '''




""" Estructuras de control """

def p_block_try_catch(p):
    '''block_try_catch : try_catch_simply
                        | try_catch_finally
    '''

def p_try_catch_simply(p):
    'try_catch_simply : TRY LKEY block_code RKEY CATCH LPARENT EXCEPTION VARIABLE RPARENT LKEY block_code RKEY'
    
def p_try_catch_finally(p):
    'try_catch_finally : TRY LKEY block_code RKEY CATCH LPARENT EXCEPTION VARIABLE RPARENT LKEY block_code RKEY FINALLY LKEY block_code RKEY'


def p_access_modifiers(p):
    '''access_modifiers : PUBLIC
                        | PRIVATE
    '''





""" Oeraciones """

def p_arithmetic_operation(p):
    '''arithmetic_operation : value_numeric
                            | value_numeric arithmetic_operator arithmetic_operation
    '''

def p_logic_operation(p):
    '''logic_operation  : value_logic
                        | value_logic logic_operator logic_operation
    '''

def p_concatenation(p):
    '''concatenation    : STRING
                        | STRING PLUS concatenation
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

def p_variable_assignation_multiline(p):
    '''variable_assignation_multiline   : 
    '''




""" def p_conditional(p):
    'conditional : if else_if else'

def p_if(p):
    'if : IF LPARENT <condicion> RPARENT LKEY <bloque> RKEY'
    
def p_else_if(p):
    'else_if : ELSE_IF < condicion > RPARENT LKEY < bloque > RKEY'

def p_else(p):
    'else : ELSE LKEY <bloque> RKEY'

def p_block_code_if(p):
    '''
    block_code_if : VARIABLE |
                    conditional
    '''

def p_condicion(p):
    '''condicion : operandos comparation_oper operandos'|
     logic_oper operandos comparation_oper operandos'''

def p_bloque(p):
    'bloque : value_string'

def P_operandos(p):
    'operandos : value_numeric'

#siguuientes dos deficniones son de prueba. son divisones de logic_operator() de la linea 84
def p_logic_oper(p):
    '''logic_oper : LOGICAND |
                    LOGICOR'''
    
def p_comparation_oper(p):
    '''comparation_oper : EQUAL_COMPARATION |
                            INEQUALITY |
                            GREATER_THAN |
                            SMALLER_THAN |
                            GREATER_THAN_OR_EQUAL |
                            SMALLER_THAN_OR_EQUAL
    ''' """



""" Estructura de datos """




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