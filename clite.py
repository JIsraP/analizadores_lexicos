import ply.lex as lex

# Declare the states
states = (
    ('string', 'exclusive'),
)

tokens = [ 'INT', 'FLOAT', 'STR', 'STRCONTENT', 'QUOTATION' ]

t_ignore  = ' \t'

def getLexer():
    lexer = lex.lex()
    return lexer

# def t_STR(t):
#     r'.\"*[aA-zZ]+(\s.+)*.\"*'
#     t.value = str(t.value)
#     return t

# Regular expression rules for the initial state
def t_string(t):
    r'\"'
    t.lexer.str_start = t.lexer.lexpos
    t.lexer.begin('string')

def t_string_STR(t):
    r'\"'
    t.value = t.lexer.lexdata[t.lexer.str_start-1:t.lexer.lexpos]
    t.type = "STR"
    t.lexer.begin('INITIAL')
    return t

def t_string_QUOTATION(t):
    r'\\"'

def t_string_STRCONTENT(t):
    r'[^"]'

def t_FLOAT(t):
    r'([0-9]_?[0-9]+|[0-9]*)\.[0-9]*([eE]?[\+-]?([0-9]_?[0-9]*)+)?|[0-9]+[eE][\+-]?([0-9]_?[0-9]*)+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'[0-9]+(_[0-9]+)*'
    t.value = int(t.value)    
    return t