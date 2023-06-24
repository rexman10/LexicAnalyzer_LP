
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADDITION_ASSIGNMENT ASSIGNATION BACK_SLASH BOOL BOOLFALSE BOOLTRUE BOOLTYPE BREAK CATCH CHAR CHARTYPE CLASS COMMA CONST DECIMALTYPE DECIMAL_NUMBER DECREMENT DIVIDE DIVISION_ASSIGNMENT DOLLARSIGN DOT DOTANDCOMMA DOUBLEPOINT DOUBLE_QUOTATION_MARKS ELSE EQUAL_COMPARATION EXCEPTION FINALLY FLOATTYPE FLOAT_NUMBER FOR GREATER_THAN GREATER_THAN_OR_EQUAL IF INCREMENT INEQUALITY INTEGER INTTYPE JUMP_LINE LBRACKET LKEY LOGICAND LOGICNOT LOGICOR LOGICXOR LONG LPARENT MINUS MODULE_ASSIGNMENT MULTIPLICATION_ASSIGNMENT NAMESPACE NEW PERCENT PIPE PLUS PRINT PRIVATE PUBLIC RBRACKET READ RETURN RKEY RPARENT SIPLE_QUOTATION_MARKS SMALLER_THAN SMALLER_THAN_OR_EQUAL STATIC STRING STRINGTYPE SUBTRACTION_ASSIGNMENT SWITCH SYSTEM TABULATION TIMES TRY USING VARIABLE VOID WHILEprogram : block_using block_publicClassblock_using : USING SYSTEMblock_publicClass : PUBLIC CLASS VARIABLE LKEY block_code RKEYdata_type    : CHARTYPE\n                    | STRINGTYPE\n                    | FLOATTYPE\n                    | DECIMALTYPE\n                    | INTTYPE\n                    | BOOLTYPE\n    access_modifiers : PUBLIC\n                        | PRIVATE\n    arithmetic_operation : value_numeric\n                            | value_numeric arithmetic_operator arithmetic_operation\n    value_numeric    : INTEGER\n                        | FLOAT_NUMBER\n                        | DECIMAL_NUMBER\n                        | VARIABLE\n    value_logic  : BOOLTRUE\n                    | BOOLFALSE\n                    | VARIABLE\n    logic_operation  : value_logic\n                        | value_logic logic_operator logic_operation\n    concatenation    : STRING\n                        | STRING PLUS concatenation\n    value_string : STRING\n                    | CHAR\n                    | VARIABLE\n                    | READ LPARENT RPARENT\n                    | concatenation\n    value    : value_numeric\n                | value_logic\n                | value_string\n    logic_operator   : GREATER_THAN\n                        | SMALLER_THAN\n                        | EQUAL_COMPARATION\n                        | INEQUALITY\n                        | GREATER_THAN_OR_EQUAL\n                        | SMALLER_THAN_OR_EQUAL\n                        | LOGICAND\n                        | LOGICOR\n                        | LOGICNOT\n                        | LOGICXOR\n    arithmetic_operator  : PLUS\n                            | MINUS\n                            | TIMES\n                            | DIVIDE\n                            | PERCENT\n    constant_assignation : access_modifiers CONST data_type VARIABLE ASSIGNATION value\n                            | CONST data_type VARIABLE ASSIGNATION value\n    variable_assignation_simple  : access_modifiers data_type VARIABLE ASSIGNATION value\n                                    | data_type VARIABLE ASSIGNATION value\n                                    | data_type VARIABLE\n                                    | VARIABLE ASSIGNATION value\n    variable_multivalue  : variable_assignation_simple\n                            | variable_assignation_simple COMMA variable_multivalue\n    variable_assignation_multiline   : \n    block_code : VARIABLE\n                    | try_catch_simply\n    try_catch_simply : TRY LKEY block_code RKEY CATCH LPARENT EXCEPTION VARIABLE RPARENT LKEY block_code RKEY'
    
_lr_action_items = {'USING':([0,],[3,]),'$end':([1,4,14,],[0,-1,-3,]),'PUBLIC':([2,6,],[5,-2,]),'SYSTEM':([3,],[6,]),'CLASS':([5,],[7,]),'VARIABLE':([7,9,15,20,23,],[8,10,10,21,10,]),'LKEY':([8,13,22,],[9,15,23,]),'TRY':([9,15,23,],[13,13,13,]),'RKEY':([10,11,12,16,24,25,],[-57,14,-58,17,25,-59,]),'CATCH':([17,],[18,]),'LPARENT':([18,],[19,]),'EXCEPTION':([19,],[20,]),'RPARENT':([21,],[22,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'block_using':([0,],[2,]),'block_publicClass':([2,],[4,]),'block_code':([9,15,23,],[11,16,24,]),'try_catch_simply':([9,15,23,],[12,12,12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> block_using block_publicClass','program',2,'p_program','sintactico.py',11),
  ('block_using -> USING SYSTEM','block_using',2,'p_block_using','sintactico.py',14),
  ('block_publicClass -> PUBLIC CLASS VARIABLE LKEY block_code RKEY','block_publicClass',6,'p_block_publicClass','sintactico.py',17),
  ('data_type -> CHARTYPE','data_type',1,'p_data_type','sintactico.py',25),
  ('data_type -> STRINGTYPE','data_type',1,'p_data_type','sintactico.py',26),
  ('data_type -> FLOATTYPE','data_type',1,'p_data_type','sintactico.py',27),
  ('data_type -> DECIMALTYPE','data_type',1,'p_data_type','sintactico.py',28),
  ('data_type -> INTTYPE','data_type',1,'p_data_type','sintactico.py',29),
  ('data_type -> BOOLTYPE','data_type',1,'p_data_type','sintactico.py',30),
  ('access_modifiers -> PUBLIC','access_modifiers',1,'p_access_modifiers','sintactico.py',34),
  ('access_modifiers -> PRIVATE','access_modifiers',1,'p_access_modifiers','sintactico.py',35),
  ('arithmetic_operation -> value_numeric','arithmetic_operation',1,'p_arithmetic_operation','sintactico.py',39),
  ('arithmetic_operation -> value_numeric arithmetic_operator arithmetic_operation','arithmetic_operation',3,'p_arithmetic_operation','sintactico.py',40),
  ('value_numeric -> INTEGER','value_numeric',1,'p_value_numeric','sintactico.py',44),
  ('value_numeric -> FLOAT_NUMBER','value_numeric',1,'p_value_numeric','sintactico.py',45),
  ('value_numeric -> DECIMAL_NUMBER','value_numeric',1,'p_value_numeric','sintactico.py',46),
  ('value_numeric -> VARIABLE','value_numeric',1,'p_value_numeric','sintactico.py',47),
  ('value_logic -> BOOLTRUE','value_logic',1,'p_value_logic','sintactico.py',51),
  ('value_logic -> BOOLFALSE','value_logic',1,'p_value_logic','sintactico.py',52),
  ('value_logic -> VARIABLE','value_logic',1,'p_value_logic','sintactico.py',53),
  ('logic_operation -> value_logic','logic_operation',1,'p_logic_operation','sintactico.py',57),
  ('logic_operation -> value_logic logic_operator logic_operation','logic_operation',3,'p_logic_operation','sintactico.py',58),
  ('concatenation -> STRING','concatenation',1,'p_concatenation','sintactico.py',62),
  ('concatenation -> STRING PLUS concatenation','concatenation',3,'p_concatenation','sintactico.py',63),
  ('value_string -> STRING','value_string',1,'p_value_string','sintactico.py',67),
  ('value_string -> CHAR','value_string',1,'p_value_string','sintactico.py',68),
  ('value_string -> VARIABLE','value_string',1,'p_value_string','sintactico.py',69),
  ('value_string -> READ LPARENT RPARENT','value_string',3,'p_value_string','sintactico.py',70),
  ('value_string -> concatenation','value_string',1,'p_value_string','sintactico.py',71),
  ('value -> value_numeric','value',1,'p_value','sintactico.py',75),
  ('value -> value_logic','value',1,'p_value','sintactico.py',76),
  ('value -> value_string','value',1,'p_value','sintactico.py',77),
  ('logic_operator -> GREATER_THAN','logic_operator',1,'p_logic_operator','sintactico.py',81),
  ('logic_operator -> SMALLER_THAN','logic_operator',1,'p_logic_operator','sintactico.py',82),
  ('logic_operator -> EQUAL_COMPARATION','logic_operator',1,'p_logic_operator','sintactico.py',83),
  ('logic_operator -> INEQUALITY','logic_operator',1,'p_logic_operator','sintactico.py',84),
  ('logic_operator -> GREATER_THAN_OR_EQUAL','logic_operator',1,'p_logic_operator','sintactico.py',85),
  ('logic_operator -> SMALLER_THAN_OR_EQUAL','logic_operator',1,'p_logic_operator','sintactico.py',86),
  ('logic_operator -> LOGICAND','logic_operator',1,'p_logic_operator','sintactico.py',87),
  ('logic_operator -> LOGICOR','logic_operator',1,'p_logic_operator','sintactico.py',88),
  ('logic_operator -> LOGICNOT','logic_operator',1,'p_logic_operator','sintactico.py',89),
  ('logic_operator -> LOGICXOR','logic_operator',1,'p_logic_operator','sintactico.py',90),
  ('arithmetic_operator -> PLUS','arithmetic_operator',1,'p_arithmetic_operator','sintactico.py',94),
  ('arithmetic_operator -> MINUS','arithmetic_operator',1,'p_arithmetic_operator','sintactico.py',95),
  ('arithmetic_operator -> TIMES','arithmetic_operator',1,'p_arithmetic_operator','sintactico.py',96),
  ('arithmetic_operator -> DIVIDE','arithmetic_operator',1,'p_arithmetic_operator','sintactico.py',97),
  ('arithmetic_operator -> PERCENT','arithmetic_operator',1,'p_arithmetic_operator','sintactico.py',98),
  ('constant_assignation -> access_modifiers CONST data_type VARIABLE ASSIGNATION value','constant_assignation',6,'p_constant_assignation','sintactico.py',101),
  ('constant_assignation -> CONST data_type VARIABLE ASSIGNATION value','constant_assignation',5,'p_constant_assignation','sintactico.py',102),
  ('variable_assignation_simple -> access_modifiers data_type VARIABLE ASSIGNATION value','variable_assignation_simple',5,'p_variable_assignation_simple','sintactico.py',106),
  ('variable_assignation_simple -> data_type VARIABLE ASSIGNATION value','variable_assignation_simple',4,'p_variable_assignation_simple','sintactico.py',107),
  ('variable_assignation_simple -> data_type VARIABLE','variable_assignation_simple',2,'p_variable_assignation_simple','sintactico.py',108),
  ('variable_assignation_simple -> VARIABLE ASSIGNATION value','variable_assignation_simple',3,'p_variable_assignation_simple','sintactico.py',109),
  ('variable_multivalue -> variable_assignation_simple','variable_multivalue',1,'p_variable_multivalue','sintactico.py',113),
  ('variable_multivalue -> variable_assignation_simple COMMA variable_multivalue','variable_multivalue',3,'p_variable_multivalue','sintactico.py',114),
  ('variable_assignation_multiline -> <empty>','variable_assignation_multiline',0,'p_variable_assignation_multiline','sintactico.py',118),
  ('block_code -> VARIABLE','block_code',1,'p_block_code','sintactico.py',122),
  ('block_code -> try_catch_simply','block_code',1,'p_block_code','sintactico.py',123),
  ('try_catch_simply -> TRY LKEY block_code RKEY CATCH LPARENT EXCEPTION VARIABLE RPARENT LKEY block_code RKEY','try_catch_simply',12,'p_try_catch_simply','sintactico.py',127),
]
