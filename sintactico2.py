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
                                | normal_if
                                | block_while
                                | stack_struct
                                | functions_stack
                                | queue_struct
                                | functions_queue
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

#Estructuras de control 
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


#Estructuras de datos
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
    'queue_struct               : QUEUE VARIABLE ASSIGNATION NEW QUEUE LPARENT RPARENT DOTANDCOMMA'

def p_functions_queue(p):
    '''functions_queue          : queue_enqueue
                                | queue_dequeue
                                | queue_clear
                                | queue_isEmpty
                                | queue_peek
    '''

def p_queue_enqueue(p):
    'queue_enqueue            : VARIABLE DOT ENQUEUE LPARENT value RPARENT DOTANDCOMMA'

def p_queue_dequeue(p):
    'queue_dequeue            : VARIABLE DOT DEQUEUE LPARENT RPARENT DOTANDCOMMA'

def p_queue_clear(p):
    'queue_clear              : VARIABLE DOT CLEAR LPARENT RPARENT DOTANDCOMMA'

def p_queue_peek(p):
    'queue_peek               : VARIABLE DOT PEEK LPARENT RPARENT DOTANDCOMMA'

def p_queue_isEmpty(p):
    'queue_isEmpty            : VARIABLE DOT ISEMPTY LPARENT RPARENT DOTANDCOMMA'

    #fin colas

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
        do{
            Queue pila1 = new Queue ();
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
            }
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


