def p_all_block_code(p):
    '''all_block_code   : block_code
                        | block_code all_block_code  
    '''

def p_block_code(p):
    '''block_code   : def_const_or_var
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












""" Declaración de funciones """
def p_declaration_async(p):
    '''declaration_async    : PUBLIC STATIC ASYNC TASK METHOD LPARENT RPARENT LKEY AWAIT TASK DOT METHOD LPARENT LPARENT RPARENT ARROW LKEY block_code RKEY RPARENT DOTANDCOMMA RKEY
    '''

def p_declration_lambda(p):
    "declaration_lambda : ACTION SMALLER_THAN STRINGTYPE GREATER_THAN VARIABLE ASSIGNATION VARIABLE ARROW LKEY block_code RKEY"
