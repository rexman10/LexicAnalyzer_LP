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
using System; public class clase1 { Action<string> clase = x => {} }

Implementacion sencilla IF por pruebas
using System; public class clase1 { if(52) {44} else if (52) {514} else {52} }
using System; public class clase1 { if(52) {44} else {52} }

using System; public class clase1 { Dictionary<> myDict = new Dictionary<>(); }
using System; public class clase1 { Dictionary<> myDict = new Dictionary<>(); myDict.put(key, value);}
using System; public class clase1 { Dictionary<> myDict = new Dictionary<>(); myDict.remove(key);}

using System; public class clase1 { Dictionary<string, int> myDict = new Dictionary<string, int>() { { key, 1 }, { key, 2 } }; 
using System; public class clase1 { Dictionary<> myDict = new Dictionary<>() { { key1, 1 }, { key2, 2 } }; 

Pruebas condicionales
using System; public class clase1 { if(){} else_if (){} else_if(){} else{}} 
using System; public class clase1 { if(){mama} else_if (){mama} else_if(){nana} else{kaka}} 
    if anidado, cada vez auentar un nivel
using System; public class clase1 { if(){if(){mama} else{msms} } else_if (){if(){hfghg} else{ghfhgf}} else_if(){dfds} else{kaka}}

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
                    | block_while
                    | VARIABLE
                    | dict_estruct
                    | functions_dict
                    | functions_list
                    | declaration_lambda
                    | block_if
                    | print_data
                    | block_for
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
def p_print_data(p):
    '''print_data       : PRINT RPARENT STRING LPARENT DOTANDCOMMA
    '''

def p_read_data(p):
    '''read_data        : READ RPARENT LPARENT
    '''

def p_value(p):
    '''value    : value_numeric
                | value_logic
                | value_string
                | read_data
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

def p_block_for(p):
    '''block_for        : for_anidado
                        | for_each
    '''

def p_for_simple(p):
    '''for_simple       : FOR LPARENT assignation_with_datatype logic_operation DOTANDCOMMA VARIABLE INCREMENT RPARENT LKEY block_code RKEY
                        | FOR LPARENT assignation_with_datatype logic_operation DOTANDCOMMA VARIABLE DECREMENT RPARENT LKEY block_code RKEY

    '''

def p_for_anidado(p):
    '''for_anidado      : for_simple
                        | FOR LPARENT assignation_with_datatype logic_operation DOTANDCOMMA VARIABLE INCREMENT RPARENT LKEY for_anidado RKEY
                        | FOR LPARENT assignation_with_datatype logic_operation DOTANDCOMMA VARIABLE DECREMENT RPARENT LKEY for_anidado RKEY 
    '''

def p_for_each(p):
    '''for_each         : FOREACH LPARENT data_type VARIABLE IN VARIABLE RPARENT LKEY block_code RKEY
    '''

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

def p_block_while(p):
    '''block_while : normal_while
                   | do_while             
    '''

def p_normal_while(p):
    'normal_while : WHILE LPARENT logic_operation RPARENT LKEY block_code RKEY'

def p_do_while(p):
    'do_while : DO LKEY block_code RKEY WHILE LPARENT logic_operation RPARENT'

def p_block_if(p):
    'block_if : IF LPARENT logic_operation RPARENT LKEY not_yes_nested_if RKEY other_if'

def p_other_if(p):
    '''
    other_if : ELSE LKEY not_yes_nested_if RKEY
               | ELSE_IF LPARENT logic_operation RPARENT LKEY not_yes_nested_if RKEY other_if
    '''

def p_not_yes_nested_if(p):
    '''
    not_yes_nested_if : block_if
                       | block_code
    '''

""" Operaciones """

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

def p_dict_estruct(p):
    '''
    dict_estruct : dict_empty
                   | dict_full
    '''

#variable = random mix
def p_dict_empty(p):
    '''
    dict_empty : DICTIONARY SMALLER_THAN GREATER_THAN VARIABLE ASSIGNATION NEW DICTIONARY SMALLER_THAN GREATER_THAN LPARENT RPARENT DOTANDCOMMA
    '''

def p_dict_full(p):
    '''
    dict_full : DICTIONARY SMALLER_THAN GREATER_THAN VARIABLE ASSIGNATION NEW DICTIONARY SMALLER_THAN GREATER_THAN LPARENT RPARENT LKEY dictionary_value RKEY DOTANDCOMMA
    '''

def p_dictionary_value(p):
    '''dictionary_value : LKEY key_value_pair RKEY'''

def p_key_value_pairs(p):
    '''key_value_pairs : key_value_pair
                       | key_value_pair COMMA key_value_pairs'''

#Key: String Value: String | int
def p_key_value_pair(p):
    '''key_value_pair : STRING DOUBLEPOINT valueHash'''

#definicion repetida, para prueba
def p_valueHash(p):
    '''valueHash : INTTYPE
                '''
def p_estruct_of_data(p):
    '''estruct_of_data : list_empty
                        | list_full
    '''

def p_functions_dict(p):
    '''
    functions_dict : dict_func_put
                    | dict_func_remove
    '''

def p_dict_func_put(p):
    '''
    dict_func_put : STRING DOT PUT LPARENT STRING COMMA STRING RPARENT DOTANDCOMMA
    '''

def p_dict_func_remove(p):
    '''
    dict_func_remove : STRING DOT REMOVE LPARENT STRING RPARENT DOTANDCOMMA
    '''

#Agg la funcion Valueof

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





""" Declaración de funciones """
def p_declration_lambda(p):
    "declaration_lambda : ACTION SMALLER_THAN STRINGTYPE GREATER_THAN VARIABLE ASSIGNATION VARIABLE ARROW LKEY RKEY"



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