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
using System; public class clase1 { List<string> nombres = new List<string>(){"Adair"}; }
using System; public class clase1 { List<int> nombres = new List<int>(){4}; }
using System; public class clase1 { List<int> nombres = new List<int>(){4 , 5, 5, 6}; }

using System; public class clase1 { int var2 = 14 ; var3 = var2 ; List<string> nombres = new List<string>(){"Adair"}; }
using System; public class clase1 { Action<string> clase = x => {} }

Implementacion sencilla IF por pruebas
using System; public class clase1 { if(52) {44} else if (52) {514} else {52} }
using System; public class clase1 { if(52) {44} else {52} }

using System; public class clase1 { Dictionary<> myDict = new Dictionary<>(); }
using System; public class clase1 { Dictionary<> myDict = new Dictionary<>(); myDict.put(key, value);}
using System; public class clase1 { Dictionary<> myDict = new Dictionary<>(); myDict.remove(key);}

using System; public class clase1 { Dictionary<string, int> myDict = new Dictionary<string, int>() { { key, 1 }, { key, 2 } }; }
using System; public class clase1 { Dictionary<> myDict = new Dictionary<>() { { key1, 1 }, { key2, 2 } }; }

Pruebas condicionales
using System; public class clase1 { if(){} else_if (){} else_if(){} else{}} 
using System; public class clase1 { if(){mama} else_if (){mama} else_if(){nana} else{kaka}} 
    if anidado, cada vez auentar un nivel
using System; public class clase1 { if(){if(){mama} else{msms} } else_if (){if(){hfghg} else{ghfhgf}} else_if(){dfds} else{kaka}}

using System; 
public class clase1 {
    for(int ida=0; i < 0; i++){
        Console.WriteLine(ida);
    }
}

using System; 
public class clase1 { 
    const int var2 = 14 , var3 = 15 ;
    List<int> nombres = new List<int>(){4 , 5, 5, 6}; 
    nombres.Add("dgf"); 
    nombres.RemoveAt(0);
    int var2 = 14; 
    var3 = var2 ; 
    var5 = 4 ;
    Dictionary<> myDict = new Dictionary<>(); myDict.remove(key);
    Dictionary<> myDict2 = new Dictionary<>() { { key1, 1 }, { key2, 2 } };
    Console.WriteLine("hasta luego");
    Console.WriteLine(myDict2);
}
"""
 
def p_program(p):
    'program                    : USING SYSTEM DOTANDCOMMA block_publicClass'

def p_block_publicClass(p):
    '''block_publicClass        : PUBLIC CLASS VARIABLE LKEY all_method_definitions block_main_method RKEY
                                | PUBLIC CLASS VARIABLE LKEY block_main_method RKEY
                                | PUBLIC CLASS VARIABLE LKEY all_method_definitions RKEY
    '''

def p_block_main_method(p):
    '''block_main_method        : STATIC VOID MAIN LPARENT STRINGTYPE LBRACKET RBRACKET VARIABLE RPARENT LKEY all_block_code RKEY
    '''

def p_block_code(p):
    '''block_code               : def_const_or_var
                                | print_data
                                | read_data
                                | arithmetic_operation
                                | logic_operation
                                | array_assignation
                                | array_value_assign
                                | array_indexing

                                | lists
                                | functions_list

                                | dict_estruct
                                | functions_dict
                                | concurrent_method

                                | queue_struct
                                | functions_queue

                                | stack_struct
                                | functions_stack

                                | block_if

                                | block_for

                                | block_try_catch

                                | block_while
    '''

def p_all_block_code(p):
    '''all_block_code           : block_code
                                | block_code all_block_code  
    '''

def p_method_definition(p):
    '''method_definition        : simple_method
                                | declaration_async
                                | declaration_lambda
    '''

def p_all_method_definitions(p):
    '''all_method_definitions   : method_definition
                                | method_definition all_method_definitions  
    '''

""" Tipo de valores validos para asignar """
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
                                | value_logic
                                | value_string
                                | read_data
                                | METHOD
                                | array
    '''

def p_array_assignation(p):
    'array_assignation          : array_type VARIABLE ASSIGNATION LBRACKET array_content RBRACKET DOTANDCOMMA'

def p_array(p):
    'array                      : LBRACKET array_content RBRACKET'

def p_array_content(p):
    '''array_content            : value
                                | value COMMA array_content
    '''

def p_array_indexing(p):
    '''array_indexing           : VARIABLE LBRACKET VARIABLE RBRACKET
                                | VARIABLE LBRACKET INTEGER RBRACKET
    '''

def p_array_value_assign(p):
    '''array_value_assign       : VARIABLE LBRACKET VARIABLE RBRACKET ASSIGNATION value DOTANDCOMMA
                                | VARIABLE LBRACKET INTEGER RBRACKET ASSIGNATION value DOTANDCOMMA
    '''

def p_value_string(p):
    '''value_string             : STRING
                                | CHAR
                                | VARIABLE
                                | concatenation
    '''

def p_value_logic(p):
    '''value_logic              : BOOLTRUE
                                | BOOLFALSE
                                | logic_operation
    '''

def p_value_numeric(p):
    '''value_numeric            : INTEGER
                                | FLOAT_NUMBER
                                | DECIMAL_NUMBER
                                | arithmetic_operation
    '''

""" Operaciones logicas y aritmeticas"""
def p_arithmetic_operation(p):
    '''arithmetic_operation     : value_numeric
                                | VARIABLE
                                | value_numeric arithmetic_operator arithmetic_operation
                                | VARIABLE arithmetic_operator arithmetic_operation
    '''

def p_logic_operation(p):
    '''logic_operation          : value_numeric logic_operator INTEGER 
                                | VARIABLE logic_operator INTEGER
    '''

def p_logic_operator(p):
    '''logic_operator           : GREATER_THAN
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
    '''arithmetic_operator      : PLUS
                                | MINUS
                                | TIMES
                                | DIVIDE
                                | PERCENT
    '''

""" Declaracion de variables y constantes """
def p_access_modifiers(p):
    '''access_modifiers         : PUBLIC
                                | PRIVATE
    '''

def p_def_const_or_var(p):
    '''def_const_or_var         : constant_assignation
                                | variable_assignation
                                | late_initialization
    '''

def p_constant_assignation(p):
    '''constant_assignation     : access_modifiers CONST data_type assignation_key_value DOTANDCOMMA
                                | CONST data_type assignation_key_value DOTANDCOMMA
                                | access_modifiers CONST data_type assignation_key_value_multiple DOTANDCOMMA
                                | CONST data_type assignation_key_value_multiple DOTANDCOMMA
    '''

def p_variable_assignation(p):
    '''variable_assignation     : access_modifiers data_type assignation_key_value DOTANDCOMMA
                                | data_type assignation_key_value DOTANDCOMMA
                                | access_modifiers data_type assignation_key_value_multiple DOTANDCOMMA
                                | data_type assignation_key_value_multiple DOTANDCOMMA
    '''

def p_late_initialization(p):
    '''late_initialization      : access_modifiers data_type VARIABLE DOTANDCOMMA
                                | data_type VARIABLE DOTANDCOMMA
                                | assignation_key_value DOTANDCOMMA
    '''

def p_assignation_key_value(p):
    '''assignation_key_value    : VARIABLE ASSIGNATION value
                                | READ LPARENT RPARENT
    '''

def p_assignation_key_value_multiple(p):
    '''assignation_key_value_multiple   : assignation_key_value
                                        | assignation_key_value COMMA assignation_key_value_multiple   
    '''

def p_assignation_with_datatype(p):
    '''assignation_with_datatype        : data_type assignation_key_value DOTANDCOMMA
                                        | data_type assignation_key_value COMMA assignation_with_datatype                    
    '''

def p_data_type(p):
    '''data_type                : CHARTYPE
                                | STRINGTYPE
                                | FLOATTYPE
                                | DECIMALTYPE
                                | INTTYPE
                                | BOOLTYPE
                                | array_type
    '''

def p_array_type(p):
    '''array_type               : CHARTYPE LBRACKET RBRACKET
                                | STRINGTYPE LBRACKET RBRACKET
                                | FLOATTYPE LBRACKET RBRACKET
                                | DECIMALTYPE LBRACKET RBRACKET
                                | INTTYPE LBRACKET RBRACKET
                                | BOOLTYPE LBRACKET RBRACKET
    '''

""" Estructuras de control """

def p_logic_operations(p):
    '''logic_operations         : logic_operation DOTANDCOMMA
                                | logic_operation COMMA logic_operations
    '''

def p_block_for(p):
    '''block_for                : for_anidado
                                | for_each
    '''

def p_for_simple(p):
    '''for_simple               : FOR LPARENT assignation_with_datatype logic_operations DOTANDCOMMA VARIABLE INCREMENT RPARENT LKEY all_block_code RKEY
                                | FOR LPARENT assignation_with_datatype logic_operations DOTANDCOMMA VARIABLE DECREMENT RPARENT LKEY all_block_code RKEY

    '''

def p_for_anidado(p):
    '''for_anidado              : for_simple
                                | FOR LPARENT assignation_with_datatype logic_operations DOTANDCOMMA VARIABLE INCREMENT RPARENT LKEY for_anidado RKEY
                                | FOR LPARENT assignation_with_datatype logic_operations DOTANDCOMMA VARIABLE DECREMENT RPARENT LKEY for_anidado RKEY 
    '''

def p_for_each(p):
    '''for_each                 : FOREACH LPARENT data_type VARIABLE IN VARIABLE RPARENT LKEY all_block_code RKEY
    '''

def p_block_try_catch(p):
    '''block_try_catch          : try_catch_simply
                                | try_catch_finally
    '''

def p_try_catch_simply(p):
    'try_catch_simply           : TRY LKEY all_block_code RKEY CATCH LPARENT EXCEPTION VARIABLE RPARENT LKEY all_block_code RKEY'
    
def p_try_catch_finally(p):
    'try_catch_finally          : TRY LKEY all_block_code RKEY CATCH LPARENT EXCEPTION VARIABLE RPARENT LKEY all_block_code RKEY FINALLY LKEY all_block_code RKEY'


def p_block_while(p):
    '''block_while              : normal_while
                                | do_while             
    '''

def p_normal_while(p):
    'normal_while               : WHILE LPARENT logic_operation RPARENT LKEY all_block_code RKEY'

def p_do_while(p):
    'do_while                   : DO LKEY all_block_code RKEY WHILE LPARENT logic_operation RPARENT'

def p_block_if(p):
    'block_if                   : IF LPARENT logic_operation RPARENT LKEY not_yes_nested_if RKEY other_if'

def p_other_if(p):
    '''
    other_if                    : ELSE LKEY not_yes_nested_if RKEY
                                | ELSE_IF LPARENT logic_operation RPARENT LKEY not_yes_nested_if RKEY other_if
    '''

def p_not_yes_nested_if(p):
    '''
    not_yes_nested_if           : block_if
                                | block_code
    '''



""" Estructura de datos """

def p_dict_estruct(p):
    '''
    dict_estruct                : dict_empty
                                | dict_full
    '''

#variable = random mix
def p_dict_empty(p):
    '''
    dict_empty                  : DICTIONARY SMALLER_THAN GREATER_THAN VARIABLE ASSIGNATION NEW DICTIONARY SMALLER_THAN GREATER_THAN LPARENT RPARENT DOTANDCOMMA
    '''

def p_dict_full(p):
    '''
    dict_full                   : DICTIONARY SMALLER_THAN GREATER_THAN VARIABLE ASSIGNATION NEW DICTIONARY SMALLER_THAN GREATER_THAN LPARENT RPARENT LKEY key_value_pairs RKEY DOTANDCOMMA
    '''


def p_key_value_pairs(p):
    '''key_value_pairs          : key_value_pair
                                | key_value_pair COMMA key_value_pairs
    '''

#Key: String Value: String | int
def p_key_value_pair(p):
    '''key_value_pair           : LKEY VARIABLE COMMA value RKEY
    '''


def p_estruct_of_data(p):
    '''estruct_of_data          : list_empty
                                | list_full
    '''

def p_functions_dict(p):
    '''
    functions_dict              : dict_func_put
                                | dict_func_remove
    '''

def p_dict_func_put(p):
    '''
    dict_func_put               : VARIABLE DOT PUT LPARENT STRING COMMA VARIABLE RPARENT DOTANDCOMMA
    '''

def p_dict_func_remove(p):
    '''
    dict_func_remove            : VARIABLE DOT REMOVE LPARENT VARIABLE RPARENT DOTANDCOMMA
    '''

#Agg la funcion Valueof

def p_lists(p):
    ''' lists                   : list_empty
                                | list_full
    '''

def p_list_empty(p):
    '''list_empty               : LIST SMALLER_THAN STRINGTYPE GREATER_THAN VARIABLE ASSIGNATION NEW LIST SMALLER_THAN STRINGTYPE GREATER_THAN LPARENT RPARENT DOTANDCOMMA
                                | LIST SMALLER_THAN INTTYPE GREATER_THAN VARIABLE ASSIGNATION NEW LIST SMALLER_THAN INTTYPE GREATER_THAN LPARENT RPARENT DOTANDCOMMA
    '''
    
def p_list_full(p):
    '''list_full                : LIST SMALLER_THAN STRINGTYPE GREATER_THAN VARIABLE ASSIGNATION NEW LIST SMALLER_THAN STRINGTYPE GREATER_THAN LPARENT RPARENT LKEY strings_list RKEY DOTANDCOMMA
                                | LIST SMALLER_THAN INTTYPE GREATER_THAN VARIABLE ASSIGNATION NEW LIST SMALLER_THAN INTTYPE GREATER_THAN LPARENT RPARENT LKEY ints_list RKEY DOTANDCOMMA
    '''

def p_strings_list(p):
    '''strings_list             : STRING
                                | STRING COMMA strings_list
    '''

def p_ints_list(p):
    '''ints_list                : INTEGER
                                | INTEGER COMMA ints_list
    '''

def p_functions_list(p):
    '''functions_list           : list_func_clear
                                | list_func_count
                                | list_func_add
                                | list_func_removeat
    '''

def p_list_func_clear(p):
    "list_func_clear            : VARIABLE DOT CLEAR LPARENT RPARENT DOTANDCOMMA"

def p_list_func_count(p):
    "list_func_count            : VARIABLE DOT COUNT LPARENT RPARENT DOTANDCOMMA"

def p_list_func_add(p):
    "list_func_add              : VARIABLE DOT ADD LPARENT STRING RPARENT DOTANDCOMMA"

def p_list_func_removeat(p):
    "list_func_removeat         : VARIABLE DOT REMOVEAT LPARENT INTEGER RPARENT DOTANDCOMMA"

def p_stack_struct(p):
    'stack_struct               : STACK VARIABLE ASSIGNATION NEW STACK LPARENT RPARENT DOTANDCOMMA'

def p_functions_stack(p):
    '''functions_stack          : stack_push
                                | stack_pop
                                | stack_clear
                                | stack_peek
                                | stack_isEmpty
    '''

def p_stack_push(p):
    'stack_push                 : VARIABLE DOT PUSH LPARENT value RPARENT DOTANDCOMMA'

def p_stack_pop(p):
    'stack_pop                  : VARIABLE DOT POP LPARENT RPARENT DOTANDCOMMA'

def p_stack_clear(p):
    'stack_clear                : VARIABLE DOT CLEAR LPARENT RPARENT DOTANDCOMMA'

def p_stack_peek(p):
    'stack_peek                 : VARIABLE DOT PEEK LPARENT RPARENT DOTANDCOMMA'

def p_stack_isEmpty(p):
    'stack_isEmpty              : VARIABLE DOT ISEMPTY LPARENT RPARENT DOTANDCOMMA'

def p_queue_struct(p):
    '''queue_struct             : QUEUE SMALLER_THAN data_type GREATER_THAN VARIABLE ASSIGNATION NEW QUEUE SMALLER_THAN data_type GREATER_THAN LPARENT RPARENT DOTANDCOMMA
                                | QUEUE SMALLER_THAN data_type GREATER_THAN VARIABLE ASSIGNATION NEW QUEUE SMALLER_THAN GREATER_THAN LPARENT RPARENT DOTANDCOMMA
    '''

def p_functions_queue(p):
    '''functions_queue          : queue_enqueue
                                | queue_dequeue
                                | queue_clear
                                | queue_isEmpty
                                | queue_peek
    '''

def p_queue_enqueue(p):
    '''queue_enqueue            : VARIABLE DOT ENQUEUE LPARENT value RPARENT DOTANDCOMMA
    '''

def p_queue_dequeue(p):
    '''queue_dequeue            : VARIABLE DOT DEQUEUE LPARENT RPARENT DOTANDCOMMA
    '''

def p_queue_clear(p):
    '''queue_clear              : VARIABLE DOT CLEAR LPARENT RPARENT DOTANDCOMMA
    '''

def p_queue_peek(p):
    '''queue_peek               : VARIABLE DOT PEEK LPARENT RPARENT DOTANDCOMMA
    '''

def p_queue_isEmpty(p):
    '''queue_isEmpty            : VARIABLE DOT ISEMPTY LPARENT RPARENT DOTANDCOMMA
    '''


""" Declaración de funciones """

def p_simple_method(p):
    '''simple_method            : STATIC data_type METHOD LPARENT function_arguments RPARENT LKEY all_block_code function_return RKEY
                                | STATIC VOID METHOD LPARENT function_arguments RPARENT LKEY all_block_code RKEY
                                | STATIC VOID MAIN LPARENT function_arguments RPARENT LKEY all_block_code function_return RKEY
                                | access_modifiers STATIC data_type METHOD LPARENT function_arguments RPARENT LKEY all_block_code function_return RKEY
                                | PUBLIC STATIC VOID METHOD LPARENT function_arguments RPARENT LKEY all_block_code RKEY
    '''

def p_function_return(p):
    '''function_return          : RETURN value DOTANDCOMMA
    '''

def p_function_argument(p):
    '''function_argument        : data_type VARIABLE
                                | data_type CHAR    
                                | METHOD VARIABLE
                                | data_type LBRACKET RBRACKET VARIABLE
    '''

def p_function_arguments(p):
    '''function_arguments       : function_argument
                                | function_argument COMMA function_arguments
    '''

def p_declaration_async(p):
    '''declaration_async        : PUBLIC STATIC ASYNC TASK METHOD LPARENT RPARENT LKEY AWAIT TASK DOT METHOD LPARENT LPARENT RPARENT ARROW LKEY block_code RKEY RPARENT DOTANDCOMMA RKEY
    '''

def p_declration_lambda(p):
    "declaration_lambda         : ACTION SMALLER_THAN STRINGTYPE GREATER_THAN VARIABLE ASSIGNATION VARIABLE ARROW LKEY block_code RKEY"

def p_concurrent_method(p):
    '''concurrent_method        : method_declaration CONCURRENT LKEY concurrent_block RKEY'''

def p_method_declaration(p):
    '''method_declaration       : METHOD IDENTIFIER LPARENT RPARENT DOTANDCOMMA'''

def p_concurrent_block(p):
    '''concurrent_block         : statement_list'''

def p_statement_list(p):
    '''statement_list           : statement
                                | statement_list statement'''

def p_statement(p):
    '''statement                : assignment_concurrent
                                | if_statement_concurrent
                                | while_loop_concurrent
                                | method_call_concurrent
                                | return_statement_concurrent'''

def p_assignment_concurrent(p):
    '''assignment_concurrent    : VARIABLE ASSIGNATION expression DOTANDCOMMA'''

def p_if_statement_concurrent(p):
    '''if_statement_concurrent  : IF LPARENT condition RPARENT LKEY concurrent_block RKEY'''

def p_while_loop_concurrent(p):
    '''while_loop_concurrent    : WHILE LPARENT condition RPARENT LKEY concurrent_block RKEY'''

def p_method_call_concurrent(p):
    '''method_call_concurrent   : IDENTIFIER LPARENT RPARENT DOTANDCOMMA'''

def p_return_statement_concurrent(p):
    '''return_statement_concurrent : RETURN expression DOTANDCOMMA'''

def p_expression(p):
    '''expression               : value_numeric
                                | VARIABLE
                                | value_numeric arithmetic_operator expression
                                | VARIABLE arithmetic_operator expression
    '''

def p_condition(p):
    '''condition                : value_numeric logic_operator value_numeric
                                | VARIABLE logic_operator value_numeric
                                | value_numeric logic_operator VARIABLE
                                | VARIABLE logic_operator VARIABLE
    '''

#El metodo para imprimir en consola al ejecutar solo el archivo sintactico.py
'''
def p_error(p):
    if p:
         print("Error de sintaxis en token:", p.type)
         #sintactico.errok()
    else:
         print("Syntax error at EOF")
'''

p_error_message = None
def p_error(p):
    global p_error_message
    if p:
        p_error_message = "Error de sintaxis en token: " + str(p.type)
    else:
        p_error_message = "Syntax error at EOF"

# Build the parser
sintactico = yacc.yacc()



datos = '''
using System; 
public class clase1 { 
    const int var2 = 14 ; 
    var3 = var2 ; 
    const int var5 = 4 ;
    int var2 = 14 ; var3 = var2 ; 
    List<string> nombres = new List<string>(){"Adair"};
    nombres.Add("Eduardo"); 
    nombres.RemoveAt(0);
    try{  const int var5 = 4 ; } 
    catch (exception e){ dsadas } 
    finally { final }
    nombres.Clear(); 
    nombres.Cnt();
}
'''

print(datos)

def analizar_sintactico_string(content):
    result = sintactico.parse(content)
    #return result is not None
    if result!=None:
        print(result)
        return result

varresult = analizar_sintactico_string(datos)
