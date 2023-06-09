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
    'LLLAVE',
    'RLLAVE',
    'LCORCHETE',
    'RCORCHETE',
    'PUNTO',
    #Fin aporte Juan Guadalupe

    #Inicio aporte Adair Abrigo

    #Fin aporte Adair Abrigo
    #Inicio aporte David Rivera

    #Fin aporte David Rivera
    #Inicio aporte Kenneth Pacheco

    #Fin aporte Kenneth Pacheco


) + tuple(reserved.values())
 
 #Exp Regulares para tokens de símbolos

#Inicio aporte Juan Guadalupe
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LLLAVE = r'\['
t_RLLAVE = r'\]'
t_LCORCHETE = r'\{'
t_RCORCHETE = r'\}'
t_PUNTO   = r'\.'
#Fin aporte Juan Guadalupe
#Inicio aporte Adair Abrigo

#Fin aporte Adair Abrigo
#Inicio aporte David Rivera

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
    '''.lower()
 
 #Datos de entrada
lexer.input(data)
 
 # Tokenizador
while True:
  tok = lexer.token()
  if not tok: 
    break      #Rompe
  print(tok)
