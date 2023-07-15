
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACTION ADD ADDITION_ASSIGNMENT ARROW ASSIGNATION ASYNC AWAIT BACK_SLASH BOOLFALSE BOOLTRUE BOOLTYPE BREAK CATCH CHAR CHARTYPE CLASS CLEAR COMMA CONCURRENT CONST COUNT DECIMALTYPE DECIMAL_NUMBER DECREMENT DEQUEUE DICTIONARY DIVIDE DIVISION_ASSIGNMENT DO DOLLARSIGN DOT DOTANDCOMMA DOUBLEPOINT DOUBLE_QUOTATION_MARKS ELSE ELSE_IF ENQUEUE EQUAL_COMPARATION EXCEPTION FINALLY FLOATTYPE FLOAT_NUMBER FOR FOREACH GREATER_THAN GREATER_THAN_OR_EQUAL ID IDENTIFIER IF IN INCREMENT INEQUALITY INTEGER INTTYPE ISEMPTY JUMP_LINE LBRACKET LIST LKEY LOGICAND LOGICNOT LOGICOR LONG LPARENT MAIN METHOD MINUS MODULE_ASSIGNMENT MULTIPLICATION_ASSIGNMENT NAMESPACE NEW PEEK PERCENT PIPE PLUS POP PRINT PRIVATE PUBLIC PUSH PUT QUEUE RBRACKET READ REMOVE REMOVEAT RETURN RKEY RPARENT SIPLE_QUOTATION_MARKS SMALLER_THAN SMALLER_THAN_OR_EQUAL STACK STATIC STRING STRINGTYPE SUBTRACTION_ASSIGNMENT SWITCH SYSTEM TABULATION TASK TIMES TRY USING VARIABLE VOID WHILEprogram                    : USING SYSTEM DOTANDCOMMA block_publicClassblock_publicClass        : PUBLIC CLASS VARIABLE LKEY block_main_method RKEY\n    block_main_method        : STATIC VOID MAIN LPARENT STRINGTYPE LBRACKET RBRACKET VARIABLE RPARENT LKEY all_block_code RKEY\n    block_code               : def_const_or_var\n                                | print_data\n    all_block_code           : block_code\n                                | block_code all_block_code        \n    data_type                : CHARTYPE\n                                | STRINGTYPE\n                                | FLOATTYPE\n                                | DECIMALTYPE\n                                | INTTYPE\n                                | BOOLTYPE\n    value_string             : STRING\n                                | CHAR\n                                | concatenation\n    value_boolean            : BOOLTRUE\n                                | BOOLFALSE\n                                | VARIABLE\n                                | comparison_operation\n    value_numeric            : INTEGER\n                                | FLOAT_NUMBER\n                                | DECIMAL_NUMBER\n                                | VARIABLE\n    print_data               : PRINT LPARENT STRING RPARENT DOTANDCOMMA\n                                | PRINT LPARENT VARIABLE RPARENT DOTANDCOMMA\n    read_data                : READ LPARENT RPARENT DOTANDCOMMA\n    concatenation            : STRING\n                                | STRING PLUS concatenation\n    value                    : value_numeric\n                                | value_boolean\n                                | value_string\n                                | VARIABLE\n                                | read_data\n    arithmetic_operation     : value_numeric\n                                | value_numeric arithmetic_operator arithmetic_operation\n    arithmetic_operator      : PLUS\n                                | MINUS\n                                | TIMES\n                                | DIVIDE\n                                | PERCENT\n    comparison_operation     : value_numeric\n                                | value_numeric comparison_operator comparison_operation\n    comparison_operator      : GREATER_THAN\n                                | SMALLER_THAN\n                                | EQUAL_COMPARATION\n                                | INEQUALITY\n                                | GREATER_THAN_OR_EQUAL\n                                | SMALLER_THAN_OR_EQUAL\n    boolean_operation        : value_boolean\n                                | LOGICNOT value_boolean\n                                | value_boolean boolean_operator boolean_operation\n    boolean_operator         : LOGICAND\n                                | LOGICOR\n    def_const_or_var         : constant_assignation\n                                | variable_assignation\n    constant_assignation     : access_modifiers CONST assignation_type_value_multiple DOTANDCOMMA\n                                | CONST assignation_type_value_multiple DOTANDCOMMA\n    variable_assignation     : access_modifiers assignation_type_value_multiple DOTANDCOMMA\n                                | assignation_type_value_multiple DOTANDCOMMA\n    access_modifiers         : PUBLIC\n                                | PRIVATE\n    assignation_type_value   : INTTYPE assignation_int\n                                | STRINGTYPE assignation_string\n                                | FLOATTYPE assignation_float\n                                | BOOLTYPE assignation_true\n                                | BOOLTYPE assignation_false\n    assignation_int          : VARIABLE ASSIGNATION INTEGER\n                                | VARIABLE ASSIGNATION VARIABLE\n                                | VARIABLE ASSIGNATION arithmetic_operation\n    assignation_string       : VARIABLE ASSIGNATION STRING\n                                | VARIABLE ASSIGNATION VARIABLE\n    assignation_float        : VARIABLE ASSIGNATION FLOAT_NUMBER\n                                | VARIABLE ASSIGNATION VARIABLE\n                                | VARIABLE ASSIGNATION arithmetic_operation\n    assignation_true         : VARIABLE ASSIGNATION BOOLTRUE\n                                | VARIABLE ASSIGNATION VARIABLE\n                                | VARIABLE ASSIGNATION boolean_operation\n    assignation_false        : VARIABLE ASSIGNATION BOOLFALSE\n                                | VARIABLE ASSIGNATION VARIABLE\n                                | VARIABLE ASSIGNATION boolean_operation\n    assignation_type_value_multiple          : INTTYPE assignation_int_multiple\n                                                | STRINGTYPE assignation_string_multiple\n                                                | FLOATTYPE assignation_float_multiple\n                                                | BOOLTYPE assignation_true_multiple\n                                                | BOOLTYPE assignation_false_multiple\n    assignation_int_multiple                 : assignation_int\n                                                | assignation_int COMMA assignation_int_multiple\n    assignation_string_multiple              : assignation_string\n                                                | assignation_string COMMA assignation_string_multiple\n    assignation_float_multiple               : assignation_float\n                                                | assignation_float COMMA assignation_float_multiple\n    assignation_true_multiple                : assignation_true\n                                                | assignation_true COMMA assignation_true_multiple\n    assignation_false_multiple               : assignation_false\n                                                | assignation_false COMMA assignation_false_multiple\n    '
    
_lr_action_items = {'USING':([0,],[2,]),'$end':([1,5,12,],[0,-1,-2,]),'SYSTEM':([2,],[3,]),'DOTANDCOMMA':([3,32,38,39,45,46,48,49,51,52,54,55,56,57,63,73,74,75,76,77,79,80,81,82,83,84,85,86,87,88,89,90,91,93,95,96,97,98,99,101,102,116,117,118,119,127,128,129,130,131,132,133,134,],[4,47,-83,-89,64,65,-82,-87,-84,-91,-85,-86,-93,-95,78,-90,-72,-71,103,104,-88,-24,-21,-70,-35,-22,-23,-92,-24,-22,-75,-21,-94,-96,-19,-17,-78,-18,-50,-20,-42,-51,-17,-18,-19,-36,-24,-19,-78,-19,-81,-52,-43,]),'PUBLIC':([4,21,24,25,26,27,28,47,64,65,78,103,104,],[6,33,33,-4,-5,-55,-56,-60,-59,-58,-57,-25,-26,]),'CLASS':([6,],[7,]),'VARIABLE':([7,18,22,35,36,37,43,59,60,66,67,68,69,70,71,72,100,105,106,107,108,109,110,111,112,113,114,115,120,121,122,123,124,125,126,],[8,19,40,50,53,58,62,40,74,50,80,53,87,92,94,95,119,128,-37,-38,-39,-40,-41,129,131,119,-53,-54,128,-44,-45,-46,-47,-48,-49,]),'LKEY':([8,20,],[9,21,]),'STATIC':([9,],[11,]),'RKEY':([10,23,24,25,26,27,28,41,42,47,64,65,78,103,104,],[12,41,-6,-4,-5,-55,-56,-3,-7,-60,-59,-58,-57,-25,-26,]),'VOID':([11,],[13,]),'MAIN':([13,],[14,]),'LPARENT':([14,29,],[15,43,]),'STRINGTYPE':([15,21,24,25,26,27,28,30,31,33,34,44,47,64,65,78,103,104,],[16,22,22,-4,-5,-55,-56,22,22,-61,-62,22,-60,-59,-58,-57,-25,-26,]),'LBRACKET':([16,],[17,]),'RBRACKET':([17,],[18,]),'RPARENT':([19,61,62,],[20,76,77,]),'PRINT':([21,24,25,26,27,28,47,64,65,78,103,104,],[29,29,-4,-5,-55,-56,-60,-59,-58,-57,-25,-26,]),'CONST':([21,24,25,26,27,28,30,33,34,47,64,65,78,103,104,],[31,31,-4,-5,-55,-56,44,-61,-62,-60,-59,-58,-57,-25,-26,]),'PRIVATE':([21,24,25,26,27,28,47,64,65,78,103,104,],[34,34,-4,-5,-55,-56,-60,-59,-58,-57,-25,-26,]),'INTTYPE':([21,24,25,26,27,28,30,31,33,34,44,47,64,65,78,103,104,],[35,35,-4,-5,-55,-56,35,35,-61,-62,35,-60,-59,-58,-57,-25,-26,]),'FLOATTYPE':([21,24,25,26,27,28,30,31,33,34,44,47,64,65,78,103,104,],[36,36,-4,-5,-55,-56,36,36,-61,-62,36,-60,-59,-58,-57,-25,-26,]),'BOOLTYPE':([21,24,25,26,27,28,30,31,33,34,44,47,64,65,78,103,104,],[37,37,-4,-5,-55,-56,37,37,-61,-62,37,-60,-59,-58,-57,-25,-26,]),'COMMA':([39,49,52,56,57,74,75,80,81,82,83,84,85,87,88,89,90,95,96,97,98,99,101,102,116,117,118,119,127,128,129,130,131,132,133,134,],[59,66,68,70,71,-72,-71,-24,-21,-70,-35,-22,-23,-24,-22,-75,-21,-19,-17,-78,-18,-50,-20,-42,-51,-17,-18,-19,-36,-24,-19,-78,-19,-81,-52,-43,]),'ASSIGNATION':([40,50,53,58,92,94,],[60,67,69,72,111,112,]),'STRING':([43,60,],[61,75,]),'INTEGER':([67,69,72,100,105,106,107,108,109,110,111,112,113,114,115,120,121,122,123,124,125,126,],[81,90,90,90,90,-37,-38,-39,-40,-41,90,90,90,-53,-54,90,-44,-45,-46,-47,-48,-49,]),'FLOAT_NUMBER':([67,69,72,100,105,106,107,108,109,110,111,112,113,114,115,120,121,122,123,124,125,126,],[84,88,84,84,84,-37,-38,-39,-40,-41,84,84,84,-53,-54,84,-44,-45,-46,-47,-48,-49,]),'DECIMAL_NUMBER':([67,69,72,100,105,106,107,108,109,110,111,112,113,114,115,120,121,122,123,124,125,126,],[85,85,85,85,85,-37,-38,-39,-40,-41,85,85,85,-53,-54,85,-44,-45,-46,-47,-48,-49,]),'BOOLTRUE':([72,100,111,112,113,114,115,],[96,117,96,117,117,-53,-54,]),'BOOLFALSE':([72,100,111,112,113,114,115,],[98,118,118,98,118,-53,-54,]),'LOGICNOT':([72,111,112,113,114,115,],[100,100,100,100,-53,-54,]),'PLUS':([80,81,83,84,85,87,88,90,128,],[-24,-21,106,-22,-23,-24,-22,-21,-24,]),'MINUS':([80,81,83,84,85,87,88,90,128,],[-24,-21,107,-22,-23,-24,-22,-21,-24,]),'TIMES':([80,81,83,84,85,87,88,90,128,],[-24,-21,108,-22,-23,-24,-22,-21,-24,]),'DIVIDE':([80,81,83,84,85,87,88,90,128,],[-24,-21,109,-22,-23,-24,-22,-21,-24,]),'PERCENT':([80,81,83,84,85,87,88,90,128,],[-24,-21,110,-22,-23,-24,-22,-21,-24,]),'GREATER_THAN':([84,85,90,95,102,119,128,129,131,],[-22,-23,-21,-24,121,-24,-24,-24,-24,]),'SMALLER_THAN':([84,85,90,95,102,119,128,129,131,],[-22,-23,-21,-24,122,-24,-24,-24,-24,]),'EQUAL_COMPARATION':([84,85,90,95,102,119,128,129,131,],[-22,-23,-21,-24,123,-24,-24,-24,-24,]),'INEQUALITY':([84,85,90,95,102,119,128,129,131,],[-22,-23,-21,-24,124,-24,-24,-24,-24,]),'GREATER_THAN_OR_EQUAL':([84,85,90,95,102,119,128,129,131,],[-22,-23,-21,-24,125,-24,-24,-24,-24,]),'SMALLER_THAN_OR_EQUAL':([84,85,90,95,102,119,128,129,131,],[-22,-23,-21,-24,126,-24,-24,-24,-24,]),'LOGICAND':([84,85,90,95,96,98,99,101,102,117,118,119,128,129,131,134,],[-22,-23,-21,-19,-17,-18,114,-20,-42,-17,-18,-19,-24,-19,-19,-43,]),'LOGICOR':([84,85,90,95,96,98,99,101,102,117,118,119,128,129,131,134,],[-22,-23,-21,-19,-17,-18,115,-20,-42,-17,-18,-19,-24,-19,-19,-43,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'block_publicClass':([4,],[5,]),'block_main_method':([9,],[10,]),'all_block_code':([21,24,],[23,42,]),'block_code':([21,24,],[24,24,]),'def_const_or_var':([21,24,],[25,25,]),'print_data':([21,24,],[26,26,]),'constant_assignation':([21,24,],[27,27,]),'variable_assignation':([21,24,],[28,28,]),'access_modifiers':([21,24,],[30,30,]),'assignation_type_value_multiple':([21,24,30,31,44,],[32,32,45,46,63,]),'assignation_string_multiple':([22,59,],[38,73,]),'assignation_string':([22,59,],[39,39,]),'assignation_int_multiple':([35,66,],[48,79,]),'assignation_int':([35,66,],[49,49,]),'assignation_float_multiple':([36,68,],[51,86,]),'assignation_float':([36,68,],[52,52,]),'assignation_true_multiple':([37,70,],[54,91,]),'assignation_false_multiple':([37,71,],[55,93,]),'assignation_true':([37,70,],[56,56,]),'assignation_false':([37,71,],[57,57,]),'arithmetic_operation':([67,69,105,],[82,89,127,]),'value_numeric':([67,69,72,100,105,111,112,113,120,],[83,83,102,102,83,102,102,102,102,]),'boolean_operation':([72,111,112,113,],[97,130,132,133,]),'value_boolean':([72,100,111,112,113,],[99,116,99,99,99,]),'comparison_operation':([72,100,111,112,113,120,],[101,101,101,101,101,134,]),'arithmetic_operator':([83,],[105,]),'boolean_operator':([99,],[113,]),'comparison_operator':([102,],[120,]),}

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
  ('block_main_method -> STATIC VOID MAIN LPARENT STRINGTYPE LBRACKET RBRACKET VARIABLE RPARENT LKEY all_block_code RKEY','block_main_method',12,'p_block_main_method','sintactico2.py',15),
  ('block_code -> def_const_or_var','block_code',1,'p_block_code','sintactico2.py',19),
  ('block_code -> print_data','block_code',1,'p_block_code','sintactico2.py',20),
  ('all_block_code -> block_code','all_block_code',1,'p_all_block_code','sintactico2.py',24),
  ('all_block_code -> block_code all_block_code','all_block_code',2,'p_all_block_code','sintactico2.py',25),
  ('data_type -> CHARTYPE','data_type',1,'p_data_type','sintactico2.py',31),
  ('data_type -> STRINGTYPE','data_type',1,'p_data_type','sintactico2.py',32),
  ('data_type -> FLOATTYPE','data_type',1,'p_data_type','sintactico2.py',33),
  ('data_type -> DECIMALTYPE','data_type',1,'p_data_type','sintactico2.py',34),
  ('data_type -> INTTYPE','data_type',1,'p_data_type','sintactico2.py',35),
  ('data_type -> BOOLTYPE','data_type',1,'p_data_type','sintactico2.py',36),
  ('value_string -> STRING','value_string',1,'p_value_string','sintactico2.py',42),
  ('value_string -> CHAR','value_string',1,'p_value_string','sintactico2.py',43),
  ('value_string -> concatenation','value_string',1,'p_value_string','sintactico2.py',44),
  ('value_boolean -> BOOLTRUE','value_boolean',1,'p_value_boolean','sintactico2.py',48),
  ('value_boolean -> BOOLFALSE','value_boolean',1,'p_value_boolean','sintactico2.py',49),
  ('value_boolean -> VARIABLE','value_boolean',1,'p_value_boolean','sintactico2.py',50),
  ('value_boolean -> comparison_operation','value_boolean',1,'p_value_boolean','sintactico2.py',51),
  ('value_numeric -> INTEGER','value_numeric',1,'p_value_numeric','sintactico2.py',55),
  ('value_numeric -> FLOAT_NUMBER','value_numeric',1,'p_value_numeric','sintactico2.py',56),
  ('value_numeric -> DECIMAL_NUMBER','value_numeric',1,'p_value_numeric','sintactico2.py',57),
  ('value_numeric -> VARIABLE','value_numeric',1,'p_value_numeric','sintactico2.py',58),
  ('print_data -> PRINT LPARENT STRING RPARENT DOTANDCOMMA','print_data',5,'p_print_data','sintactico2.py',62),
  ('print_data -> PRINT LPARENT VARIABLE RPARENT DOTANDCOMMA','print_data',5,'p_print_data','sintactico2.py',63),
  ('read_data -> READ LPARENT RPARENT DOTANDCOMMA','read_data',4,'p_read_data','sintactico2.py',67),
  ('concatenation -> STRING','concatenation',1,'p_concatenation','sintactico2.py',71),
  ('concatenation -> STRING PLUS concatenation','concatenation',3,'p_concatenation','sintactico2.py',72),
  ('value -> value_numeric','value',1,'p_value','sintactico2.py',76),
  ('value -> value_boolean','value',1,'p_value','sintactico2.py',77),
  ('value -> value_string','value',1,'p_value','sintactico2.py',78),
  ('value -> VARIABLE','value',1,'p_value','sintactico2.py',79),
  ('value -> read_data','value',1,'p_value','sintactico2.py',80),
  ('arithmetic_operation -> value_numeric','arithmetic_operation',1,'p_arithmetic_operation','sintactico2.py',86),
  ('arithmetic_operation -> value_numeric arithmetic_operator arithmetic_operation','arithmetic_operation',3,'p_arithmetic_operation','sintactico2.py',87),
  ('arithmetic_operator -> PLUS','arithmetic_operator',1,'p_arithmetic_operator','sintactico2.py',91),
  ('arithmetic_operator -> MINUS','arithmetic_operator',1,'p_arithmetic_operator','sintactico2.py',92),
  ('arithmetic_operator -> TIMES','arithmetic_operator',1,'p_arithmetic_operator','sintactico2.py',93),
  ('arithmetic_operator -> DIVIDE','arithmetic_operator',1,'p_arithmetic_operator','sintactico2.py',94),
  ('arithmetic_operator -> PERCENT','arithmetic_operator',1,'p_arithmetic_operator','sintactico2.py',95),
  ('comparison_operation -> value_numeric','comparison_operation',1,'p_comparison_operation','sintactico2.py',99),
  ('comparison_operation -> value_numeric comparison_operator comparison_operation','comparison_operation',3,'p_comparison_operation','sintactico2.py',100),
  ('comparison_operator -> GREATER_THAN','comparison_operator',1,'p_comparison_operator','sintactico2.py',104),
  ('comparison_operator -> SMALLER_THAN','comparison_operator',1,'p_comparison_operator','sintactico2.py',105),
  ('comparison_operator -> EQUAL_COMPARATION','comparison_operator',1,'p_comparison_operator','sintactico2.py',106),
  ('comparison_operator -> INEQUALITY','comparison_operator',1,'p_comparison_operator','sintactico2.py',107),
  ('comparison_operator -> GREATER_THAN_OR_EQUAL','comparison_operator',1,'p_comparison_operator','sintactico2.py',108),
  ('comparison_operator -> SMALLER_THAN_OR_EQUAL','comparison_operator',1,'p_comparison_operator','sintactico2.py',109),
  ('boolean_operation -> value_boolean','boolean_operation',1,'p_boolean_operation','sintactico2.py',113),
  ('boolean_operation -> LOGICNOT value_boolean','boolean_operation',2,'p_boolean_operation','sintactico2.py',114),
  ('boolean_operation -> value_boolean boolean_operator boolean_operation','boolean_operation',3,'p_boolean_operation','sintactico2.py',115),
  ('boolean_operator -> LOGICAND','boolean_operator',1,'p_boolean_operator','sintactico2.py',119),
  ('boolean_operator -> LOGICOR','boolean_operator',1,'p_boolean_operator','sintactico2.py',120),
  ('def_const_or_var -> constant_assignation','def_const_or_var',1,'p_def_const_or_var','sintactico2.py',126),
  ('def_const_or_var -> variable_assignation','def_const_or_var',1,'p_def_const_or_var','sintactico2.py',127),
  ('constant_assignation -> access_modifiers CONST assignation_type_value_multiple DOTANDCOMMA','constant_assignation',4,'p_constant_assignation','sintactico2.py',131),
  ('constant_assignation -> CONST assignation_type_value_multiple DOTANDCOMMA','constant_assignation',3,'p_constant_assignation','sintactico2.py',132),
  ('variable_assignation -> access_modifiers assignation_type_value_multiple DOTANDCOMMA','variable_assignation',3,'p_variable_assignation','sintactico2.py',136),
  ('variable_assignation -> assignation_type_value_multiple DOTANDCOMMA','variable_assignation',2,'p_variable_assignation','sintactico2.py',137),
  ('access_modifiers -> PUBLIC','access_modifiers',1,'p_access_modifiers','sintactico2.py',141),
  ('access_modifiers -> PRIVATE','access_modifiers',1,'p_access_modifiers','sintactico2.py',142),
  ('assignation_type_value -> INTTYPE assignation_int','assignation_type_value',2,'p_assignation_type_value','sintactico2.py',146),
  ('assignation_type_value -> STRINGTYPE assignation_string','assignation_type_value',2,'p_assignation_type_value','sintactico2.py',147),
  ('assignation_type_value -> FLOATTYPE assignation_float','assignation_type_value',2,'p_assignation_type_value','sintactico2.py',148),
  ('assignation_type_value -> BOOLTYPE assignation_true','assignation_type_value',2,'p_assignation_type_value','sintactico2.py',149),
  ('assignation_type_value -> BOOLTYPE assignation_false','assignation_type_value',2,'p_assignation_type_value','sintactico2.py',150),
  ('assignation_int -> VARIABLE ASSIGNATION INTEGER','assignation_int',3,'p_assignation_int','sintactico2.py',154),
  ('assignation_int -> VARIABLE ASSIGNATION VARIABLE','assignation_int',3,'p_assignation_int','sintactico2.py',155),
  ('assignation_int -> VARIABLE ASSIGNATION arithmetic_operation','assignation_int',3,'p_assignation_int','sintactico2.py',156),
  ('assignation_string -> VARIABLE ASSIGNATION STRING','assignation_string',3,'p_assignation_string','sintactico2.py',160),
  ('assignation_string -> VARIABLE ASSIGNATION VARIABLE','assignation_string',3,'p_assignation_string','sintactico2.py',161),
  ('assignation_float -> VARIABLE ASSIGNATION FLOAT_NUMBER','assignation_float',3,'p_assignation_float','sintactico2.py',165),
  ('assignation_float -> VARIABLE ASSIGNATION VARIABLE','assignation_float',3,'p_assignation_float','sintactico2.py',166),
  ('assignation_float -> VARIABLE ASSIGNATION arithmetic_operation','assignation_float',3,'p_assignation_float','sintactico2.py',167),
  ('assignation_true -> VARIABLE ASSIGNATION BOOLTRUE','assignation_true',3,'p_assignation_true','sintactico2.py',171),
  ('assignation_true -> VARIABLE ASSIGNATION VARIABLE','assignation_true',3,'p_assignation_true','sintactico2.py',172),
  ('assignation_true -> VARIABLE ASSIGNATION boolean_operation','assignation_true',3,'p_assignation_true','sintactico2.py',173),
  ('assignation_false -> VARIABLE ASSIGNATION BOOLFALSE','assignation_false',3,'p_assignation_false','sintactico2.py',177),
  ('assignation_false -> VARIABLE ASSIGNATION VARIABLE','assignation_false',3,'p_assignation_false','sintactico2.py',178),
  ('assignation_false -> VARIABLE ASSIGNATION boolean_operation','assignation_false',3,'p_assignation_false','sintactico2.py',179),
  ('assignation_type_value_multiple -> INTTYPE assignation_int_multiple','assignation_type_value_multiple',2,'p_assignation_type_value_multiple','sintactico2.py',184),
  ('assignation_type_value_multiple -> STRINGTYPE assignation_string_multiple','assignation_type_value_multiple',2,'p_assignation_type_value_multiple','sintactico2.py',185),
  ('assignation_type_value_multiple -> FLOATTYPE assignation_float_multiple','assignation_type_value_multiple',2,'p_assignation_type_value_multiple','sintactico2.py',186),
  ('assignation_type_value_multiple -> BOOLTYPE assignation_true_multiple','assignation_type_value_multiple',2,'p_assignation_type_value_multiple','sintactico2.py',187),
  ('assignation_type_value_multiple -> BOOLTYPE assignation_false_multiple','assignation_type_value_multiple',2,'p_assignation_type_value_multiple','sintactico2.py',188),
  ('assignation_int_multiple -> assignation_int','assignation_int_multiple',1,'p_assignation_int_multiple','sintactico2.py',192),
  ('assignation_int_multiple -> assignation_int COMMA assignation_int_multiple','assignation_int_multiple',3,'p_assignation_int_multiple','sintactico2.py',193),
  ('assignation_string_multiple -> assignation_string','assignation_string_multiple',1,'p_assignation_string_multiple','sintactico2.py',197),
  ('assignation_string_multiple -> assignation_string COMMA assignation_string_multiple','assignation_string_multiple',3,'p_assignation_string_multiple','sintactico2.py',198),
  ('assignation_float_multiple -> assignation_float','assignation_float_multiple',1,'p_assignation_float_multiple','sintactico2.py',202),
  ('assignation_float_multiple -> assignation_float COMMA assignation_float_multiple','assignation_float_multiple',3,'p_assignation_float_multiple','sintactico2.py',203),
  ('assignation_true_multiple -> assignation_true','assignation_true_multiple',1,'p_assignation_true_multiple','sintactico2.py',207),
  ('assignation_true_multiple -> assignation_true COMMA assignation_true_multiple','assignation_true_multiple',3,'p_assignation_true_multiple','sintactico2.py',208),
  ('assignation_false_multiple -> assignation_false','assignation_false_multiple',1,'p_assignation_false_multiple','sintactico2.py',212),
  ('assignation_false_multiple -> assignation_false COMMA assignation_false_multiple','assignation_false_multiple',3,'p_assignation_false_multiple','sintactico2.py',213),
]
