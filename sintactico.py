import ply.yacc as yacc

from main import tokens

""" Ejemplos con los que probar:
using system public class clase1 { adas } 
using system public class clase1 { try{ acacsacasc } catch (exception e){ dsadas } }
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
def p_block_code(p):
    '''block_code : VARIABLE
                    | try_catch_simply
    '''

def p_try_catch_simply(p):
    'try_catch_simply : TRY LKEY block_code RKEY CATCH LPARENT EXCEPTION VARIABLE RPARENT LKEY block_code RKEY'
    


def p_operator(p):
    '''operator : logic_operator
                | arithmetic_operator
    '''

def p_logic_operators(p):
    '''logic_operator   : GREATER_THAN
                        | SMALLER_THAN
                        | EQUAL_COMPARATION
                        | INEQUALITY
                        | GREATER_THAN_OR_EQUAL
                        | SMALLER_THAN_OR_EQUAL
                        | LOGICAND
                        | LOGICOR
                        | LOGICNOT
    '''

def p_arithmetic_operator(p):
    '''arithmetic_operator  : PLUS
                            | MINUS
                            | TIMES
                            | DIVIDE
                            | PERCENT
    '''


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