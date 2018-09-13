from antlr4 import CommonTokenStream, ParseTreeWalker, InputStream
from TpConjuntosLexer import TpConjuntosLexer
from TpConjuntosParser import TpConjuntosParser
from TpConjuntosListener import TpConjuntosListener
import antlr4

# TODO:
# Asignar sets a variables
# Seguir con el resto de las funciones de set


class RealListener(TpConjuntosListener):
    
    def __init__(self):
        self.variables = {}

    def enterProgram(self, ctx:TpConjuntosParser.ProgramContext):
        for node in ctx.children:
            self.visitStatement(node)

    def exitProgram(self, ctx:TpConjuntosParser.ProgramContext):
        print('Program ended. :)')


    def visitStatement(self, ctx:TpConjuntosParser.StatementContext):
        for node in ctx.children:
            if type(node) == TpConjuntosParser.ExpressionContext:
                result = self.visitExpression(node)
                print(result)
            
            elif type(node) == TpConjuntosParser.AssignStatementContext:
                self.visitAssignStatement(node)

            elif type(node) == antlr4.tree.Tree.TerminalNodeImpl:   # VARNAME
                result = self.variables[node.symbol.text]
                print(node.symbol.text + ' = ' + str(result))

            elif type(node) == TpConjuntosParser.BooleanExpressionContext:
                result = self.visitBooleanExpresion(node)
                print(result)

            elif type(node) == TpConjuntosParser.IfStatementContext:
                condition = self.visitBooleanExpresion(node.children[1])
                if condition:
                    i = 3
                    while i < len(node.children) - 1 and type(node.children[i]) != antlr4.tree.Tree.TerminalNodeImpl:
                        self.visitStatement(node.children[i])
                        i += 1
                else:
                    i = 3
                    while i < len(node.children) - 1 and type(node.children[i]) != antlr4.tree.Tree.TerminalNodeImpl:
                        i += 1
                        # sale del while cuando encuentra el ELSE
                    
                    i += 1      # Para saltear el ELSE
                    while i < len(node.children) - 1:
                        self.visitStatement(node.children[i])
                        i += 1
            
            elif type(node) == TpConjuntosParser.SetExpressionContext:
                self.visitSetExpression(node)

    
    def visitSetExpression(self, ctx:TpConjuntosParser.SetExpressionContext):
        aux = []
        n_start = int(ctx.n_start.text)
        n_end = int(ctx.n_end.text)
        
        if (ctx.n_step != None):
            n_step = int(ctx.n_step.text)
        else:
            n_step = 1

        for x in range(n_start, n_end + 1, n_step):
            aux.append(x)
        
        return aux


    # Ok
    def visitBooleanExpresion(self, ctx:TpConjuntosParser.BooleanExpressionContext):
        left =  self.visitOperand(ctx.children[0])
        right = self.visitOperand(ctx.children[2])
        op = ctx.children[1].symbol.text

        return eval(str(left) + op + str(right))

    # Ok
    def visitOperand(self, ctx:TpConjuntosParser.OperandContext):
        node = ctx.children[0]
        if type(node) == TpConjuntosParser.ExpressionContext:
            return self.visitExpression(node)

        if type(node) == antlr4.tree.Tree.TerminalNodeImpl:
            return self.variables[node.symbol.text]
        
        return ''   # No deberia pasar

    # Ok
    def visitAssignStatement(self, ctx:TpConjuntosParser.AssignStatementContext):
        name = ctx.children[0].symbol.text
        value = self.visitExpression(ctx.children[2])
        self.variables[name] = value

    # Ok
    def visitExpression(self, ctx:TpConjuntosParser.ExpressionContext):
        # Es un Term
        if type(ctx.children[0]) == TpConjuntosParser.TermContext:
            return self.visitTerm(ctx.children[0])
        
        # Es un Set
        if type(ctx.children[0]) == TpConjuntosParser.SetExpressionContext:
            return self.visitSetExpression(ctx.children[0])
        
        # Es una Expression + - Term
        sign = 1
        if ctx.children[1].symbol.text == '-':
            sign = -1

        value1 = self.visitExpression(ctx.children[0])
        value2 = self.visitTerm(ctx.children[2])

        return value1 + sign * value2

    # Ok
    def visitTerm(self, ctx:TpConjuntosParser.TermContext):
        if type(ctx.children[0]) == TpConjuntosParser.FactorContext:
            # Es un factor
            return self.visitFactor(ctx.children[0])

        # Es un term * / factor
        value1 = self.visitTerm(ctx.children[0])
        value2 = self.visitFactor(ctx.children[2])

        if ctx.children[1].symbol.text == '*':
            return value1 * value2

        return value1 / value2

    # Ok
    def visitFactor(self, ctx:TpConjuntosParser.FactorContext):
        
        if ctx.children[0].symbol.text != '(':
            nodo = ctx.children[0]
            return int(nodo.symbol.text)

        return self.visitExpression(ctx.children[1])
        

def main():
  
    program =   "a = 37 \n"
    program +=  "b = 54 \n"
    program +=  "c = set[0 5 2] \n"

    input = InputStream(program)
    lexer = TpConjuntosLexer(input)
    stream = CommonTokenStream(lexer)
    parser = TpConjuntosParser(stream)

    tree = parser.program()
    
    listener = RealListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
 
    print(listener.variables)

if __name__ == '__main__':
    main()