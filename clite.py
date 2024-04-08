import ply.lex as lex

tokens = [ 'INT' ]

t_ignore  = ' \t'

def getLexer():
    lexer = lex.lex()
    return lexer

def t_INT(t):
    r'[0-9]+(_[0-9]+)*'
    t.value = int(t.value)    
    return t