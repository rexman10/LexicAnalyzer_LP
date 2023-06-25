import ply.yacc as yacc

from lexico import tokens

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

using System; public class clase1 { List<string> nombres = new List<string>();}
using System; public class clase1 { List<string> nombres = new List<string>(); nombres.Clear(); nombres.Count();}

using System; public class clase1 { List<string> nombres = new List<string>(); nombres.Add("dgf"); nombres.RemoveAt(0);}
using System; public class clase1 { List<string> nombres = new List<string>(){"Adair"} }
using System; public class clase1 { List<int> nombres = new List<int>(){4} }
using System; public class clase1 { List<int> nombres = new List<int>(){4 , 5, 5, 6} }

using System; public class clase1 { int var2 = 14 ; var3 = var2 ; List<string> nombres = new List<string>(){"Adair"} }

Implementacion sencilla IF por pruebas
using System; public class clase1 { if(52) {44} else if (52) {514} else {52} }
using System; public class clase1 { if(52) {44} else {52} }

Por el momento falla por un token
using System; public class clase1 { Dictionary<string, int> myDict = new Dictionary<string, int>() { { "key1", 1 }, { "key2", 2 } }; }
using System; public class clase1 { Dictionary<string, int> myDict = new Dictionary<string, int>() { { key1, 1 }, { key2, 2 } }; }
"""
 
def p_program(p):
    'program : block_using block_publicClass'

def p_block_using(p):
    'block_using : USING SYSTEM DOTANDCOMMA'

def p_block_publicClass(p):
    'block_publicClass : PUBLIC CLASS VARIABLE LKEY all_block_code RKEY'


def p_all_block_code(p):
    '''all_block_code : block_code
                        | block_code all_block_code  
    '''

def p_block_code(p):
    '''block_code : def_const_or_var
                    | estruct_of_data
                    | block_try_catch
                    | VARIABLE
                    | declaration_dict
                    | functions_list
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



""" Estructura de datos """

def p_declaration_dict(p):
    '''declaration_dict : DICTIONARY VARIABLE ASSIGNATION dictionary_value'''

def p_dictionary_value(p):
    '''dictionary_value : LKEY key_value_pairs RKEY'''

def p_key_value_pairs(p):
    '''key_value_pairs : key_value_pair
                       | key_value_pair COMMA key_value_pairs'''

def p_key_value_pair(p):
    '''key_value_pair : STRING DOUBLEPOINT value'''

#definicion repetida, para prueba
def p_valueHash(p):
    '''valueHash : INTTYPE
             | STRING'''



def p_estruct_of_data(p):
    '''estruct_of_data : list_empty
                        | list_full
    '''

def p_list_empty(p):
    '''list_empty : LIST SMALLER_THAN STRINGTYPE GREATER_THAN VARIABLE ASSIGNATION NEW LIST SMALLER_THAN STRINGTYPE GREATER_THAN LPARENT RPARENT DOTANDCOMMA
                    | LIST SMALLER_THAN INTTYPE GREATER_THAN VARIABLE ASSIGNATION NEW LIST SMALLER_THAN INTTYPE GREATER_THAN LPARENT RPARENT DOTANDCOMMA
    '''
    
def p_list_full(p):
    '''list_full : LIST SMALLER_THAN STRINGTYPE GREATER_THAN VARIABLE ASSIGNATION NEW LIST SMALLER_THAN STRINGTYPE GREATER_THAN LPARENT RPARENT LKEY strings_list RKEY
                    | LIST SMALLER_THAN INTTYPE GREATER_THAN VARIABLE ASSIGNATION NEW LIST SMALLER_THAN INTTYPE GREATER_THAN LPARENT RPARENT LKEY ints_list RKEY
    '''

def p_strings_list(p):
    '''strings_list : STRING
                    | STRING COMMA strings_list
    '''

def p_ints_list(p):
    '''ints_list : INTEGER
                | INTEGER COMMA ints_list
    '''

def p_functions_list(p):
    '''functions_list : list_func_clear
                        | list_func_count
                        | list_func_add
                        | list_func_removeat
    '''

def p_list_func_clear(p):
    "list_func_clear : VARIABLE DOT CLEAR LPARENT RPARENT DOTANDCOMMA"

def p_list_func_count(p):
    "list_func_count : VARIABLE DOT COUNT LPARENT RPARENT DOTANDCOMMA"

def p_list_func_add(p):
    "list_func_add : VARIABLE DOT ADD LPARENT STRING RPARENT DOTANDCOMMA"

def p_list_func_removeat(p):
    "list_func_removeat : VARIABLE DOT REMOVEAT LPARENT INTEGER RPARENT DOTANDCOMMA"

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