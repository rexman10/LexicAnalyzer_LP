import ply.lex as lex
lexical_result = []
#Diccionario de palabras reservadas
reserved = {
    #Inicio aporte Juan Guadalupe
    'const':'CONST',
    'bool':'BOOLTYPE',
    'true':'BOOLTRUE',
    'false':'BOOLFALSE',
    'char':'CHARTYPE',
    'float':'FLOATTYPE',
    'decimal':'DECIMALTYPE',
    'int':'INTTYPE',
    'class':'CLASS',
    'string':'STRINGTYPE',
    'namespace':'NAMESPACE',
    'Task':'TASK',
    'async':'ASYNC',
    'Queue':'QUEUE',
    'EnQueue':'ENQUEUE',
    'DeQueue':'DEQUEUE',
    'Peek':'PEEK',
    'IsEmpty':'ISEMPTY',
    #Fin aporte Juan Guadalupe

    #Inicio aporte Adair Abrigo
    "if": "IF",
    "while": "WHILE",
    "public": "PUBLIC",
    "private": "PRIVATE",
    "static": "STATIC",
    "void": "VOID",
    "long": "LONG",
    "return": "RETURN",
    "for": "FOR",
    "foreach": "FOREACH",
    "in": "IN",
    "finally": "FINALLY",
    "exception": "EXCEPTION",
    "List":"LIST",
    "Add":"ADD",
    "Clear":"CLEAR",
    "RemoveAt":"REMOVEAT",
    "Count":"COUNT",
    "Action":"ACTION",
    "await":"AWAIT",
    "Main":"MAIN",
    "e":"ERROR",
    "enum":"ENUM",
    #Fin aporte Adair Abrigo

    #Inicio aporte David Rivera
    "Concurrent": "CONCURRENT",
    "ContainsKey": "CONTAINSKEY",
    "ContainsValue": "CONTAINSVALUE",
    #Cambiar la R minucla por mayuscula
    "Remove": "REMOVEDICT",
    "Thread": "THREAD",
    "Start": "START",
    "Join": "JOIN",
    "Write": "WRITE",
    "Dictionary": "DICTIONARY",
    "else_if": "ELSE_IF",
    "put": "PUT",
    "break": "BREAK",
    "try": "TRY",
    "new": "NEW",
    "switch": "SWITCH",
    "else": "ELSE",
    "catch": "CATCH",
    #Fin aporte David Rivera
    #Inicio aporte Kenneth Pacheco
    'do': 'DO',
    "using": "USING",
    "System": "SYSTEM",
    "Stack": "STACK",
    "Push": "PUSH",
    "Pop": "POP",
    #Fin aporte Kenneth Pacheco

}

 #Sequencia de tokens, puede ser lista o tupla
tokens = (
    #Inicio aporte Juan Guadalupe
    'VARIABLE',
    'LPARENT',
    'RPARENT',
    'LBRACKET',
    'RBRACKET',
    'LKEY',
    'RKEY',
    'DOT',
    'ID',
    'DOUBLEPOINT',
    'PRINT',
    'READ',
    'METHOD',
    #Fin aporte Juan Guadalupe

    #Inicio aporte Adair Abrigo
    'FLOAT_NUMBER',
    'DECIMAL_NUMBER',
    'INTEGER',
    'STRING',
    'CHAR',
    'PLUS',
    'INCREMENT',
    'MINUS',
    'DECREMENT',
    'TIMES',
    'DIVIDE',
    'PERCENT',
    'DOLLARSIGN',
    'GREATER_THAN',
    'SMALLER_THAN',
    'EQUAL_COMPARATION',
    'ASSIGNATION',
    'COMMA',
    'DOTANDCOMMA',
    'ARROW',
    #Fin aporte Adair Abrigo
    #Inicio aporte David Rivera
    #Operadores de comparacion
    'INEQUALITY',
    'GREATER_THAN_OR_EQUAL',
    'SMALLER_THAN_OR_EQUAL',
    'IDENTIFIER',
    #Operadores logicos
    'LOGICAND',
    'LOGICOR',
    'LOGICNOT',
    #Fin aporte David Rivera
    #Inicio aporte Kenneth Pacheco
    'ADDITION_ASSIGNMENT',
    'SUBTRACTION_ASSIGNMENT',
    'MULTIPLICATION_ASSIGNMENT',
    'DIVISION_ASSIGNMENT',
    'MODULE_ASSIGNMENT',
    'JUMP_LINE',
    'TABULATION',
    'DOUBLE_QUOTATION_MARKS',
    'SIPLE_QUOTATION_MARKS',
    'BACK_SLASH',
    'PIPE'
    #Fin aporte Kenneth Pacheco


) + tuple(reserved.values())

 #Exp Regulares para tokens de símbolos

#Inicio aporte Juan Guadalupe
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LKEY = r'\{'
t_RKEY = r'\}'
t_DOT   = r'\.'
t_COMMA = r'\,'
t_DOUBLEPOINT = r'\:'
#Fin aporte Juan Guadalupe
#Inicio aporte Adair Abrigo
t_STRING = r'("[^"]*"|\'[^\']*\')'
t_PLUS = r'\+'
t_INCREMENT = r'\+\+'
t_MINUS = r'-'
t_DECREMENT = r'\-\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_PERCENT = r'\%'
t_DOLLARSIGN = r'\$'
t_GREATER_THAN = r'\>'
t_SMALLER_THAN = r'\<'
t_EQUAL_COMPARATION = r'\=\='
t_ASSIGNATION = r'\='
t_DOTANDCOMMA = r'\;'
t_ARROW = r'\=\>'
#Fin aporte Adair Abrigo
#Inicio aporte David Rivera
t_INEQUALITY = r'\!\='
t_GREATER_THAN_OR_EQUAL = r'\>\='
t_SMALLER_THAN_OR_EQUAL = r'\<\='
t_LOGICAND = r'\&\&'
t_LOGICOR = r'\|\|'
t_LOGICNOT = r'\!'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
#Fin aporte David Rivera
#Inicio aporte Kenneth Pacheco
t_ADDITION_ASSIGNMENT = r'\+\='
t_SUBTRACTION_ASSIGNMENT = r'\-\='
t_MULTIPLICATION_ASSIGNMENT = r'\*\='
t_DIVISION_ASSIGNMENT = r'\/\='
t_MODULE_ASSIGNMENT = r'\%\='
t_JUMP_LINE = r'\\n'
t_TABULATION = r'\\t'
t_DOUBLE_QUOTATION_MARKS = r'"'
t_SIPLE_QUOTATION_MARKS = r"'"
t_PIPE = r'\|'
t_BACK_SLASH = r'\\'
#Fin aporte Kenneth Pacheco


def t_PRINT(t):
    r'Console\.WriteLine'
    return t

def t_READ(t):
    r'Console\.ReadLine'
    return t

#Para contabilizar nro de líneas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)
  global numero_linea
  numero_linea = t.lexer.lineno


#Inicio aporte Juan Guadalupe
def t_METHOD(t):
  r'[A-Z]\w*'
  t.type = reserved.get(t.value,'METHOD')
  return t
def t_VARIABLE(t):
  r'[a-z\_]\w*'
  t.type = reserved.get(t.value,'VARIABLE')
  return t
#Fin aporte Juan Guadalupe

#Inicio aporte David Rivera
# #Para validar los tipos de datos
def t_DECIMAL_NUMBER(t):
    r'\-?\d+\.\d+m'
    t.value = float(str(t.value)[0:-2])
    return t
def t_FLOAT_NUMBER(t):
    r'\-?\d+\.\d+f'
    t.value = float(str(t.value)[0:-2])
    return t
def t_INTEGER(t):
    r'\-?\d+'
    t.value = int(t.value)
    return t
def t_CHAR(t):
    r'\'[a-zA-Z]\''
    t.value = str(t.value)
    return t

#Para reestablecer el numero delineas al analizar nuevo archivo
def resetear_numero_linea():
    global numero_linea
    numero_linea = 1

def obtener_numero_linea():
    return numero_linea

#Fin aporte David Rivera

 # Ignorar lo que no sea un token en mi LP
t_ignore  = ' \t'

 #Presentación de errores léxicos
def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)
 #Reconocer comentarios
#Inicio aporte Juan Guadalupe
def t_COMMENT(t):
    r'(\/\/.*|(/\*(.|\n)*?\*/))'
    pass
#Fin aporte Juan Guadalupe
 #Contruir analizador
lexer = lex.lex()

def analyze_lexical_string(content, numero_linea_inicial=1):
    lexer.lineno = numero_linea_inicial
    lexer.input(content)
    lexical_result = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        lexical_result.append(tok)
    return lexical_result




