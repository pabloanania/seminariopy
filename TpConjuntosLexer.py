# Generated from .\TpConjuntos.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24")
        buf.write("i\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17X\n\17")
        buf.write("\3\20\6\20[\n\20\r\20\16\20\\\3\21\6\21`\n\21\r\21\16")
        buf.write("\21a\3\22\3\22\3\23\3\23\3\23\3\23\2\2\24\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\3\2\6\4\2>>@@\3\2c|\3\2\62;\5\2")
        buf.write("\13\f\17\17\"\"\2n\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\3\'\3\2\2\2\5,\3\2\2\2\7.\3\2")
        buf.write("\2\2\t\60\3\2\2\2\13\63\3\2\2\2\r9\3\2\2\2\17?\3\2\2\2")
        buf.write("\21B\3\2\2\2\23D\3\2\2\2\25F\3\2\2\2\27H\3\2\2\2\31J\3")
        buf.write("\2\2\2\33L\3\2\2\2\35W\3\2\2\2\37Z\3\2\2\2!_\3\2\2\2#")
        buf.write("c\3\2\2\2%e\3\2\2\2\'(\7u\2\2()\7g\2\2)*\7v\2\2*+\7]\2")
        buf.write("\2+\4\3\2\2\2,-\7_\2\2-\6\3\2\2\2./\7?\2\2/\b\3\2\2\2")
        buf.write("\60\61\7k\2\2\61\62\7h\2\2\62\n\3\2\2\2\63\64\7v\2\2\64")
        buf.write("\65\7j\2\2\65\66\7g\2\2\66\67\7p\2\2\678\7\"\2\28\f\3")
        buf.write("\2\2\29:\7g\2\2:;\7n\2\2;<\7u\2\2<=\7g\2\2=>\7\"\2\2>")
        buf.write("\16\3\2\2\2?@\7h\2\2@A\7k\2\2A\20\3\2\2\2BC\7-\2\2C\22")
        buf.write("\3\2\2\2DE\7/\2\2E\24\3\2\2\2FG\7,\2\2G\26\3\2\2\2HI\7")
        buf.write("\61\2\2I\30\3\2\2\2JK\7*\2\2K\32\3\2\2\2LM\7+\2\2M\34")
        buf.write("\3\2\2\2NO\7?\2\2OX\7?\2\2PQ\7>\2\2QX\7?\2\2RS\7@\2\2")
        buf.write("SX\7?\2\2TX\t\2\2\2UV\7#\2\2VX\7?\2\2WN\3\2\2\2WP\3\2")
        buf.write("\2\2WR\3\2\2\2WT\3\2\2\2WU\3\2\2\2X\36\3\2\2\2Y[\t\3\2")
        buf.write("\2ZY\3\2\2\2[\\\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2] \3\2\2")
        buf.write("\2^`\5#\22\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2\2ab\3\2\2\2b")
        buf.write("\"\3\2\2\2cd\t\4\2\2d$\3\2\2\2ef\t\5\2\2fg\3\2\2\2gh\b")
        buf.write("\23\2\2h&\3\2\2\2\6\2W\\a\3\b\2\2")
        return buf.getvalue()


class TpConjuntosLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    COMPARATION_OPERATOR = 14
    VARNAME = 15
    NUMBER = 16
    DIGIT = 17
    WS = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'set['", "']'", "'='", "'if'", "'then '", "'else '", "'fi'", 
            "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "COMPARATION_OPERATOR", "VARNAME", "NUMBER", "DIGIT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "COMPARATION_OPERATOR", 
                  "VARNAME", "NUMBER", "DIGIT", "WS" ]

    grammarFileName = "TpConjuntos.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


