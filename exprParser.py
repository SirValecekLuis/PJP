# Generated from expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,40,242,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,
        0,11,0,12,0,13,1,1,1,1,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,
        1,3,1,27,8,1,1,1,1,1,5,1,31,8,1,10,1,12,1,34,9,1,1,1,3,1,37,8,1,
        1,1,1,1,1,1,1,1,5,1,43,8,1,10,1,12,1,46,9,1,1,1,5,1,49,8,1,10,1,
        12,1,52,9,1,1,1,3,1,55,8,1,1,1,1,1,1,1,1,1,5,1,61,8,1,10,1,12,1,
        64,9,1,1,1,5,1,67,8,1,10,1,12,1,70,9,1,1,1,3,1,73,8,1,1,1,1,1,1,
        1,1,1,1,1,1,1,4,1,81,8,1,11,1,12,1,82,1,1,1,1,5,1,87,8,1,10,1,12,
        1,90,9,1,1,1,3,1,93,8,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,101,8,1,11,1,
        12,1,102,1,1,1,1,1,1,3,1,108,8,1,1,1,1,1,1,1,4,1,113,8,1,11,1,12,
        1,114,1,1,1,1,1,1,3,1,120,8,1,3,1,122,8,1,1,1,5,1,125,8,1,10,1,12,
        1,128,9,1,1,1,3,1,131,8,1,1,1,1,1,4,1,135,8,1,11,1,12,1,136,1,1,
        1,1,5,1,141,8,1,10,1,12,1,144,9,1,1,1,3,1,147,8,1,1,1,1,1,1,1,1,
        1,1,1,5,1,154,8,1,10,1,12,1,157,9,1,1,1,5,1,160,8,1,10,1,12,1,163,
        9,1,1,1,3,1,166,8,1,1,1,1,1,3,1,170,8,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,190,8,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,5,2,213,8,2,10,2,12,2,216,9,2,1,3,1,3,1,4,1,4,1,
        4,1,4,5,4,224,8,4,10,4,12,4,227,9,4,1,4,1,4,3,4,231,8,4,1,4,5,4,
        234,8,4,10,4,12,4,237,9,4,1,4,3,4,240,8,4,1,4,0,1,4,5,0,2,4,6,8,
        0,5,1,0,16,18,2,0,14,14,19,19,1,0,21,22,1,0,23,24,1,0,27,31,293,
        0,11,1,0,0,0,2,169,1,0,0,0,4,189,1,0,0,0,6,217,1,0,0,0,8,219,1,0,
        0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,
        1,0,0,0,14,1,1,0,0,0,15,170,3,8,4,0,16,17,5,34,0,0,17,18,5,1,0,0,
        18,22,3,4,2,0,19,21,5,2,0,0,20,19,1,0,0,0,21,24,1,0,0,0,22,20,1,
        0,0,0,22,23,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,25,27,5,39,0,0,26,
        25,1,0,0,0,26,27,1,0,0,0,27,170,1,0,0,0,28,32,3,4,2,0,29,31,5,2,
        0,0,30,29,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,36,
        1,0,0,0,34,32,1,0,0,0,35,37,5,39,0,0,36,35,1,0,0,0,36,37,1,0,0,0,
        37,170,1,0,0,0,38,39,5,3,0,0,39,44,5,34,0,0,40,41,5,4,0,0,41,43,
        5,34,0,0,42,40,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,
        45,50,1,0,0,0,46,44,1,0,0,0,47,49,5,2,0,0,48,47,1,0,0,0,49,52,1,
        0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,53,
        55,5,39,0,0,54,53,1,0,0,0,54,55,1,0,0,0,55,170,1,0,0,0,56,57,5,5,
        0,0,57,62,3,4,2,0,58,59,5,4,0,0,59,61,3,4,2,0,60,58,1,0,0,0,61,64,
        1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,68,1,0,0,0,64,62,1,0,0,0,
        65,67,5,2,0,0,66,65,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,
        0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,71,73,5,39,0,0,72,71,1,0,0,0,72,
        73,1,0,0,0,73,170,1,0,0,0,74,75,5,6,0,0,75,76,5,7,0,0,76,77,3,4,
        2,0,77,78,5,8,0,0,78,80,5,9,0,0,79,81,3,2,1,0,80,79,1,0,0,0,81,82,
        1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,84,88,5,10,0,0,
        85,87,5,2,0,0,86,85,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,
        0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,91,93,5,39,0,0,92,91,1,0,0,0,92,
        93,1,0,0,0,93,170,1,0,0,0,94,95,5,11,0,0,95,96,5,7,0,0,96,97,3,4,
        2,0,97,107,5,8,0,0,98,100,5,9,0,0,99,101,3,2,1,0,100,99,1,0,0,0,
        101,102,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,104,1,0,0,0,
        104,105,5,10,0,0,105,108,1,0,0,0,106,108,3,2,1,0,107,98,1,0,0,0,
        107,106,1,0,0,0,108,121,1,0,0,0,109,119,5,12,0,0,110,112,5,9,0,0,
        111,113,3,2,1,0,112,111,1,0,0,0,113,114,1,0,0,0,114,112,1,0,0,0,
        114,115,1,0,0,0,115,116,1,0,0,0,116,117,5,10,0,0,117,120,1,0,0,0,
        118,120,3,2,1,0,119,110,1,0,0,0,119,118,1,0,0,0,120,122,1,0,0,0,
        121,109,1,0,0,0,121,122,1,0,0,0,122,126,1,0,0,0,123,125,5,2,0,0,
        124,123,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,
        127,130,1,0,0,0,128,126,1,0,0,0,129,131,5,39,0,0,130,129,1,0,0,0,
        130,131,1,0,0,0,131,170,1,0,0,0,132,134,5,9,0,0,133,135,3,2,1,0,
        134,133,1,0,0,0,135,136,1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,
        137,138,1,0,0,0,138,142,5,10,0,0,139,141,5,2,0,0,140,139,1,0,0,0,
        141,144,1,0,0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,146,1,0,0,0,
        144,142,1,0,0,0,145,147,5,39,0,0,146,145,1,0,0,0,146,147,1,0,0,0,
        147,170,1,0,0,0,148,149,5,34,0,0,149,150,5,13,0,0,150,155,3,4,2,
        0,151,152,5,13,0,0,152,154,3,4,2,0,153,151,1,0,0,0,154,157,1,0,0,
        0,155,153,1,0,0,0,155,156,1,0,0,0,156,161,1,0,0,0,157,155,1,0,0,
        0,158,160,5,2,0,0,159,158,1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,
        0,161,162,1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,164,166,5,39,0,
        0,165,164,1,0,0,0,165,166,1,0,0,0,166,170,1,0,0,0,167,170,5,2,0,
        0,168,170,5,39,0,0,169,15,1,0,0,0,169,16,1,0,0,0,169,28,1,0,0,0,
        169,38,1,0,0,0,169,56,1,0,0,0,169,74,1,0,0,0,169,94,1,0,0,0,169,
        132,1,0,0,0,169,148,1,0,0,0,169,167,1,0,0,0,169,168,1,0,0,0,170,
        3,1,0,0,0,171,172,6,2,-1,0,172,173,5,34,0,0,173,174,5,1,0,0,174,
        190,3,4,2,17,175,176,5,14,0,0,176,190,3,4,2,16,177,178,5,15,0,0,
        178,190,3,4,2,15,179,190,5,38,0,0,180,190,5,35,0,0,181,190,5,36,
        0,0,182,190,5,33,0,0,183,190,5,37,0,0,184,190,5,34,0,0,185,186,5,
        7,0,0,186,187,3,4,2,0,187,188,5,8,0,0,188,190,1,0,0,0,189,171,1,
        0,0,0,189,175,1,0,0,0,189,177,1,0,0,0,189,179,1,0,0,0,189,180,1,
        0,0,0,189,181,1,0,0,0,189,182,1,0,0,0,189,183,1,0,0,0,189,184,1,
        0,0,0,189,185,1,0,0,0,190,214,1,0,0,0,191,192,10,14,0,0,192,193,
        7,0,0,0,193,213,3,4,2,15,194,195,10,13,0,0,195,196,7,1,0,0,196,213,
        3,4,2,14,197,198,10,12,0,0,198,199,5,20,0,0,199,213,3,4,2,13,200,
        201,10,11,0,0,201,202,7,2,0,0,202,213,3,4,2,12,203,204,10,10,0,0,
        204,205,7,3,0,0,205,213,3,4,2,11,206,207,10,9,0,0,207,208,5,25,0,
        0,208,213,3,4,2,10,209,210,10,8,0,0,210,211,5,26,0,0,211,213,3,4,
        2,9,212,191,1,0,0,0,212,194,1,0,0,0,212,197,1,0,0,0,212,200,1,0,
        0,0,212,203,1,0,0,0,212,206,1,0,0,0,212,209,1,0,0,0,213,216,1,0,
        0,0,214,212,1,0,0,0,214,215,1,0,0,0,215,5,1,0,0,0,216,214,1,0,0,
        0,217,218,7,4,0,0,218,7,1,0,0,0,219,220,3,6,3,0,220,225,5,34,0,0,
        221,222,5,4,0,0,222,224,5,34,0,0,223,221,1,0,0,0,224,227,1,0,0,0,
        225,223,1,0,0,0,225,226,1,0,0,0,226,230,1,0,0,0,227,225,1,0,0,0,
        228,229,5,1,0,0,229,231,3,4,2,0,230,228,1,0,0,0,230,231,1,0,0,0,
        231,235,1,0,0,0,232,234,5,2,0,0,233,232,1,0,0,0,234,237,1,0,0,0,
        235,233,1,0,0,0,235,236,1,0,0,0,236,239,1,0,0,0,237,235,1,0,0,0,
        238,240,5,39,0,0,239,238,1,0,0,0,239,240,1,0,0,0,240,9,1,0,0,0,35,
        13,22,26,32,36,44,50,54,62,68,72,82,88,92,102,107,114,119,121,126,
        130,136,142,146,155,161,165,169,189,212,214,225,230,235,239
    ]

class exprParser ( Parser ):

    grammarFileName = "expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'read'", "','", "'write'", 
                     "'while'", "'('", "')'", "'{'", "'}'", "'if'", "'else'", 
                     "'<<'", "'-'", "'!'", "'*'", "'/'", "'%'", "'+'", "'.'", 
                     "'<'", "'>'", "'=='", "'!='", "'&&'", "'||'", "'int'", 
                     "'float'", "'bool'", "'string'", "'file'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "COMMENT", "BOOL", "ID", "INT", "FLOAT", "STRING", 
                      "FILE", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_vartype = 3
    RULE_decl = 4

    ruleNames =  [ "prog", "stat", "expr", "vartype", "decl" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    COMMENT=32
    BOOL=33
    ID=34
    INT=35
    FLOAT=36
    STRING=37
    FILE=38
    NEWLINE=39
    WS=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.StatContext)
            else:
                return self.getTypedRuleContext(exprParser.StatContext,i)


        def getRuleIndex(self):
            return exprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = exprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.stat()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1095082494700) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintvarContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(exprParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(exprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintvar" ):
                listener.enterPrintvar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintvar" ):
                listener.exitPrintvar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintvar" ):
                return visitor.visitPrintvar(self)
            else:
                return visitor.visitChildren(self)


    class NewlineContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(exprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewline" ):
                listener.enterNewline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewline" ):
                listener.exitNewline(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline" ):
                return visitor.visitNewline(self)
            else:
                return visitor.visitChildren(self)


    class ReadContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(exprParser.ID)
            else:
                return self.getToken(exprParser.ID, i)
        def NEWLINE(self):
            return self.getToken(exprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)


    class IfstatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(exprParser.ExprContext,0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.StatContext)
            else:
                return self.getTypedRuleContext(exprParser.StatContext,i)

        def NEWLINE(self):
            return self.getToken(exprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfstatement" ):
                listener.enterIfstatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfstatement" ):
                listener.exitIfstatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstatement" ):
                return visitor.visitIfstatement(self)
            else:
                return visitor.visitChildren(self)


    class DeclarContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def decl(self):
            return self.getTypedRuleContext(exprParser.DeclContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclar" ):
                listener.enterDeclar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclar" ):
                listener.exitDeclar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclar" ):
                return visitor.visitDeclar(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(exprParser.ExprContext,0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.StatContext)
            else:
                return self.getTypedRuleContext(exprParser.StatContext,i)

        def NEWLINE(self):
            return self.getToken(exprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class MultistatementContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.StatContext)
            else:
                return self.getTypedRuleContext(exprParser.StatContext,i)

        def NEWLINE(self):
            return self.getToken(exprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultistatement" ):
                listener.enterMultistatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultistatement" ):
                listener.exitMultistatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultistatement" ):
                return visitor.visitMultistatement(self)
            else:
                return visitor.visitChildren(self)


    class WriteContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprParser.ExprContext,i)

        def NEWLINE(self):
            return self.getToken(exprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)


    class EmptysemicolonContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptysemicolon" ):
                listener.enterEmptysemicolon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptysemicolon" ):
                listener.exitEmptysemicolon(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptysemicolon" ):
                return visitor.visitEmptysemicolon(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(exprParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(exprParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(exprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)


    class FilewriteContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(exprParser.ID, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprParser.ExprContext,i)

        def NEWLINE(self):
            return self.getToken(exprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilewrite" ):
                listener.enterFilewrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilewrite" ):
                listener.exitFilewrite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilewrite" ):
                return visitor.visitFilewrite(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = exprParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                localctx = exprParser.DeclarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.decl()
                pass

            elif la_ == 2:
                localctx = exprParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(exprParser.ID)
                self.state = 17
                self.match(exprParser.T__0)
                self.state = 18
                self.expr(0)
                self.state = 22
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 19
                        self.match(exprParser.T__1) 
                    self.state = 24
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 26
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 25
                    self.match(exprParser.NEWLINE)


                pass

            elif la_ == 3:
                localctx = exprParser.PrintvarContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.expr(0)
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 29
                        self.match(exprParser.T__1) 
                    self.state = 34
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                self.state = 36
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 35
                    self.match(exprParser.NEWLINE)


                pass

            elif la_ == 4:
                localctx = exprParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.match(exprParser.T__2)
                self.state = 39
                self.match(exprParser.ID)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 40
                    self.match(exprParser.T__3)
                    self.state = 41
                    self.match(exprParser.ID)
                    self.state = 46
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 50
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 47
                        self.match(exprParser.T__1) 
                    self.state = 52
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                self.state = 54
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 53
                    self.match(exprParser.NEWLINE)


                pass

            elif la_ == 5:
                localctx = exprParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 56
                self.match(exprParser.T__4)
                self.state = 57
                self.expr(0)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 58
                    self.match(exprParser.T__3)
                    self.state = 59
                    self.expr(0)
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 65
                        self.match(exprParser.T__1) 
                    self.state = 70
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                self.state = 72
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 71
                    self.match(exprParser.NEWLINE)


                pass

            elif la_ == 6:
                localctx = exprParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 74
                self.match(exprParser.T__5)
                self.state = 75
                self.match(exprParser.T__6)
                self.state = 76
                self.expr(0)
                self.state = 77
                self.match(exprParser.T__7)
                self.state = 78
                self.match(exprParser.T__8)
                self.state = 80 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 79
                    self.stat()
                    self.state = 82 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1095082494700) != 0)):
                        break

                self.state = 84
                self.match(exprParser.T__9)
                self.state = 88
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 85
                        self.match(exprParser.T__1) 
                    self.state = 90
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                self.state = 92
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 91
                    self.match(exprParser.NEWLINE)


                pass

            elif la_ == 7:
                localctx = exprParser.IfstatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 94
                self.match(exprParser.T__10)
                self.state = 95
                self.match(exprParser.T__6)
                self.state = 96
                self.expr(0)
                self.state = 97
                self.match(exprParser.T__7)
                self.state = 107
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 98
                    self.match(exprParser.T__8)
                    self.state = 100 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 99
                        self.stat()
                        self.state = 102 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1095082494700) != 0)):
                            break

                    self.state = 104
                    self.match(exprParser.T__9)
                    pass

                elif la_ == 2:
                    self.state = 106
                    self.stat()
                    pass


                self.state = 121
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 109
                    self.match(exprParser.T__11)
                    self.state = 119
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        self.state = 110
                        self.match(exprParser.T__8)
                        self.state = 112 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 111
                            self.stat()
                            self.state = 114 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1095082494700) != 0)):
                                break

                        self.state = 116
                        self.match(exprParser.T__9)
                        pass

                    elif la_ == 2:
                        self.state = 118
                        self.stat()
                        pass




                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 123
                        self.match(exprParser.T__1) 
                    self.state = 128
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                self.state = 130
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 129
                    self.match(exprParser.NEWLINE)


                pass

            elif la_ == 8:
                localctx = exprParser.MultistatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 132
                self.match(exprParser.T__8)
                self.state = 134 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 133
                    self.stat()
                    self.state = 136 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1095082494700) != 0)):
                        break

                self.state = 138
                self.match(exprParser.T__9)
                self.state = 142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 139
                        self.match(exprParser.T__1) 
                    self.state = 144
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                self.state = 146
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 145
                    self.match(exprParser.NEWLINE)


                pass

            elif la_ == 9:
                localctx = exprParser.FilewriteContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 148
                self.match(exprParser.ID)
                self.state = 149
                self.match(exprParser.T__12)
                self.state = 150
                self.expr(0)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 151
                    self.match(exprParser.T__12)
                    self.state = 152
                    self.expr(0)
                    self.state = 157
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 161
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 158
                        self.match(exprParser.T__1) 
                    self.state = 163
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                self.state = 165
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 164
                    self.match(exprParser.NEWLINE)


                pass

            elif la_ == 10:
                localctx = exprParser.EmptysemicolonContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 167
                self.match(exprParser.T__1)
                pass

            elif la_ == 11:
                localctx = exprParser.NewlineContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 168
                self.match(exprParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class CompareContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompare" ):
                listener.enterCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompare" ):
                listener.exitCompare(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare" ):
                return visitor.visitCompare(self)
            else:
                return visitor.visitChildren(self)


    class BoolContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(exprParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(exprParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(exprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class LogicorContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicor" ):
                listener.enterLogicor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicor" ):
                listener.exitLogicor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicor" ):
                return visitor.visitLogicor(self)
            else:
                return visitor.visitChildren(self)


    class ParanthesesContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(exprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParantheses" ):
                listener.enterParantheses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParantheses" ):
                listener.exitParantheses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParantheses" ):
                return visitor.visitParantheses(self)
            else:
                return visitor.visitChildren(self)


    class AddsubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddsub" ):
                listener.enterAddsub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddsub" ):
                listener.exitAddsub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddsub" ):
                return visitor.visitAddsub(self)
            else:
                return visitor.visitChildren(self)


    class AssignexprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(exprParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(exprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignexpr" ):
                listener.enterAssignexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignexpr" ):
                listener.exitAssignexpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignexpr" ):
                return visitor.visitAssignexpr(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(exprParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(exprParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class MuldivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMuldiv" ):
                listener.enterMuldiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMuldiv" ):
                listener.exitMuldiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMuldiv" ):
                return visitor.visitMuldiv(self)
            else:
                return visitor.visitChildren(self)


    class LogicandContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicand" ):
                listener.enterLogicand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicand" ):
                listener.exitLogicand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicand" ):
                return visitor.visitLogicand(self)
            else:
                return visitor.visitChildren(self)


    class FileContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FILE(self):
            return self.getToken(exprParser.FILE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile" ):
                listener.enterFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile" ):
                listener.exitFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile" ):
                return visitor.visitFile(self)
            else:
                return visitor.visitChildren(self)


    class StringconcatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringconcat" ):
                listener.enterStringconcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringconcat" ):
                listener.exitStringconcat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringconcat" ):
                return visitor.visitStringconcat(self)
            else:
                return visitor.visitChildren(self)


    class LogicnotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(exprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicnot" ):
                listener.enterLogicnot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicnot" ):
                listener.exitLogicnot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicnot" ):
                return visitor.visitLogicnot(self)
            else:
                return visitor.visitChildren(self)


    class IsequalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsequal" ):
                listener.enterIsequal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsequal" ):
                listener.exitIsequal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsequal" ):
                return visitor.visitIsequal(self)
            else:
                return visitor.visitChildren(self)


    class UnaryminusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(exprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryminus" ):
                listener.enterUnaryminus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryminus" ):
                listener.exitUnaryminus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryminus" ):
                return visitor.visitUnaryminus(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = exprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                localctx = exprParser.AssignexprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 172
                self.match(exprParser.ID)
                self.state = 173
                self.match(exprParser.T__0)
                self.state = 174
                self.expr(17)
                pass

            elif la_ == 2:
                localctx = exprParser.UnaryminusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 175
                self.match(exprParser.T__13)
                self.state = 176
                self.expr(16)
                pass

            elif la_ == 3:
                localctx = exprParser.LogicnotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 177
                self.match(exprParser.T__14)
                self.state = 178
                self.expr(15)
                pass

            elif la_ == 4:
                localctx = exprParser.FileContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 179
                self.match(exprParser.FILE)
                pass

            elif la_ == 5:
                localctx = exprParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 180
                self.match(exprParser.INT)
                pass

            elif la_ == 6:
                localctx = exprParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 181
                self.match(exprParser.FLOAT)
                pass

            elif la_ == 7:
                localctx = exprParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 182
                self.match(exprParser.BOOL)
                pass

            elif la_ == 8:
                localctx = exprParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 183
                self.match(exprParser.STRING)
                pass

            elif la_ == 9:
                localctx = exprParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 184
                self.match(exprParser.ID)
                pass

            elif la_ == 10:
                localctx = exprParser.ParanthesesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 185
                self.match(exprParser.T__6)
                self.state = 186
                self.expr(0)
                self.state = 187
                self.match(exprParser.T__7)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 212
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = exprParser.MuldivContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 191
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 192
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 193
                        self.expr(15)
                        pass

                    elif la_ == 2:
                        localctx = exprParser.AddsubContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 194
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 195
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==19):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 196
                        self.expr(14)
                        pass

                    elif la_ == 3:
                        localctx = exprParser.StringconcatContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 197
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 198
                        self.match(exprParser.T__19)
                        self.state = 199
                        self.expr(13)
                        pass

                    elif la_ == 4:
                        localctx = exprParser.CompareContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 200
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 201
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 202
                        self.expr(12)
                        pass

                    elif la_ == 5:
                        localctx = exprParser.IsequalContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 203
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 204
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 205
                        self.expr(11)
                        pass

                    elif la_ == 6:
                        localctx = exprParser.LogicandContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 206
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 207
                        self.match(exprParser.T__24)
                        self.state = 208
                        self.expr(10)
                        pass

                    elif la_ == 7:
                        localctx = exprParser.LogicorContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 209
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 210
                        self.match(exprParser.T__25)
                        self.state = 211
                        self.expr(9)
                        pass

             
                self.state = 216
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class VartypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprParser.RULE_vartype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVartype" ):
                listener.enterVartype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVartype" ):
                listener.exitVartype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVartype" ):
                return visitor.visitVartype(self)
            else:
                return visitor.visitChildren(self)




    def vartype(self):

        localctx = exprParser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vartype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4160749568) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(exprParser.VartypeContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(exprParser.ID)
            else:
                return self.getToken(exprParser.ID, i)

        def expr(self):
            return self.getTypedRuleContext(exprParser.ExprContext,0)


        def NEWLINE(self):
            return self.getToken(exprParser.NEWLINE, 0)

        def getRuleIndex(self):
            return exprParser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = exprParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.vartype()
            self.state = 220
            self.match(exprParser.ID)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 221
                self.match(exprParser.T__3)
                self.state = 222
                self.match(exprParser.ID)
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 228
                self.match(exprParser.T__0)
                self.state = 229
                self.expr(0)


            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 232
                    self.match(exprParser.T__1) 
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 238
                self.match(exprParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         




