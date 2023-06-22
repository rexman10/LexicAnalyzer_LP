import ply.yacc as yacc

from main import tokens

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