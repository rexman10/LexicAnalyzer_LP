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
                                | STATIC VOID MAIN LPARENT STRINGTYPE LBRACKET RBRACKET VARIABLE RPARENT LKEY all_block_code RKEY all_block_code
    '''

def p_block_code(p):
    '''block_code               : def_const_or_var
                                | print_data
                                | array_assignation
                                | array_value_assign
                                | array_indexing
                                | thread_main
                                | concurrent_method
                                | method_definition

                                | block_try_catch

                                | lists
                                | functions_list
                                
                                | statement_lambda

                                | enums
                                | normal_if

                                | block_for

                                | block_while

                                | stack_struct
                                | functions_stack

                                | queue_struct
                                | functions_queue

                                | dictionary_declaration
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
                                | array_type
                                | METHOD
    '''

# Valores disponibles

def p_value_string(p):
    '''value_string             : STRING
                                | CHAR
                                | VARIABLE
                                | concatenation
    '''

def p_value_boolean(p):
    '''value_boolean            : BOOLTRUE
                                | BOOLFALSE
                                | VARIABLE
                                | comparison_operation
                                | functions_queue
                                | array_indexing
                                | VARIABLE DOT ISEMPTY LPARENT RPARENT
    '''

def p_value_numeric(p):
    '''value_numeric            : INTEGER
                                | FLOAT_NUMBER
                                | DECIMAL_NUMBER
                                | VARIABLE
    '''

def p_print_data(p):
    '''print_data               : PRINT LPARENT value_string RPARENT DOTANDCOMMA
    '''

def p_read_data(p):
    '''read_data                : READ LPARENT RPARENT DOTANDCOMMA
    '''

def p_concatenation(p):
    '''concatenation            : STRING
                                | VARIABLE
                                | STRING PLUS concatenation
                                | VARIABLE PLUS concatenation
    '''

def p_array_type(p):
    '''array_type               : CHARTYPE LBRACKET RBRACKET
                                | STRINGTYPE LBRACKET RBRACKET
                                | FLOATTYPE LBRACKET RBRACKET
                                | DECIMALTYPE LBRACKET RBRACKET
                                | INTTYPE LBRACKET RBRACKET
                                | BOOLTYPE LBRACKET RBRACKET
    '''

def p_array_assignation(p):
    '''array_assignation        : CHARTYPE LBRACKET RBRACKET char_array_assignation DOTANDCOMMA
                                | STRINGTYPE LBRACKET RBRACKET string_array_assignation DOTANDCOMMA
                                | FLOATTYPE LBRACKET RBRACKET float_array_assignation DOTANDCOMMA
                                | DECIMALTYPE LBRACKET RBRACKET decimal_array_assignation DOTANDCOMMA
                                | INTTYPE LBRACKET RBRACKET int_array_assignation DOTANDCOMMA
                                | BOOLTYPE LBRACKET RBRACKET bool_array_assignation DOTANDCOMMA
    '''

def p_char_array_assignation(p):
    'char_array_assignation     : VARIABLE ASSIGNATION LBRACKET char_content_multiple RBRACKET'

def p_char_content_multiple(p):
    '''char_content_multiple    : CHAR
                                | CHAR COMMA char_content_multiple
    '''

def p_string_array_assignation(p):
    'string_array_assignation   : VARIABLE ASSIGNATION LBRACKET string_content_multiple RBRACKET'

def p_string_content_multiple(p):
    '''string_content_multiple  : STRING
                                | STRING COMMA string_content_multiple
    '''

def p_float_array_assignation(p):
    'float_array_assignation    : VARIABLE ASSIGNATION LBRACKET float_content_multiple RBRACKET'

def p_float_content_multiple(p):
    '''float_content_multiple   : FLOAT_NUMBER
                                | FLOAT_NUMBER COMMA float_content_multiple
    '''

def p_int_array_assignation(p):
    'int_array_assignation      : VARIABLE ASSIGNATION LBRACKET int_content_multiple RBRACKET'

def p_int_content_multiple(p):
    '''int_content_multiple     : INTEGER
                                | INTEGER COMMA int_content_multiple
    '''

def p_decimal_array_assignation(p):
    'decimal_array_assignation  : VARIABLE ASSIGNATION LBRACKET decimal_content_multiple RBRACKET'

def p_decimal_content_multiple(p):
    '''decimal_content_multiple : DECIMAL_NUMBER
                                | DECIMAL_NUMBER COMMA decimal_content_multiple
    '''

def p_bool_array_assignation(p):
    'bool_array_assignation     : VARIABLE ASSIGNATION LBRACKET bool_content_multiple RBRACKET'

def p_bool_content_multiple(p):
    '''bool_content_multiple    : BOOLTRUE
                                | BOOLFALSE
                                | BOOLTRUE COMMA bool_content_multiple
                                | BOOLFALSE COMMA bool_content_multiple
    '''

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

def p_value(p):
    '''value                    : value_numeric
                                | value_boolean
                                | value_string
                                | VARIABLE
                                | read_data
                                | array
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
    '''def_const_or_var         : constant_assignation
                                | variable_assignation
    '''

def p_constant_assignation(p):
    '''constant_assignation     : access_modifiers CONST assignation_type_value_multiple DOTANDCOMMA
                                | CONST assignation_type_value_multiple DOTANDCOMMA
    '''

def p_variable_assignation(p):
    '''variable_assignation     : access_modifiers assignation_type_value_multiple DOTANDCOMMA
                                | assignation_type_value_multiple DOTANDCOMMA
                                | VARIABLE ASSIGNATION functions_queue
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
    '''assignation_int          : VARIABLE ASSIGNATION INTEGER
                                | VARIABLE ASSIGNATION VARIABLE
                                | VARIABLE ASSIGNATION arithmetic_operation
    '''

def p_assignation_string(p):
    '''assignation_string       : VARIABLE ASSIGNATION STRING
                                | VARIABLE ASSIGNATION VARIABLE
    '''

def p_assignation_float(p):
    '''assignation_float        : VARIABLE ASSIGNATION FLOAT_NUMBER
                                | VARIABLE ASSIGNATION VARIABLE
                                | VARIABLE ASSIGNATION arithmetic_operation
    '''

def p_assignation_true(p):
    '''assignation_true         : VARIABLE ASSIGNATION BOOLTRUE
                                | VARIABLE ASSIGNATION VARIABLE
                                | VARIABLE ASSIGNATION boolean_operation
    '''

def p_assignation_false(p):
    '''assignation_false        : VARIABLE ASSIGNATION BOOLFALSE
                                | VARIABLE ASSIGNATION VARIABLE
                                | VARIABLE ASSIGNATION boolean_operation
    '''


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

# Definicion de metodos

def p_method_definition(p):
    '''method_definition        : access_modifiers STATIC data_type METHOD LPARENT func_parameters RPARENT LKEY all_block_code RETURN VARIABLE DOTANDCOMMA RKEY
                                | access_modifiers STATIC VOID METHOD LPARENT func_parameters RPARENT LKEY all_block_code RKEY
                                | STATIC data_type METHOD LPARENT func_parameters RPARENT LKEY all_block_code RETURN VARIABLE DOTANDCOMMA RKEY
                                | STATIC VOID METHOD LPARENT func_parameters RPARENT LKEY all_block_code RKEY

                                | access_modifiers STATIC data_type METHOD LPARENT RPARENT LKEY all_block_code RETURN VARIABLE DOTANDCOMMA RKEY
                                | access_modifiers STATIC VOID METHOD LPARENT RPARENT LKEY all_block_code RKEY
                                | STATIC data_type METHOD LPARENT RPARENT LKEY all_block_code RETURN VARIABLE DOTANDCOMMA RKEY
                                | STATIC VOID METHOD LPARENT RPARENT LKEY all_block_code RKEY

                                | data_type METHOD LPARENT func_parameters RPARENT LKEY block_code RETURN VARIABLE DOTANDCOMMA RKEY
    '''

def p_func_parameter(p):
    '''func_parameter           : data_type VARIABLE'''

def p_func_parameters(p):
    '''func_parameters          : func_parameter
                                | func_parameter COMMA func_parameters
    '''

#Inicio Metodos concurrentes
def p_thread_main(p):
    '''
    thread_main                 : declaration_thread declaration_thread thread_init thread_init thread_wait thread_wait
    '''

def p_declaration_thread(p):
    '''
    declaration_thread          : THREAD thread_identificator ASSIGNATION NEW THREAD LPARENT thread_identificator RPARENT DOTANDCOMMA
                                | THREAD thread_identificator ASSIGNATION NEW THREAD LPARENT concurrent_method RPARENT DOTANDCOMMA
    '''

def p_thread_init(p):
    '''
    thread_init                 : thread_identificator DOT START LPARENT RPARENT DOTANDCOMMA
    '''

def p_thread_wait(p):
    '''
    thread_wait                 : thread_identificator DOT JOIN LPARENT RPARENT DOTANDCOMMA
    '''

def p_concurrent_method(p):
    '''
    concurrent_method           : STATIC VOID thread_identificator LPARENT RPARENT LKEY thread_logic RKEY
                                | WRITE
    '''

def p_thread_logic(p):
    '''
    thread_logic                : thread_sentence
                                | thread_logic thread_sentence
    '''

def p_thread_sentence(p):
    '''
    thread_sentence             : thread_expression DOTANDCOMMA
    '''

def p_thread_expression(p):
    '''
    thread_expression           : thread_identificator DOT concurrent_method LPARENT RPARENT
                                | PRINT LPARENT STRING RPARENT
    '''

def p_thread_arguments(p):
    '''
    thread_arguments            : thread_expression
                                | thread_arguments COMMA thread_expression
    '''

def p_thread_identificator(p):
    '''
    thread_identificator        : VARIABLE
    '''
#Fin Metodos Concurrentes

#Declaración de funciones

def p_statement_lambda(p):
    'statement_lambda           : LPARENT VARIABLE ARROW LKEY all_block_code RKEY RPARENT'
    
#Tipos de datos
def p_enums(p):
    'enums                      : ENUM METHOD LKEY list_enums RKEY'

def p_list_enums(p):
    '''list_enums               : METHOD
                                | METHOD COMMA list_enums 
    '''

#Fin Metodos Concurrentes

#Estructuras de control 
    #sentencia try-catch 

def p_block_try_catch(p):
    '''block_try_catch          : try_catch_simply
                                | try_catch_finally
    '''

def p_try_catch_simply(p):
    'try_catch_simply           : TRY LKEY all_block_code_try RKEY CATCH LPARENT EXCEPTION ERROR RPARENT LKEY PRINT LPARENT ERROR RPARENT DOTANDCOMMA RKEY'
    
def p_try_catch_finally(p):
    'try_catch_finally          : TRY LKEY all_block_code_try RKEY CATCH LPARENT EXCEPTION ERROR RPARENT LKEY PRINT LPARENT ERROR RPARENT DOTANDCOMMA RKEY FINALLY LKEY all_block_code_try RKEY'

def p_block_code_try(p):
    '''block_code_try           : def_const_or_var
                                | print_data
    '''

def p_all_block_code_try(p):
    '''all_block_code_try       : block_code_try
                                | block_code_try all_block_code_try        
    '''

    #sentencia if 

def p_block_if(p):
    '''block_if                 : normal_if
                                | all_block_code
    '''
def p_normal_if(p):
    '''normal_if                : IF LPARENT boolean_operation RPARENT LKEY block_if RKEY other_if
                                | IF LPARENT boolean_operation RPARENT LKEY block_if RKEY 
    '''

def p_other_if(p):
    '''other_if                 : ELSE LKEY block_if RKEY
                                | ELSE_IF LPARENT boolean_operation RPARENT LKEY block_if RKEY other_if
    '''

    #fin sentencia if
    #sentencia while
def p_block_while(p):
    '''block_while              : normal_while
                                | do_while             
    '''

def p_normal_while(p):
    'normal_while               : WHILE LPARENT boolean_operation RPARENT LKEY all_block_code RKEY'

def p_do_while(p):
    'do_while                   : DO LKEY all_block_code RKEY WHILE LPARENT boolean_operation RPARENT'
    
    #fin sentencia while
    #sentencia for
def p_block_for(p):
    '''block_for                : for_simple
                                | for_each
    '''

def p_for_simple(p):
    '''for_simple               : FOR LPARENT INTTYPE assignation_int DOTANDCOMMA comparison_operation DOTANDCOMMA VARIABLE INCREMENT RPARENT LKEY all_block_code RKEY
                                | FOR LPARENT INTTYPE assignation_int DOTANDCOMMA comparison_operation DOTANDCOMMA VARIABLE DECREMENT RPARENT LKEY all_block_code RKEY

    '''

def p_for_each(p):
    '''for_each                 : FOREACH LPARENT data_type VARIABLE IN VARIABLE RPARENT LKEY all_block_code RKEY
    '''

    #fin sentencia for

#Estructuras de datos

    #Inicio listas 
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
    '''list_func_add            : VARIABLE DOT ADD LPARENT INTEGER RPARENT DOTANDCOMMA
                                | VARIABLE DOT ADD LPARENT STRING RPARENT DOTANDCOMMA
                                | VARIABLE DOT ADD LPARENT VARIABLE RPARENT DOTANDCOMMA
    '''
    

def p_list_func_removeat(p):
    '''list_func_removeat       : VARIABLE DOT REMOVEAT LPARENT INTEGER RPARENT DOTANDCOMMA
    '''

    #fin listas
    #Inicio pilas
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

    #fin pilas
    #inicio colas
def p_queue_struct(p):
    'queue_struct               : QUEUE SMALLER_THAN data_type GREATER_THAN VARIABLE ASSIGNATION NEW QUEUE SMALLER_THAN GREATER_THAN LPARENT RPARENT DOTANDCOMMA'

def p_functions_queue(p):
    '''functions_queue          : queue_enqueue
                                | queue_dequeue
                                | queue_clear
                                | queue_isEmpty
                                | queue_peek
    '''

def p_queue_enqueue(p):
    'queue_enqueue              : VARIABLE DOT ENQUEUE LPARENT value RPARENT DOTANDCOMMA'

def p_queue_dequeue(p):
    'queue_dequeue              : VARIABLE DOT DEQUEUE LPARENT RPARENT DOTANDCOMMA'

def p_queue_clear(p):
    'queue_clear                : VARIABLE DOT CLEAR LPARENT RPARENT DOTANDCOMMA'

def p_queue_peek(p):
    'queue_peek                 : VARIABLE DOT PEEK LPARENT RPARENT DOTANDCOMMA'

def p_queue_isEmpty(p):
    'queue_isEmpty              : VARIABLE DOT ISEMPTY LPARENT RPARENT DOTANDCOMMA'

    #fin colas

    #Inicio diccionarios

def p_dictionary_declaration(p):
    '''
    dictionary_declaration      : dictionary_string
                                | dictionary_integer
    '''

def p_dictionary_integer(p):
    '''
    dictionary_integer          : dictionary_integer_empty
                                | dictionary_integer_full
    '''

def p_dictionary_string(p):
    '''
    dictionary_string           : dictionary_string_empty
                                | dictionary_string_full
    '''

def p_dictionary_string_full(p):
    '''
    dictionary_string_full      : DICTIONARY SMALLER_THAN STRINGTYPE COMMA STRINGTYPE GREATER_THAN VARIABLE ASSIGNATION NEW DICTIONARY SMALLER_THAN STRINGTYPE COMMA STRINGTYPE GREATER_THAN LPARENT RPARENT LKEY dictionary_string_full_values RKEY DOTANDCOMMA
    '''

def p_dictionary_string_full_values(p):
    '''
    dictionary_string_full_values       : LKEY value_string COMMA value_string RKEY
                                        | LKEY value_string COMMA value_string RKEY COMMA dictionary_string_full_values
    '''

def p_dictionary_string_empty(p):
    '''
    dictionary_string_empty     : DICTIONARY SMALLER_THAN STRINGTYPE COMMA STRINGTYPE GREATER_THAN VARIABLE ASSIGNATION NEW DICTIONARY SMALLER_THAN STRINGTYPE COMMA STRINGTYPE GREATER_THAN LPARENT RPARENT DOTANDCOMMA dictionary_string_empty_methods
    '''

def p_dictionary_string_empty_methods(p):
    '''
    dictionary_string_empty_methods : dictionary_string_empty_add
                                    | dictionary_string_empty_add dictionary_string_empty_methods
                                    | dictionary_string_empty_remove
                                    | dictionary_string_empty_remove dictionary_string_empty_methods
    '''
def p_dictionary_string_empty_add(p):
    '''
    dictionary_string_empty_add     : VARIABLE DOT ADD LPARENT value_string COMMA value_string RPARENT DOTANDCOMMA
                                    | VARIABLE DOT ADD LPARENT value_string COMMA value_string RPARENT DOTANDCOMMA dictionary_string_empty_methods
    '''

def p_dictionary_string_empty_remove(p):
    '''
    dictionary_string_empty_remove  : VARIABLE DOT REMOVEDICT LPARENT value_string RPARENT DOTANDCOMMA
                                    | VARIABLE DOT REMOVEDICT LPARENT value_string RPARENT DOTANDCOMMA dictionary_string_empty_methods
    '''

def p_dictionary_integer_full(p):
    '''
    dictionary_integer_full      : DICTIONARY SMALLER_THAN INTTYPE COMMA INTTYPE GREATER_THAN VARIABLE ASSIGNATION NEW DICTIONARY SMALLER_THAN INTTYPE COMMA INTTYPE GREATER_THAN LPARENT RPARENT LKEY dictionary_integer_full_values RKEY DOTANDCOMMA
    '''

def p_dictionary_integer_full_values(p):
    '''
    dictionary_integer_full_values      : LKEY value_numeric COMMA value_numeric RKEY
                                        | LKEY value_numeric COMMA value_numeric RKEY COMMA dictionary_integer_full_values
    '''
def p_dictionary_integer_empty(p):
    '''
    dictionary_integer_empty        : DICTIONARY SMALLER_THAN INTTYPE COMMA INTTYPE GREATER_THAN VARIABLE ASSIGNATION NEW DICTIONARY SMALLER_THAN INTTYPE COMMA INTTYPE GREATER_THAN LPARENT RPARENT DOTANDCOMMA dictionary_integer_empty_methods
    '''


def p_dictionary_integer_empty_methods(p):
    '''
    dictionary_integer_empty_methods    : dictionary_integer_empty_add
                                        | dictionary_integer_empty_add dictionary_integer_empty_methods
                                        | dictionary_integer_empty_remove
                                        | dictionary_integer_empty_remove dictionary_integer_empty_methods

    '''
def p_dictionary_integer_empty_add(p):
    '''
    dictionary_integer_empty_add        : VARIABLE DOT ADD LPARENT INTEGER COMMA INTEGER RPARENT DOTANDCOMMA
                                        | VARIABLE DOT ADD LPARENT INTEGER COMMA INTEGER RPARENT DOTANDCOMMA dictionary_integer_empty_methods
    '''

def p_dictionary_integer_empty_remove(p):
    '''
    dictionary_integer_empty_remove     : VARIABLE DOT REMOVEDICT LPARENT value_numeric RPARENT DOTANDCOMMA
                                        | VARIABLE DOT REMOVEDICT LPARENT value_numeric RPARENT DOTANDCOMMA dictionary_integer_empty_methods
    '''
    # Fin diccionarios

'''
#Funcion ejecucion en sintactico2.py
def p_error(p):
    if p:
         print("Error de sintaxis en token:", p.type, "in: ", p.lexpos, p.value)
         sintactico.errok()
    else:
         print("Syntax error at EOF")
'''

#Inicio Funcion ejecucion en interfaz.py (Tambien devuelve salida por consola)
mensajes_error = []

def p_error(p):
    if p:
        error_message = "Error de sintaxis en el token: " + str(p.type) + ", línea: " + str(p.lineno)
        mensajes_error.append(error_message)
        #Comentar sntactico.errok()
        sintactico.errok()
    else:
        print("Syntax error at EOF")

def resetear_linea():
    global contenido_archivo
    contenido_archivo = None

def resetear_errores():
    global mensajes_error
    mensajes_error = []
#Fin Funcion ejecucion en interfaz.py (Tambien devuelve salida por consola)

# Build the parser
sintactico = yacc.yacc()

datos = '''
using System;
public class clase1 {
    static void Main (string[] args) {
        Dictionary<string, string> comunidadesCapitales = new Dictionary<string, string>()
        {
            {"Aragon", "Zaragoza"},
            {"Navarra", "Pamplona"}
        };
        Dictionary<string, string> dicc = new Dictionary<string, string>();
        dicc.Add("mirandma","Martin Miranda");
        dicc.Add("polizzia","Ariel Polizzi");
        dicc.Remove("polizzia");
        
        Dictionary<int, int> diccint = new Dictionary<int, int>();
        diccint.Add(5, 25);
        diccint.Add(8, 30);
        diccint.Add(12,38);
        diccint.Add(58,59);
        diccint.Remove(58);
    
        bool var1 = x >= 34 && x == 34;
        bool var2 = x <= 34 || x == 34;
        bool var3 = x > 34;
        bool var4 = x < 34 && x == 34 && x != 34;
        bool var5 = true;   
        bool var6 = false;
        int operacion1 = 123 / 123123 + 5345 * 123124 - 4365;
        int var = 4;
        string var2 = "6", var3 = "8";
        try{
            bool var5 = true;
        }catch(exception e){
            Console.WriteLine(e);
        }
        List<int> numeros = new List<int>(){4 , 5, 5, 6};    
        numeros.Clear(); 
        numeros.Count();
        numeros.Add(4);
        numeros.RemoveAt(0);
        (x => {
            int operacion1 = 123 / 123123 + 5345 * 123124 - 4365;
        })
        enum Season
        {
            Spring,
            Summer,
            Autumn,
            Winter
        }
        string var2 = "5", var3 = "8";   
        do{
            Queue<Integer> pila1 = new Queue<>();
            pila1.EnQueue(5);
            pila1.DeQueue();
            pila1.Clear();
            pila1.Peek();
            pila1.IsEmpty();
        }while(5>10 && 6==3 || false && holi || !false)    

        if (5>10 && 6==3 || false && holi || !false){
            bool var4 = x < 34 && x == 34 && x != 34;
            bool var5 = true;
            bool var6 = false;
            if (5>10 && 6==3 || false && holi || !false){
                bool var4 = x < 34 && x == 34 && x != 34;
                bool var5 = true; 
            }
        }else_if(5>10 && 6==3 || false && holi || !false){
            bool var4 = x < 34 && x == 34 && x != 34;
            bool var5 = true; 
        }else{
            bool var4 = x < 34 && x == 34 && x != 34;
            bool var5 = true;
            bool var6 = false;
            if (5>10 && 6==3 || false && holi || !false){
                bool var4 = x < 34 && x == 34 && x != 34;
                bool var5 = true;
                bool[] arreglo1 = [true, false];
                int[] arreglo1 = [12, 74];
                decimal[] arreglo1 = [12.25m, -74.141m];
                float[] arreglo1 = [12.17f, 74.20f];
                string[] arreglo1 = ["true", "false"];
                char[] arreglo1 = ['A', 'z', 'p', 'G'];
            }
        }

        for(int i=0;i<5;i++){
            bool var4 = x < 34 && x == 34 && x != 34;
            bool var5 = true;
            for(int i=0;i<5;i--){
                bool var4 = x < 34 && x == 34 && x != 34;
                bool var5 = true;
                foreach(int elementos in numeros){
                    bool var5 = true;
                }
            }
        }
    }
    char[] arreglo1 = ['A', 'z', 'p', 'G'];

    public static void Bfs(Graph graph, int v, bool[] discovered){
        Queue<Integer> queue = new Queue<>();
        discovered[v] = true;
        queue.EnQueue(v);
        while (!queue.IsEmpty()){
            v = queue.DeQueue();
            Console.WriteLine(v + " ");
            foreach(int u in adjList){
                if (!discovered[u]){
                    discovered[u] = true;
                    queue.EnQueue(u);
                }
            }
        }
    }
}
'''

#print(datos)

datos2 = '''
using System;
public class clase1 {
    static void Main (string[] args) {
        const int factor= 9;
        List<int> distancias = new List<int>(){22, 20, 21, 26}; 
        List<int> distanciascorregidas = new List<int>();
        foreach(int masa in masas){
            int dt = factor * distancias;
            distanciascorregidas.Add(dt);
            Console.WriteLine(dt);        
        }
        public static void CalculateVe(Graph graph, int v){
        Queue<Integer> tiempos = new Queue<>();
        discovered[v] = true;
        queue.EnQueue(v);
        while (!queue.IsEmpty()){
            v = queue.DeQueue();
            Console.WriteLine(v + " ");
            foreach(int u in adjList){
                if (!discovered[u]){
                    discovered[u] = true;
                    queue.EnQueue(u);
                }
            }
        }
    }

    }
}
'''

print(datos2)


'''
#Funcion ejecucion en sintactico2.py
def analizar_sintactico_sintactico(content):
    result = sintactico.parse(content)
    #return result is not None
    if result!=None:
        print(result)
        return result
var = analizar_sintactico_sintactico(datos)
'''


#Inicio Funcion ejecucion en interfaz.py (Tambien devuelve salida por consola)
def analizar_sintactico(contenido):
    result = sintactico.parse(contenido)
    #return result is not None
    if result!=None:
        return result

analizar_sintactico(datos)

if len(mensajes_error) > 0:
    for error in mensajes_error:
        print(error)
else:
    print("Análisis sintáctico exitoso")
#Inicio Funcion ejecucion en interfaz.py (Tambien devuelve salida por consola)
