import ply.lex as lex

#Diccionario de palabras reservadas
reserved = {
    #Inicio aporte Juan Guadalupe
    'const':'CONST',
    'bool':'BOOLTYPE',
    'true':'BOOLTRUE',
    'false':'BOOLFALSE',
    'char':'CHARTYPE',
    'decimal':'DECIMALTYPE',
    'double':'DOUBLETYPE',
    'float':'FLOATTYPE',
    'int':'INTTYPE',
    'class':'CLASS',
    'string':'STRINGTYPE',
    #Fin aporte Juan Guadalupe

    #Inicio aporte Adair Abrigo
    "if": "IF",
    "while": "WHILE",
    "public": "PUBLIC",
    "static": "STATIC",
    "void": "VOID",
    "long": "LONG",
    "return": "RETURN",
    "int": "INT",
    "for": "FOR",
    #Fin aporte Adair Abrigo
    #Inicio aporte David Rivera
    "break": "BREAK",
    "try": "TRY",
    "private": "PRIVATE",
    "new": "NEW",
    "switch": "SWITCH",
    "else": "ELSE",
    "catch": "CATCH"
    #Fin aporte David Rivera
    #Inicio aporte Kenneth Pacheco

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
    'DOUBLEPOINT',
    'PRINT',
    #Fin aporte Juan Guadalupe

    #Inicio aporte Adair Abrigo
    'FLOAT_NUMBER',
    'INTEGER',
    'BOOL',
    'OBJECT',
    'STRING',
    'PLUS',
    'MINUS',
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
    #Fin aporte Adair Abrigo
    #Inicio aporte David Rivera
        #Operadores de comparacion
    'INEQUALITY',
    'GREATER_THAN_OR_EQUAL',
    'SMALLER_THAN_OR_EQUAL',
        #Operadores logicos
    'LOGICAND',
    'LOGICOR',
    'LOGICNOT',
    'LOGICXOR', #TRUE SI A O B ES TRUE
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
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_PERCENT = r'\%'
t_DOLLARSIGN = r'\$'
t_GREATER_THAN = r'>'
t_SMALLER_THAN = r'<'
t_EQUAL_COMPARATION = r'=='
t_ASSIGNATION = r'='
t_DOTANDCOMMA = r';'
#Fin aporte Adair Abrigo
#Inicio aporte David Rivera
t_INEQUALITY = r'!='
t_GREATER_THAN_OR_EQUAL = r'>='
t_SMALLER_THAN_OR_EQUAL = r'<='
t_LOGICAND = r'\&\&'
t_LOGICOR = r'\|\|'
t_LOGICNOT = r'\!'
#Fin aporte David Rivera
#Inicio aporte Kenneth Pacheco
t_ADDITION_ASSIGNMENT = r'\+='
t_SUBTRACTION_ASSIGNMENT = r'-='
t_MULTIPLICATION_ASSIGNMENT = r'\*='
t_DIVISION_ASSIGNMENT = r'\/='
t_MODULE_ASSIGNMENT = r'%='
t_JUMP_LINE = r'\\n'
t_TABULATION = r'\\t'
t_DOUBLE_QUOTATION_MARKS = r'"'
t_SIPLE_QUOTATION_MARKS = r"'"
t_PIPE = r'\|'
t_BACK_SLASH = r'\\'
#Fin aporte Kenneth Pacheco

def t_PRINT(t):
    r'(Console\.WriteLine|Console\.Write|System\.Console\.WriteLine|System\.Console\.Write)'
    return t


#Para contabilizar nro de líneas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

#Inicio aporte Juan Guadalupe
def t_OBJECT(t):
  r'[A-Z]\w*'
  return t

def t_VARIABLE(t):
  r'[a-zA-Z\_]\w*'
  t.type = reserved.get(t.value,'VARIABLE')
  return t
#Fin aporte Juan Guadalupe

#Inicio aporte David Rivera
# #Para validar los tipos de datos
def t_FLOAT_NUMBER(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t
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


#Datos de entrada
def analizar(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


archivo = open("algoritmo1.txt")
for linea in archivo:
    print(">>"+linea)
    analizar(linea)
    if len(linea)==0:
        break

 # Tokenizador
#while True:
#  tok = lexer.token()
#  if not tok: 
#    break      #Rompe
#  print(tok)
