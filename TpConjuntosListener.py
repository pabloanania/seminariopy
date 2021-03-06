# Generated from .\TpConjuntos.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TpConjuntosParser import TpConjuntosParser
else:
    from TpConjuntosParser import TpConjuntosParser

# This class defines a complete listener for a parse tree produced by TpConjuntosParser.
class TpConjuntosListener(ParseTreeListener):

    # Enter a parse tree produced by TpConjuntosParser#program.
    def enterProgram(self, ctx:TpConjuntosParser.ProgramContext):
        pass

    # Exit a parse tree produced by TpConjuntosParser#program.
    def exitProgram(self, ctx:TpConjuntosParser.ProgramContext):
        pass


    # Enter a parse tree produced by TpConjuntosParser#statement.
    def enterStatement(self, ctx:TpConjuntosParser.StatementContext):
        pass

    # Exit a parse tree produced by TpConjuntosParser#statement.
    def exitStatement(self, ctx:TpConjuntosParser.StatementContext):
        pass


    # Enter a parse tree produced by TpConjuntosParser#setElement.
    def enterSetElement(self, ctx:TpConjuntosParser.SetElementContext):
        pass

    # Exit a parse tree produced by TpConjuntosParser#setElement.
    def exitSetElement(self, ctx:TpConjuntosParser.SetElementContext):
        pass


    # Enter a parse tree produced by TpConjuntosParser#setFunction.
    def enterSetFunction(self, ctx:TpConjuntosParser.SetFunctionContext):
        pass

    # Exit a parse tree produced by TpConjuntosParser#setFunction.
    def exitSetFunction(self, ctx:TpConjuntosParser.SetFunctionContext):
        pass


    # Enter a parse tree produced by TpConjuntosParser#setBelongs.
    def enterSetBelongs(self, ctx:TpConjuntosParser.SetBelongsContext):
        pass

    # Exit a parse tree produced by TpConjuntosParser#setBelongs.
    def exitSetBelongs(self, ctx:TpConjuntosParser.SetBelongsContext):
        pass


    # Enter a parse tree produced by TpConjuntosParser#setElementSum.
    def enterSetElementSum(self, ctx:TpConjuntosParser.SetElementSumContext):
        pass

    # Exit a parse tree produced by TpConjuntosParser#setElementSum.
    def exitSetElementSum(self, ctx:TpConjuntosParser.SetElementSumContext):
        pass


    # Enter a parse tree produced by TpConjuntosParser#setElementAverage.
    def enterSetElementAverage(self, ctx:TpConjuntosParser.SetElementAverageContext):
        pass

    # Exit a parse tree produced by TpConjuntosParser#setElementAverage.
    def exitSetElementAverage(self, ctx:TpConjuntosParser.SetElementAverageContext):
        pass


    # Enter a parse tree produced by TpConjuntosParser#setLength.
    def enterSetLength(self, ctx:TpConjuntosParser.SetLengthContext):
        pass

    # Exit a parse tree produced by TpConjuntosParser#setLength.
    def exitSetLength(self, ctx:TpConjuntosParser.SetLengthContext):
        pass


    # Enter a parse tree produced by TpConjuntosParser#setIntersection.
    def enterSetIntersection(self, ctx:TpConjuntosParser.SetIntersectionContext):
        pass

    # Exit a parse tree produced by TpConjuntosParser#setIntersection.
    def exitSetIntersection(self, ctx:TpConjuntosParser.SetIntersectionContext):
        pass


    # Enter a parse tree produced by TpConjuntosParser#setUnion.
    def enterSetUnion(self, ctx:TpConjuntosParser.SetUnionContext):
        pass

    # Exit a parse tree produced by TpConjuntosParser#setUnion.
    def exitSetUnion(self, ctx:TpConjuntosParser.SetUnionContext):
        pass


    # Enter a parse tree produced by TpConjuntosParser#setDifference.
    def enterSetDifference(self, ctx:TpConjuntosParser.SetDifferenceContext):
        pass

    # Exit a parse tree produced by TpConjuntosParser#setDifference.
    def exitSetDifference(self, ctx:TpConjuntosParser.SetDifferenceContext):
        pass


    # Enter a parse tree produced by TpConjuntosParser#setComplement.
    def enterSetComplement(self, ctx:TpConjuntosParser.SetComplementContext):
        pass

    # Exit a parse tree produced by TpConjuntosParser#setComplement.
    def exitSetComplement(self, ctx:TpConjuntosParser.SetComplementContext):
        pass


    # Enter a parse tree produced by TpConjuntosParser#assignStatement.
    def enterAssignStatement(self, ctx:TpConjuntosParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by TpConjuntosParser#assignStatement.
    def exitAssignStatement(self, ctx:TpConjuntosParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by TpConjuntosParser#ifStatement.
    def enterIfStatement(self, ctx:TpConjuntosParser.IfStatementContext):
        pass

    # Exit a parse tree produced by TpConjuntosParser#ifStatement.
    def exitIfStatement(self, ctx:TpConjuntosParser.IfStatementContext):
        pass


    # Enter a parse tree produced by TpConjuntosParser#whileStatement.
    def enterWhileStatement(self, ctx:TpConjuntosParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by TpConjuntosParser#whileStatement.
    def exitWhileStatement(self, ctx:TpConjuntosParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by TpConjuntosParser#booleanExpression.
    def enterBooleanExpression(self, ctx:TpConjuntosParser.BooleanExpressionContext):
        pass

    # Exit a parse tree produced by TpConjuntosParser#booleanExpression.
    def exitBooleanExpression(self, ctx:TpConjuntosParser.BooleanExpressionContext):
        pass


    # Enter a parse tree produced by TpConjuntosParser#operand.
    def enterOperand(self, ctx:TpConjuntosParser.OperandContext):
        pass

    # Exit a parse tree produced by TpConjuntosParser#operand.
    def exitOperand(self, ctx:TpConjuntosParser.OperandContext):
        pass


    # Enter a parse tree produced by TpConjuntosParser#expression.
    def enterExpression(self, ctx:TpConjuntosParser.ExpressionContext):
        pass

    # Exit a parse tree produced by TpConjuntosParser#expression.
    def exitExpression(self, ctx:TpConjuntosParser.ExpressionContext):
        pass


    # Enter a parse tree produced by TpConjuntosParser#term.
    def enterTerm(self, ctx:TpConjuntosParser.TermContext):
        pass

    # Exit a parse tree produced by TpConjuntosParser#term.
    def exitTerm(self, ctx:TpConjuntosParser.TermContext):
        pass


    # Enter a parse tree produced by TpConjuntosParser#factor.
    def enterFactor(self, ctx:TpConjuntosParser.FactorContext):
        pass

    # Exit a parse tree produced by TpConjuntosParser#factor.
    def exitFactor(self, ctx:TpConjuntosParser.FactorContext):
        pass


