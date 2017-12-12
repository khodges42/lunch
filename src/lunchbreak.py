from compiler_util import lex

lexer = lex.Lex('test')


print(lexer.lex_file('test.lb'))
