import ply.lex as lex

#Diccionario de palabras reservadas
reserved = {
    'if':'IF',
    'else':'ELSE',
    'for':'FOR',
    'while':'WHILE',
    'bool':'BOOLEAN',
    'char':'CHAR',
    'decimal':'DECIMAL',
    'double':'DOUBLE',
    'float':'FLOTANTE',
    'int':'INTEGER',
    'string':'STRING',
}

 #Sequencia de tokens, puede ser lista o tupla
tokens = (
    'NUMERO',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'VARIABLE',
    'COMA',
    'MAYORQ',
    'MENORQ',
    'IGUALQ',
    'DIFERENTEQ',
    'CADENA',
    'RPARENT',
    'LPARENT',
) + tuple(reserved.values())
 
 #Exp Regulares para tokens de símbolos
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NUMERO  = r'\d+'
t_COMA    = r','
t_MAYORQ  = r'>'
t_MENORQ  = r'<'
t_DIFERENTEQ  = r'<>'
t_IGUALQ  = r'=='
t_CADENA  = r'"[\w\s\*]*"'

 
 #Para contabilizar nro de líneas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_VARIABLE(t):
  r'[a-zA-Z]\w*'
  t.type = reserved.get(t.value,'VARIABLE')
  return t

 
 # Ignorar lo que no sea un token en mi LP
t_ignore  = ' \t'
 
 #Presentación de errores léxicos
def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)
 #Reconocer comentarios
def t_COMMENT(t):
    r'\#.*'
    pass
 #Contruir analizador
lexer = lex.lex()

#Testeando
data = '''
cadena para prueba
    '''.lower()
 
 #Datos de entrada
lexer.input(data)
 
 # Tokenizador
while True:
  tok = lexer.token()
  if not tok: 
    break      #Rompe
  print(tok)
