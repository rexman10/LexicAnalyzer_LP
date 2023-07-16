
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACTION ADD ADDITION_ASSIGNMENT ARROW ASSIGNATION ASYNC AWAIT BACK_SLASH BOOLFALSE BOOLTRUE BOOLTYPE BREAK CATCH CHAR CHARTYPE CLASS CLEAR COMMA CONCURRENT CONST COUNT DECIMALTYPE DECIMAL_NUMBER DECREMENT DEQUEUE DICTIONARY DIVIDE DIVISION_ASSIGNMENT DO DOLLARSIGN DOT DOTANDCOMMA DOUBLEPOINT DOUBLE_QUOTATION_MARKS ELSE ELSE_IF ENQUEUE EQUAL_COMPARATION EXCEPTION FINALLY FLOATTYPE FLOAT_NUMBER FOR FOREACH GREATER_THAN GREATER_THAN_OR_EQUAL ID IDENTIFIER IF IN INCREMENT INEQUALITY INTEGER INTTYPE ISEMPTY JOIN JUMP_LINE LBRACKET LIST LKEY LOGICAND LOGICNOT LOGICOR LONG LPARENT MAIN METHOD MINUS MODULE_ASSIGNMENT MULTIPLICATION_ASSIGNMENT NAMESPACE NEW PEEK PERCENT PIPE PLUS POP PRINT PRIVATE PUBLIC PUSH PUT QUEUE RBRACKET READ REMOVE REMOVEAT RETURN RKEY RPARENT SIPLE_QUOTATION_MARKS SMALLER_THAN SMALLER_THAN_OR_EQUAL STACK START STATIC STRING STRINGTYPE SUBTRACTION_ASSIGNMENT SWITCH SYSTEM TABULATION TASK THREAD TIMES TRY USING VARIABLE VOID WHILE WRITEprogram                    : USING SYSTEM DOTANDCOMMA block_publicClassblock_publicClass        : PUBLIC CLASS VARIABLE LKEY block_main_method RKEY\n                                | STATIC VOID MAIN LPARENT STRINGTYPE LBRACKET RBRACKET VARIABLE RPARENT LKEY all_block_code RKEY all_block_code\n    block_main_method        : STATIC VOID MAIN LPARENT STRINGTYPE LBRACKET RBRACKET VARIABLE RPARENT LKEY all_block_code RKEY\n                                | STATIC VOID MAIN LPARENT STRINGTYPE LBRACKET RBRACKET VARIABLE RPARENT LKEY all_block_code RKEY all_block_code\n    block_code               : def_const_or_var\n                                | print_data\n                                | thread_main\n                                | concurrent_method\n    all_block_code           : block_code\n                                | block_code all_block_code        \n    data_type                : CHARTYPE\n                                | STRINGTYPE\n                                | FLOATTYPE\n                                | DECIMALTYPE\n                                | INTTYPE\n                                | BOOLTYPE\n    value_string             : STRING\n                                | CHAR\n                                | concatenation\n    value_boolean            : BOOLTRUE\n                                | BOOLFALSE\n                                | VARIABLE\n                                | comparison_operation\n    value_numeric            : INTEGER\n                                | FLOAT_NUMBER\n                                | DECIMAL_NUMBER\n                                | VARIABLE\n    print_data               : PRINT LPARENT STRING RPARENT DOTANDCOMMA\n                                | PRINT LPARENT VARIABLE RPARENT DOTANDCOMMA\n    read_data                : READ LPARENT RPARENT DOTANDCOMMA\n    concatenation            : STRING\n                                | STRING PLUS concatenation\n    value                    : value_numeric\n                                | value_boolean\n                                | value_string\n                                | VARIABLE\n                                | read_data\n    arithmetic_operation     : value_numeric\n                                | value_numeric arithmetic_operator arithmetic_operation\n    arithmetic_operator      : PLUS\n                                | MINUS\n                                | TIMES\n                                | DIVIDE\n                                | PERCENT\n    comparison_operation     : value_numeric\n                                | value_numeric comparison_operator comparison_operation\n    comparison_operator      : GREATER_THAN\n                                | SMALLER_THAN\n                                | EQUAL_COMPARATION\n                                | INEQUALITY\n                                | GREATER_THAN_OR_EQUAL\n                                | SMALLER_THAN_OR_EQUAL\n    boolean_operation        : value_boolean\n                                | LOGICNOT value_boolean\n                                | value_boolean boolean_operator boolean_operation\n    boolean_operator         : LOGICAND\n                                | LOGICOR\n    def_const_or_var         : constant_assignation\n                                | variable_assignation\n    constant_assignation     : access_modifiers CONST assignation_type_value_multiple DOTANDCOMMA\n                                | CONST assignation_type_value_multiple DOTANDCOMMA\n    variable_assignation     : access_modifiers assignation_type_value_multiple DOTANDCOMMA\n                                | assignation_type_value_multiple DOTANDCOMMA\n    access_modifiers         : PUBLIC\n                                | PRIVATE\n    assignation_type_value   : INTTYPE assignation_int\n                                | STRINGTYPE assignation_string\n                                | FLOATTYPE assignation_float\n                                | BOOLTYPE assignation_true\n                                | BOOLTYPE assignation_false\n    assignation_int          : VARIABLE ASSIGNATION INTEGER\n                                | VARIABLE ASSIGNATION VARIABLE\n                                | VARIABLE ASSIGNATION arithmetic_operation\n    assignation_string       : VARIABLE ASSIGNATION STRING\n                                | VARIABLE ASSIGNATION VARIABLE\n    assignation_float        : VARIABLE ASSIGNATION FLOAT_NUMBER\n                                | VARIABLE ASSIGNATION VARIABLE\n                                | VARIABLE ASSIGNATION arithmetic_operation\n    assignation_true         : VARIABLE ASSIGNATION BOOLTRUE\n                                | VARIABLE ASSIGNATION VARIABLE\n                                | VARIABLE ASSIGNATION boolean_operation\n    assignation_false        : VARIABLE ASSIGNATION BOOLFALSE\n                                | VARIABLE ASSIGNATION VARIABLE\n                                | VARIABLE ASSIGNATION boolean_operation\n    assignation_type_value_multiple          : INTTYPE assignation_int_multiple\n                                                | STRINGTYPE assignation_string_multiple\n                                                | FLOATTYPE assignation_float_multiple\n                                                | BOOLTYPE assignation_true_multiple\n                                                | BOOLTYPE assignation_false_multiple\n    assignation_int_multiple                 : assignation_int\n                                                | assignation_int COMMA assignation_int_multiple\n    assignation_string_multiple              : assignation_string\n                                                | assignation_string COMMA assignation_string_multiple\n    assignation_float_multiple               : assignation_float\n                                                | assignation_float COMMA assignation_float_multiple\n    assignation_true_multiple                : assignation_true\n                                                | assignation_true COMMA assignation_true_multiple\n    assignation_false_multiple               : assignation_false\n                                                | assignation_false COMMA assignation_false_multiple\n    \n    thread_main                 : declaration_thread declaration_thread thread_init thread_init thread_wait thread_wait\n    \n    declaration_thread          : THREAD thread_identificator ASSIGNATION NEW THREAD LPARENT thread_identificator RPARENT DOTANDCOMMA\n                                | THREAD thread_identificator ASSIGNATION NEW THREAD LPARENT concurrent_method RPARENT DOTANDCOMMA\n    \n    thread_init                 : thread_identificator DOT START LPARENT RPARENT DOTANDCOMMA\n    \n    thread_wait                 : thread_identificator DOT JOIN LPARENT RPARENT DOTANDCOMMA\n    \n    concurrent_method           : STATIC VOID thread_identificator LPARENT RPARENT LKEY thread_logic RKEY\n                                | WRITE\n    \n    thread_logic                : thread_sentence\n                                | thread_logic thread_sentence\n    \n    thread_sentence             : thread_expression DOTANDCOMMA\n    \n    thread_expression           : thread_identificator DOT concurrent_method LPARENT RPARENT\n                                | PRINT LPARENT STRING RPARENT\n    \n    thread_arguments            : thread_expression\n                                | thread_arguments COMMA thread_expression\n    \n    thread_identificator        : VARIABLE\n    '
    
_lr_action_items = {'USING':([0,],[2,]),'$end':([1,5,17,32,33,34,35,36,37,38,41,57,63,81,87,88,106,134,135,164,187,202,],[0,-1,-2,-10,-6,-7,-8,-9,-59,-60,-107,-11,-64,-3,-63,-62,-61,-29,-30,-101,-106,-105,]),'SYSTEM':([2,],[3,]),'DOTANDCOMMA':([3,44,53,54,61,62,66,67,69,70,72,73,74,75,86,99,100,101,102,103,108,109,110,111,112,113,114,115,116,117,118,119,120,122,124,125,126,127,128,130,131,151,152,153,154,168,169,170,171,172,173,174,175,180,183,193,194,197,201,203,],[4,63,-87,-93,87,88,-86,-91,-88,-95,-89,-90,-97,-99,106,-94,-76,-75,134,135,-92,-28,-25,-74,-39,-26,-27,-96,-28,-26,-79,-25,-98,-100,-23,-21,-82,-22,-54,-24,-46,-55,-21,-22,-23,-40,-28,-23,-82,-23,-85,-56,-47,189,192,198,199,202,-112,-111,]),'PUBLIC':([4,27,32,33,34,35,36,37,38,41,56,63,87,88,97,106,134,135,162,164,187,202,],[6,46,46,-6,-7,-8,-9,-59,-60,-107,46,-64,-63,-62,46,-61,-29,-30,46,-101,-106,-105,]),'STATIC':([4,12,27,32,33,34,35,36,37,38,41,56,63,87,88,97,106,134,135,162,164,167,186,187,202,],[7,15,29,29,-6,-7,-8,-9,-59,-60,-107,29,-64,-63,-62,29,-61,-29,-30,29,-101,29,29,-106,-105,]),'CLASS':([6,],[8,]),'VOID':([7,15,29,],[9,18,52,]),'VARIABLE':([8,21,28,30,45,48,49,50,52,58,59,79,80,84,90,91,92,93,94,95,96,104,129,136,140,141,142,143,144,145,146,147,148,149,150,155,156,157,158,159,160,161,163,167,178,179,188,189,192,198,199,202,],[10,23,51,55,65,68,71,76,65,83,65,55,100,65,68,109,71,116,121,123,124,65,154,65,169,-41,-42,-43,-44,-45,170,172,154,-57,-58,169,-48,-49,-50,-51,-52,-53,65,65,65,-108,-109,-110,-104,-102,-103,-105,]),'MAIN':([9,18,],[11,20,]),'LKEY':([10,25,77,133,],[12,27,97,163,]),'LPARENT':([11,20,39,41,65,78,138,139,181,182,187,195,],[13,22,58,-107,-115,98,166,167,190,191,-106,200,]),'STRINGTYPE':([13,22,27,32,33,34,35,36,37,38,41,42,43,46,47,56,60,63,87,88,97,106,134,135,162,164,187,202,],[16,24,30,30,-6,-7,-8,-9,-59,-60,-107,30,30,-65,-66,30,30,-64,-63,-62,30,-61,-29,-30,30,-101,-106,-105,]),'RKEY':([14,31,32,33,34,35,36,37,38,41,57,63,87,88,106,132,134,135,162,164,176,178,179,187,188,189,202,],[17,56,-10,-6,-7,-8,-9,-59,-60,-107,-11,-64,-63,-62,-61,162,-29,-30,-4,-101,-5,187,-108,-106,-109,-110,-105,]),'LBRACKET':([16,24,],[19,26,]),'RBRACKET':([19,26,],[21,28,]),'RPARENT':([23,41,51,65,82,83,98,166,184,185,187,191,196,200,],[25,-107,77,-115,102,103,133,183,193,194,-106,197,201,203,]),'PRINT':([27,32,33,34,35,36,37,38,41,56,63,87,88,97,106,134,135,162,163,164,178,179,187,188,189,202,],[39,39,-6,-7,-8,-9,-59,-60,-107,39,-64,-63,-62,39,-61,-29,-30,39,181,-101,181,-108,-106,-109,-110,-105,]),'WRITE':([27,32,33,34,35,36,37,38,41,56,63,87,88,97,106,134,135,162,164,167,186,187,202,],[41,41,-6,-7,-8,-9,-59,-60,-107,41,-64,-63,-62,41,-61,-29,-30,41,-101,41,41,-106,-105,]),'CONST':([27,32,33,34,35,36,37,38,41,42,46,47,56,63,87,88,97,106,134,135,162,164,187,202,],[43,43,-6,-7,-8,-9,-59,-60,-107,60,-65,-66,43,-64,-63,-62,43,-61,-29,-30,43,-101,-106,-105,]),'THREAD':([27,32,33,34,35,36,37,38,40,41,56,63,87,88,97,106,107,134,135,162,164,187,198,199,202,],[45,45,-6,-7,-8,-9,-59,-60,45,-107,45,-64,-63,-62,45,-61,139,-29,-30,45,-101,-106,-102,-103,-105,]),'PRIVATE':([27,32,33,34,35,36,37,38,41,56,63,87,88,97,106,134,135,162,164,187,202,],[47,47,-6,-7,-8,-9,-59,-60,-107,47,-64,-63,-62,47,-61,-29,-30,47,-101,-106,-105,]),'INTTYPE':([27,32,33,34,35,36,37,38,41,42,43,46,47,56,60,63,87,88,97,106,134,135,162,164,187,202,],[48,48,-6,-7,-8,-9,-59,-60,-107,48,48,-65,-66,48,48,-64,-63,-62,48,-61,-29,-30,48,-101,-106,-105,]),'FLOATTYPE':([27,32,33,34,35,36,37,38,41,42,43,46,47,56,60,63,87,88,97,106,134,135,162,164,187,202,],[49,49,-6,-7,-8,-9,-59,-60,-107,49,49,-65,-66,49,49,-64,-63,-62,49,-61,-29,-30,49,-101,-106,-105,]),'BOOLTYPE':([27,32,33,34,35,36,37,38,41,42,43,46,47,56,60,63,87,88,97,106,134,135,162,164,187,202,],[50,50,-6,-7,-8,-9,-59,-60,-107,50,50,-65,-66,50,50,-64,-63,-62,50,-61,-29,-30,50,-101,-106,-105,]),'COMMA':([54,67,70,74,75,100,101,109,110,111,112,113,114,116,117,118,119,124,125,126,127,128,130,131,151,152,153,154,168,169,170,171,172,173,174,175,],[79,90,92,94,95,-76,-75,-28,-25,-74,-39,-26,-27,-28,-26,-79,-25,-23,-21,-82,-22,-54,-24,-46,-55,-21,-22,-23,-40,-28,-23,-82,-23,-85,-56,-47,]),'ASSIGNATION':([55,64,65,68,71,76,121,123,],[80,89,-115,91,93,96,146,147,]),'STRING':([58,80,190,],[82,101,196,]),'DOT':([65,85,137,177,],[-115,105,165,186,]),'NEW':([89,],[107,]),'INTEGER':([91,93,96,129,140,141,142,143,144,145,146,147,148,149,150,155,156,157,158,159,160,161,],[110,119,119,119,119,-41,-42,-43,-44,-45,119,119,119,-57,-58,119,-48,-49,-50,-51,-52,-53,]),'FLOAT_NUMBER':([91,93,96,129,140,141,142,143,144,145,146,147,148,149,150,155,156,157,158,159,160,161,],[113,117,113,113,113,-41,-42,-43,-44,-45,113,113,113,-57,-58,113,-48,-49,-50,-51,-52,-53,]),'DECIMAL_NUMBER':([91,93,96,129,140,141,142,143,144,145,146,147,148,149,150,155,156,157,158,159,160,161,],[114,114,114,114,114,-41,-42,-43,-44,-45,114,114,114,-57,-58,114,-48,-49,-50,-51,-52,-53,]),'BOOLTRUE':([96,129,146,147,148,149,150,],[125,152,125,152,152,-57,-58,]),'BOOLFALSE':([96,129,146,147,148,149,150,],[127,153,153,127,153,-57,-58,]),'LOGICNOT':([96,146,147,148,149,150,],[129,129,129,129,-57,-58,]),'START':([105,],[138,]),'PLUS':([109,110,112,113,114,116,117,119,169,],[-28,-25,141,-26,-27,-28,-26,-25,-28,]),'MINUS':([109,110,112,113,114,116,117,119,169,],[-28,-25,142,-26,-27,-28,-26,-25,-28,]),'TIMES':([109,110,112,113,114,116,117,119,169,],[-28,-25,143,-26,-27,-28,-26,-25,-28,]),'DIVIDE':([109,110,112,113,114,116,117,119,169,],[-28,-25,144,-26,-27,-28,-26,-25,-28,]),'PERCENT':([109,110,112,113,114,116,117,119,169,],[-28,-25,145,-26,-27,-28,-26,-25,-28,]),'GREATER_THAN':([113,114,119,124,131,154,169,170,172,],[-26,-27,-25,-28,156,-28,-28,-28,-28,]),'SMALLER_THAN':([113,114,119,124,131,154,169,170,172,],[-26,-27,-25,-28,157,-28,-28,-28,-28,]),'EQUAL_COMPARATION':([113,114,119,124,131,154,169,170,172,],[-26,-27,-25,-28,158,-28,-28,-28,-28,]),'INEQUALITY':([113,114,119,124,131,154,169,170,172,],[-26,-27,-25,-28,159,-28,-28,-28,-28,]),'GREATER_THAN_OR_EQUAL':([113,114,119,124,131,154,169,170,172,],[-26,-27,-25,-28,160,-28,-28,-28,-28,]),'SMALLER_THAN_OR_EQUAL':([113,114,119,124,131,154,169,170,172,],[-26,-27,-25,-28,161,-28,-28,-28,-28,]),'LOGICAND':([113,114,119,124,125,127,128,130,131,152,153,154,169,170,172,175,],[-26,-27,-25,-23,-21,-22,149,-24,-46,-21,-22,-23,-28,-23,-23,-47,]),'LOGICOR':([113,114,119,124,125,127,128,130,131,152,153,154,169,170,172,175,],[-26,-27,-25,-23,-21,-22,150,-24,-46,-21,-22,-23,-28,-23,-23,-47,]),'JOIN':([165,],[182,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'block_publicClass':([4,],[5,]),'block_main_method':([12,],[14,]),'all_block_code':([27,32,56,97,162,],[31,57,81,132,176,]),'block_code':([27,32,56,97,162,],[32,32,32,32,32,]),'def_const_or_var':([27,32,56,97,162,],[33,33,33,33,33,]),'print_data':([27,32,56,97,162,],[34,34,34,34,34,]),'thread_main':([27,32,56,97,162,],[35,35,35,35,35,]),'concurrent_method':([27,32,56,97,162,167,186,],[36,36,36,36,36,185,195,]),'constant_assignation':([27,32,56,97,162,],[37,37,37,37,37,]),'variable_assignation':([27,32,56,97,162,],[38,38,38,38,38,]),'declaration_thread':([27,32,40,56,97,162,],[40,40,59,40,40,40,]),'access_modifiers':([27,32,56,97,162,],[42,42,42,42,42,]),'assignation_type_value_multiple':([27,32,42,43,56,60,97,162,],[44,44,61,62,44,86,44,44,]),'assignation_string_multiple':([30,79,],[53,99,]),'assignation_string':([30,79,],[54,54,]),'thread_identificator':([45,52,59,84,104,136,163,167,178,],[64,78,85,85,137,137,177,184,177,]),'assignation_int_multiple':([48,90,],[66,108,]),'assignation_int':([48,90,],[67,67,]),'assignation_float_multiple':([49,92,],[69,115,]),'assignation_float':([49,92,],[70,70,]),'assignation_true_multiple':([50,94,],[72,120,]),'assignation_false_multiple':([50,95,],[73,122,]),'assignation_true':([50,94,],[74,74,]),'assignation_false':([50,95,],[75,75,]),'thread_init':([59,84,],[84,104,]),'arithmetic_operation':([91,93,140,],[111,118,168,]),'value_numeric':([91,93,96,129,140,146,147,148,155,],[112,112,131,131,112,131,131,131,131,]),'boolean_operation':([96,146,147,148,],[126,171,173,174,]),'value_boolean':([96,129,146,147,148,],[128,151,128,128,128,]),'comparison_operation':([96,129,146,147,148,155,],[130,130,130,130,130,175,]),'thread_wait':([104,136,],[136,164,]),'arithmetic_operator':([112,],[140,]),'boolean_operator':([128,],[148,]),'comparison_operator':([131,],[155,]),'thread_logic':([163,],[178,]),'thread_sentence':([163,178,],[179,188,]),'thread_expression':([163,178,],[180,180,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> USING SYSTEM DOTANDCOMMA block_publicClass','program',4,'p_program','sintactico2.py',8),
  ('block_publicClass -> PUBLIC CLASS VARIABLE LKEY block_main_method RKEY','block_publicClass',6,'p_block_publicClass','sintactico2.py',11),
  ('block_publicClass -> STATIC VOID MAIN LPARENT STRINGTYPE LBRACKET RBRACKET VARIABLE RPARENT LKEY all_block_code RKEY all_block_code','block_publicClass',13,'p_block_publicClass','sintactico2.py',12),
  ('block_main_method -> STATIC VOID MAIN LPARENT STRINGTYPE LBRACKET RBRACKET VARIABLE RPARENT LKEY all_block_code RKEY','block_main_method',12,'p_block_main_method','sintactico2.py',16),
  ('block_main_method -> STATIC VOID MAIN LPARENT STRINGTYPE LBRACKET RBRACKET VARIABLE RPARENT LKEY all_block_code RKEY all_block_code','block_main_method',13,'p_block_main_method','sintactico2.py',17),
  ('block_code -> def_const_or_var','block_code',1,'p_block_code','sintactico2.py',21),
  ('block_code -> print_data','block_code',1,'p_block_code','sintactico2.py',22),
  ('block_code -> thread_main','block_code',1,'p_block_code','sintactico2.py',23),
  ('block_code -> concurrent_method','block_code',1,'p_block_code','sintactico2.py',24),
  ('all_block_code -> block_code','all_block_code',1,'p_all_block_code','sintactico2.py',28),
  ('all_block_code -> block_code all_block_code','all_block_code',2,'p_all_block_code','sintactico2.py',29),
  ('data_type -> CHARTYPE','data_type',1,'p_data_type','sintactico2.py',35),
  ('data_type -> STRINGTYPE','data_type',1,'p_data_type','sintactico2.py',36),
  ('data_type -> FLOATTYPE','data_type',1,'p_data_type','sintactico2.py',37),
  ('data_type -> DECIMALTYPE','data_type',1,'p_data_type','sintactico2.py',38),
  ('data_type -> INTTYPE','data_type',1,'p_data_type','sintactico2.py',39),
  ('data_type -> BOOLTYPE','data_type',1,'p_data_type','sintactico2.py',40),
  ('value_string -> STRING','value_string',1,'p_value_string','sintactico2.py',46),
  ('value_string -> CHAR','value_string',1,'p_value_string','sintactico2.py',47),
  ('value_string -> concatenation','value_string',1,'p_value_string','sintactico2.py',48),
  ('value_boolean -> BOOLTRUE','value_boolean',1,'p_value_boolean','sintactico2.py',52),
  ('value_boolean -> BOOLFALSE','value_boolean',1,'p_value_boolean','sintactico2.py',53),
  ('value_boolean -> VARIABLE','value_boolean',1,'p_value_boolean','sintactico2.py',54),
  ('value_boolean -> comparison_operation','value_boolean',1,'p_value_boolean','sintactico2.py',55),
  ('value_numeric -> INTEGER','value_numeric',1,'p_value_numeric','sintactico2.py',59),
  ('value_numeric -> FLOAT_NUMBER','value_numeric',1,'p_value_numeric','sintactico2.py',60),
  ('value_numeric -> DECIMAL_NUMBER','value_numeric',1,'p_value_numeric','sintactico2.py',61),
  ('value_numeric -> VARIABLE','value_numeric',1,'p_value_numeric','sintactico2.py',62),
  ('print_data -> PRINT LPARENT STRING RPARENT DOTANDCOMMA','print_data',5,'p_print_data','sintactico2.py',66),
  ('print_data -> PRINT LPARENT VARIABLE RPARENT DOTANDCOMMA','print_data',5,'p_print_data','sintactico2.py',67),
  ('read_data -> READ LPARENT RPARENT DOTANDCOMMA','read_data',4,'p_read_data','sintactico2.py',71),
  ('concatenation -> STRING','concatenation',1,'p_concatenation','sintactico2.py',75),
  ('concatenation -> STRING PLUS concatenation','concatenation',3,'p_concatenation','sintactico2.py',76),
  ('value -> value_numeric','value',1,'p_value','sintactico2.py',80),
  ('value -> value_boolean','value',1,'p_value','sintactico2.py',81),
  ('value -> value_string','value',1,'p_value','sintactico2.py',82),
  ('value -> VARIABLE','value',1,'p_value','sintactico2.py',83),
  ('value -> read_data','value',1,'p_value','sintactico2.py',84),
  ('arithmetic_operation -> value_numeric','arithmetic_operation',1,'p_arithmetic_operation','sintactico2.py',90),
  ('arithmetic_operation -> value_numeric arithmetic_operator arithmetic_operation','arithmetic_operation',3,'p_arithmetic_operation','sintactico2.py',91),
  ('arithmetic_operator -> PLUS','arithmetic_operator',1,'p_arithmetic_operator','sintactico2.py',95),
  ('arithmetic_operator -> MINUS','arithmetic_operator',1,'p_arithmetic_operator','sintactico2.py',96),
  ('arithmetic_operator -> TIMES','arithmetic_operator',1,'p_arithmetic_operator','sintactico2.py',97),
  ('arithmetic_operator -> DIVIDE','arithmetic_operator',1,'p_arithmetic_operator','sintactico2.py',98),
  ('arithmetic_operator -> PERCENT','arithmetic_operator',1,'p_arithmetic_operator','sintactico2.py',99),
  ('comparison_operation -> value_numeric','comparison_operation',1,'p_comparison_operation','sintactico2.py',103),
  ('comparison_operation -> value_numeric comparison_operator comparison_operation','comparison_operation',3,'p_comparison_operation','sintactico2.py',104),
  ('comparison_operator -> GREATER_THAN','comparison_operator',1,'p_comparison_operator','sintactico2.py',108),
  ('comparison_operator -> SMALLER_THAN','comparison_operator',1,'p_comparison_operator','sintactico2.py',109),
  ('comparison_operator -> EQUAL_COMPARATION','comparison_operator',1,'p_comparison_operator','sintactico2.py',110),
  ('comparison_operator -> INEQUALITY','comparison_operator',1,'p_comparison_operator','sintactico2.py',111),
  ('comparison_operator -> GREATER_THAN_OR_EQUAL','comparison_operator',1,'p_comparison_operator','sintactico2.py',112),
  ('comparison_operator -> SMALLER_THAN_OR_EQUAL','comparison_operator',1,'p_comparison_operator','sintactico2.py',113),
  ('boolean_operation -> value_boolean','boolean_operation',1,'p_boolean_operation','sintactico2.py',117),
  ('boolean_operation -> LOGICNOT value_boolean','boolean_operation',2,'p_boolean_operation','sintactico2.py',118),
  ('boolean_operation -> value_boolean boolean_operator boolean_operation','boolean_operation',3,'p_boolean_operation','sintactico2.py',119),
  ('boolean_operator -> LOGICAND','boolean_operator',1,'p_boolean_operator','sintactico2.py',123),
  ('boolean_operator -> LOGICOR','boolean_operator',1,'p_boolean_operator','sintactico2.py',124),
  ('def_const_or_var -> constant_assignation','def_const_or_var',1,'p_def_const_or_var','sintactico2.py',130),
  ('def_const_or_var -> variable_assignation','def_const_or_var',1,'p_def_const_or_var','sintactico2.py',131),
  ('constant_assignation -> access_modifiers CONST assignation_type_value_multiple DOTANDCOMMA','constant_assignation',4,'p_constant_assignation','sintactico2.py',135),
  ('constant_assignation -> CONST assignation_type_value_multiple DOTANDCOMMA','constant_assignation',3,'p_constant_assignation','sintactico2.py',136),
  ('variable_assignation -> access_modifiers assignation_type_value_multiple DOTANDCOMMA','variable_assignation',3,'p_variable_assignation','sintactico2.py',140),
  ('variable_assignation -> assignation_type_value_multiple DOTANDCOMMA','variable_assignation',2,'p_variable_assignation','sintactico2.py',141),
  ('access_modifiers -> PUBLIC','access_modifiers',1,'p_access_modifiers','sintactico2.py',145),
  ('access_modifiers -> PRIVATE','access_modifiers',1,'p_access_modifiers','sintactico2.py',146),
  ('assignation_type_value -> INTTYPE assignation_int','assignation_type_value',2,'p_assignation_type_value','sintactico2.py',150),
  ('assignation_type_value -> STRINGTYPE assignation_string','assignation_type_value',2,'p_assignation_type_value','sintactico2.py',151),
  ('assignation_type_value -> FLOATTYPE assignation_float','assignation_type_value',2,'p_assignation_type_value','sintactico2.py',152),
  ('assignation_type_value -> BOOLTYPE assignation_true','assignation_type_value',2,'p_assignation_type_value','sintactico2.py',153),
  ('assignation_type_value -> BOOLTYPE assignation_false','assignation_type_value',2,'p_assignation_type_value','sintactico2.py',154),
  ('assignation_int -> VARIABLE ASSIGNATION INTEGER','assignation_int',3,'p_assignation_int','sintactico2.py',158),
  ('assignation_int -> VARIABLE ASSIGNATION VARIABLE','assignation_int',3,'p_assignation_int','sintactico2.py',159),
  ('assignation_int -> VARIABLE ASSIGNATION arithmetic_operation','assignation_int',3,'p_assignation_int','sintactico2.py',160),
  ('assignation_string -> VARIABLE ASSIGNATION STRING','assignation_string',3,'p_assignation_string','sintactico2.py',164),
  ('assignation_string -> VARIABLE ASSIGNATION VARIABLE','assignation_string',3,'p_assignation_string','sintactico2.py',165),
  ('assignation_float -> VARIABLE ASSIGNATION FLOAT_NUMBER','assignation_float',3,'p_assignation_float','sintactico2.py',169),
  ('assignation_float -> VARIABLE ASSIGNATION VARIABLE','assignation_float',3,'p_assignation_float','sintactico2.py',170),
  ('assignation_float -> VARIABLE ASSIGNATION arithmetic_operation','assignation_float',3,'p_assignation_float','sintactico2.py',171),
  ('assignation_true -> VARIABLE ASSIGNATION BOOLTRUE','assignation_true',3,'p_assignation_true','sintactico2.py',175),
  ('assignation_true -> VARIABLE ASSIGNATION VARIABLE','assignation_true',3,'p_assignation_true','sintactico2.py',176),
  ('assignation_true -> VARIABLE ASSIGNATION boolean_operation','assignation_true',3,'p_assignation_true','sintactico2.py',177),
  ('assignation_false -> VARIABLE ASSIGNATION BOOLFALSE','assignation_false',3,'p_assignation_false','sintactico2.py',181),
  ('assignation_false -> VARIABLE ASSIGNATION VARIABLE','assignation_false',3,'p_assignation_false','sintactico2.py',182),
  ('assignation_false -> VARIABLE ASSIGNATION boolean_operation','assignation_false',3,'p_assignation_false','sintactico2.py',183),
  ('assignation_type_value_multiple -> INTTYPE assignation_int_multiple','assignation_type_value_multiple',2,'p_assignation_type_value_multiple','sintactico2.py',188),
  ('assignation_type_value_multiple -> STRINGTYPE assignation_string_multiple','assignation_type_value_multiple',2,'p_assignation_type_value_multiple','sintactico2.py',189),
  ('assignation_type_value_multiple -> FLOATTYPE assignation_float_multiple','assignation_type_value_multiple',2,'p_assignation_type_value_multiple','sintactico2.py',190),
  ('assignation_type_value_multiple -> BOOLTYPE assignation_true_multiple','assignation_type_value_multiple',2,'p_assignation_type_value_multiple','sintactico2.py',191),
  ('assignation_type_value_multiple -> BOOLTYPE assignation_false_multiple','assignation_type_value_multiple',2,'p_assignation_type_value_multiple','sintactico2.py',192),
  ('assignation_int_multiple -> assignation_int','assignation_int_multiple',1,'p_assignation_int_multiple','sintactico2.py',196),
  ('assignation_int_multiple -> assignation_int COMMA assignation_int_multiple','assignation_int_multiple',3,'p_assignation_int_multiple','sintactico2.py',197),
  ('assignation_string_multiple -> assignation_string','assignation_string_multiple',1,'p_assignation_string_multiple','sintactico2.py',201),
  ('assignation_string_multiple -> assignation_string COMMA assignation_string_multiple','assignation_string_multiple',3,'p_assignation_string_multiple','sintactico2.py',202),
  ('assignation_float_multiple -> assignation_float','assignation_float_multiple',1,'p_assignation_float_multiple','sintactico2.py',206),
  ('assignation_float_multiple -> assignation_float COMMA assignation_float_multiple','assignation_float_multiple',3,'p_assignation_float_multiple','sintactico2.py',207),
  ('assignation_true_multiple -> assignation_true','assignation_true_multiple',1,'p_assignation_true_multiple','sintactico2.py',211),
  ('assignation_true_multiple -> assignation_true COMMA assignation_true_multiple','assignation_true_multiple',3,'p_assignation_true_multiple','sintactico2.py',212),
  ('assignation_false_multiple -> assignation_false','assignation_false_multiple',1,'p_assignation_false_multiple','sintactico2.py',216),
  ('assignation_false_multiple -> assignation_false COMMA assignation_false_multiple','assignation_false_multiple',3,'p_assignation_false_multiple','sintactico2.py',217),
  ('thread_main -> declaration_thread declaration_thread thread_init thread_init thread_wait thread_wait','thread_main',6,'p_thread_main','sintactico2.py',223),
  ('declaration_thread -> THREAD thread_identificator ASSIGNATION NEW THREAD LPARENT thread_identificator RPARENT DOTANDCOMMA','declaration_thread',9,'p_declaration_thread','sintactico2.py',228),
  ('declaration_thread -> THREAD thread_identificator ASSIGNATION NEW THREAD LPARENT concurrent_method RPARENT DOTANDCOMMA','declaration_thread',9,'p_declaration_thread','sintactico2.py',229),
  ('thread_init -> thread_identificator DOT START LPARENT RPARENT DOTANDCOMMA','thread_init',6,'p_thread_init','sintactico2.py',234),
  ('thread_wait -> thread_identificator DOT JOIN LPARENT RPARENT DOTANDCOMMA','thread_wait',6,'p_thread_wait','sintactico2.py',239),
  ('concurrent_method -> STATIC VOID thread_identificator LPARENT RPARENT LKEY thread_logic RKEY','concurrent_method',8,'p_concurrent_method','sintactico2.py',244),
  ('concurrent_method -> WRITE','concurrent_method',1,'p_concurrent_method','sintactico2.py',245),
  ('thread_logic -> thread_sentence','thread_logic',1,'p_thread_logic','sintactico2.py',250),
  ('thread_logic -> thread_logic thread_sentence','thread_logic',2,'p_thread_logic','sintactico2.py',251),
  ('thread_sentence -> thread_expression DOTANDCOMMA','thread_sentence',2,'p_thread_sentence','sintactico2.py',256),
  ('thread_expression -> thread_identificator DOT concurrent_method LPARENT RPARENT','thread_expression',5,'p_thread_expression','sintactico2.py',261),
  ('thread_expression -> PRINT LPARENT STRING RPARENT','thread_expression',4,'p_thread_expression','sintactico2.py',262),
  ('thread_arguments -> thread_expression','thread_arguments',1,'p_thread_arguments','sintactico2.py',267),
  ('thread_arguments -> thread_arguments COMMA thread_expression','thread_arguments',3,'p_thread_arguments','sintactico2.py',268),
  ('thread_identificator -> VARIABLE','thread_identificator',1,'p_thread_identificator','sintactico2.py',273),
]
