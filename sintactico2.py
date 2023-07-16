import ply.yacc as yacc
from lexico import tokens

errores=[]


def p_program(p):
    'program                    : USING SYSTEM DOTANDCOMMA block_publicClass'

def p_block_publicClass(p):
    '''block_publicClass        : PUBLIC CLASS VARIABLE LKEY block_main_method RKEY
                                | STATIC VOID MAIN LPARENT STRINGTYPE LBRACKET RBRACKET VARIABLE RPARENT LKEY all_block_code RKEY all_block_code
    '''

def p_block_main_method(p):
    '''block_main_method        : STATIC VOID MAIN LPARENT STRINGTYPE LBRACKET RBRACKET VARIABLE RPARENT LKEY all_block_code RKEY
                                | STATIC VOID MAIN LPARENT STRINGTYPE LBRACKET RBRACKET VARIABLE RPARENT LKEY all_block_code RKEY all_block_code
    '''

def p_block_code(p):
    '''block_code               : def_const_or_var
                                | print_data
                                | thread_main
                                | concurrent_method

                                | block_try_catch
                                | lists
                                | functions_list
                                
                                | statement_lambda

                                | enums
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



#Incio estructuras de control
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




#Estructuras de datos
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
    '''
    

def p_list_func_removeat(p):
    '''list_func_removeat       : VARIABLE DOT REMOVEAT LPARENT INTEGER RPARENT DOTANDCOMMA
                                | VARIABLE DOT REMOVEAT LPARENT STRING RPARENT DOTANDCOMMA
    '''



#Declaración de funciones

def p_statement_lambda(p):
    'statement_lambda           : LPARENT VARIABLE ARROW LKEY all_block_code RKEY RPARENT'
    



#Tipos de datos
def p_enums(p):
    'enums                    : ENUM METHOD LKEY list_enums RKEY'

def p_list_enums(p):
    '''list_enums               : METHOD
                                | METHOD COMMA list_enums 
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


