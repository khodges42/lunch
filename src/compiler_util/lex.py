class Lex(object):
    def __init__(self, data):
        self.data = data

    def lex_line(self, line):
        return line

    def lex_file(self, filen):
        with open(filen) as f:
            for line in f:
                print self.lex_line(line)
                
