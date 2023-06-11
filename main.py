import ply.lex as lex

#Diccionario de palabras reservadas
reserved = {
    #Inicio aporte Juan Guadalupe
    'const':'CONST',
    'bool':'BOOLTYPE',
    'char':'CHARTYPE',
    'decimal':'DECIMALTYPE',
    'double':'DOUBLETYPE',
    'float':'FLOATTYPE',
    'int':'INTTYPE',
    'object':'OBJECT',
    'string':'STRINGTYPE',
    #Fin aporte Juan Guadalupe

    #Inicio aporte Adair Abrigo
    "if": "IF",
    "while": "WHILE",
    "public": "PUBLIC",
    "static": "STATIC",
    "long": "LONG",
    "return": "RETURN",
    "int": "INT",
    "for": "FOR",
    #Fin aporte Adair Abrigo
    #Inicio aporte David Rivera

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
    #Fin aporte Juan Guadalupe

    #Inicio aporte Adair Abrigo
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'GREATER_THAN',
    'SMALLER_THAN',
    'EQUAL_COMPARATION',
    'EQUAL',
    'DOTANDCOMMA',
    #Fin aporte Adair Abrigo
    #Inicio aporte David Rivera
        #Operadores de comparacion
    'INEQUALITY',
    'GREATER_THAN_OR_EQUAL',
    'SMALLER_THAN_OR_EQUAL',
        #Operadores logicos
    'AND',
    'OR',
    'NOT',
    'XOR', #TRUE SI A O B ES TRUE
    #Fin aporte David Rivera
    #Inicio aporte Kenneth Pacheco

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
#Fin aporte Juan Guadalupe
#Inicio aporte Adair Abrigo
t_NUMBER = r'\d+'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_GREATER_THAN = r'>'
t_SMALLER_THAN = r'<'
t_EQUAL_COMPARATION = r'=='
t_EQUAL = r'='
t_DOTANDCOMMA = r';'
#Fin aporte Adair Abrigo
#Inicio aporte David Rivera
t_INEQUALITY = r'!='
t_GREATER_THAN_OR_EQUAL = r'>='
t_SMALLER_THAN_OR_EQUAL = r'<='
t_AND = r'&&'
t_OR = r'||'
t_NOT = r'!'
#Fin aporte David Rivera
#Inicio aporte Kenneth Pacheco

#Fin aporte Kenneth Pacheco


 
 #Para contabilizar nro de líneas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

#Inicio aporte Juan Guadalupe
def t_VARIABLE(t):
  r'[a-zA-Z\_]\w*'
  t.type = reserved.get(t.value,'VARIABLE')
  return t
#Fin aporte Juan Guadalupe
 
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

#Testeando
data = '''
//comment de una linea
/*
coment 
multilinea
*/
public void MetodoBurbuja()
  {
    int t;
    for (int a = 1; a < vector.Length; a++)
      for (int b = vector.Length - 1; b >= a; b--)
      {
          if (vector[b - 1] > vector[b])
          {
              t = vector[b - 1];
              vector[b - 1] = vector[b];
              vector[b] = t;
          }
      }
  }

public static long Factorial(int n) 
  {
    if (n==1)               // Aseguramos que termine (caso base)
        return 1;
    return n * Factorial(n-1);  // Si no es 1, sigue la recursión
  }

    '''.lower()
 
 #Datos de entrada
lexer.input(data)
 
 # Tokenizador
while True:
  tok = lexer.token()
  if not tok: 
    break      #Rompe
  print(tok)
