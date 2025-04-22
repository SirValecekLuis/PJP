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
        4,1,37,215,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,
        0,11,0,12,0,13,1,1,1,1,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,
        1,3,1,27,8,1,1,1,1,1,5,1,31,8,1,10,1,12,1,34,9,1,1,1,3,1,37,8,1,
        1,1,1,1,1,1,1,1,5,1,43,8,1,10,1,12,1,46,9,1,1,1,5,1,49,8,1,10,1,
        12,1,52,9,1,1,1,3,1,55,8,1,1,1,1,1,1,1,1,1,5,1,61,8,1,10,1,12,1,
        64,9,1,1,1,5,1,67,8,1,10,1,12,1,70,9,1,1,1,3,1,73,8,1,1,1,1,1,1,
        1,1,1,1,1,1,1,4,1,81,8,1,11,1,12,1,82,1,1,1,1,5,1,87,8,1,10,1,12,
        1,90,9,1,1,1,3,1,93,8,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,101,8,1,11,1,
        12,1,102,1,1,1,1,1,1,1,1,4,1,109,8,1,11,1,12,1,110,1,1,1,1,3,1,115,
        8,1,1,1,5,1,118,8,1,10,1,12,1,121,9,1,1,1,3,1,124,8,1,1,1,1,1,4,
        1,128,8,1,11,1,12,1,129,1,1,1,1,5,1,134,8,1,10,1,12,1,137,9,1,1,
        1,3,1,140,8,1,1,1,1,1,3,1,144,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,163,8,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,5,2,186,8,2,10,2,12,2,189,9,2,1,3,1,3,1,4,1,4,1,4,1,4,5,4,
        197,8,4,10,4,12,4,200,9,4,1,4,1,4,3,4,204,8,4,1,4,5,4,207,8,4,10,
        4,12,4,210,9,4,1,4,3,4,213,8,4,1,4,0,1,4,5,0,2,4,6,8,0,5,1,0,15,
        17,2,0,13,13,18,18,1,0,20,21,1,0,22,23,1,0,26,29,259,0,11,1,0,0,
        0,2,143,1,0,0,0,4,162,1,0,0,0,6,190,1,0,0,0,8,192,1,0,0,0,10,12,
        3,2,1,0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,
        14,1,1,0,0,0,15,144,3,8,4,0,16,17,5,32,0,0,17,18,5,1,0,0,18,22,3,
        4,2,0,19,21,5,2,0,0,20,19,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,22,
        23,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,25,27,5,36,0,0,26,25,1,0,
        0,0,26,27,1,0,0,0,27,144,1,0,0,0,28,32,3,4,2,0,29,31,5,2,0,0,30,
        29,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,36,1,0,0,
        0,34,32,1,0,0,0,35,37,5,36,0,0,36,35,1,0,0,0,36,37,1,0,0,0,37,144,
        1,0,0,0,38,39,5,3,0,0,39,44,5,32,0,0,40,41,5,4,0,0,41,43,5,32,0,
        0,42,40,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,50,
        1,0,0,0,46,44,1,0,0,0,47,49,5,2,0,0,48,47,1,0,0,0,49,52,1,0,0,0,
        50,48,1,0,0,0,50,51,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,53,55,5,
        36,0,0,54,53,1,0,0,0,54,55,1,0,0,0,55,144,1,0,0,0,56,57,5,5,0,0,
        57,62,3,4,2,0,58,59,5,4,0,0,59,61,3,4,2,0,60,58,1,0,0,0,61,64,1,
        0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,68,1,0,0,0,64,62,1,0,0,0,65,
        67,5,2,0,0,66,65,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,
        0,69,72,1,0,0,0,70,68,1,0,0,0,71,73,5,36,0,0,72,71,1,0,0,0,72,73,
        1,0,0,0,73,144,1,0,0,0,74,75,5,6,0,0,75,76,5,7,0,0,76,77,3,4,2,0,
        77,78,5,8,0,0,78,80,5,9,0,0,79,81,3,2,1,0,80,79,1,0,0,0,81,82,1,
        0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,84,88,5,10,0,0,85,
        87,5,2,0,0,86,85,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,
        0,89,92,1,0,0,0,90,88,1,0,0,0,91,93,5,36,0,0,92,91,1,0,0,0,92,93,
        1,0,0,0,93,144,1,0,0,0,94,95,5,11,0,0,95,96,5,7,0,0,96,97,3,4,2,
        0,97,98,5,8,0,0,98,100,5,9,0,0,99,101,3,2,1,0,100,99,1,0,0,0,101,
        102,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,104,1,0,0,0,104,
        114,5,10,0,0,105,106,5,12,0,0,106,108,5,9,0,0,107,109,3,2,1,0,108,
        107,1,0,0,0,109,110,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,
        112,1,0,0,0,112,113,5,10,0,0,113,115,1,0,0,0,114,105,1,0,0,0,114,
        115,1,0,0,0,115,119,1,0,0,0,116,118,5,2,0,0,117,116,1,0,0,0,118,
        121,1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,123,1,0,0,0,121,
        119,1,0,0,0,122,124,5,36,0,0,123,122,1,0,0,0,123,124,1,0,0,0,124,
        144,1,0,0,0,125,127,5,9,0,0,126,128,3,2,1,0,127,126,1,0,0,0,128,
        129,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,131,1,0,0,0,131,
        135,5,10,0,0,132,134,5,2,0,0,133,132,1,0,0,0,134,137,1,0,0,0,135,
        133,1,0,0,0,135,136,1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,0,138,
        140,5,36,0,0,139,138,1,0,0,0,139,140,1,0,0,0,140,144,1,0,0,0,141,
        144,5,2,0,0,142,144,5,36,0,0,143,15,1,0,0,0,143,16,1,0,0,0,143,28,
        1,0,0,0,143,38,1,0,0,0,143,56,1,0,0,0,143,74,1,0,0,0,143,94,1,0,
        0,0,143,125,1,0,0,0,143,141,1,0,0,0,143,142,1,0,0,0,144,3,1,0,0,
        0,145,146,6,2,-1,0,146,147,5,32,0,0,147,148,5,1,0,0,148,163,3,4,
        2,16,149,150,5,13,0,0,150,163,3,4,2,15,151,152,5,14,0,0,152,163,
        3,4,2,14,153,163,5,33,0,0,154,163,5,34,0,0,155,163,5,31,0,0,156,
        163,5,35,0,0,157,163,5,32,0,0,158,159,5,7,0,0,159,160,3,4,2,0,160,
        161,5,8,0,0,161,163,1,0,0,0,162,145,1,0,0,0,162,149,1,0,0,0,162,
        151,1,0,0,0,162,153,1,0,0,0,162,154,1,0,0,0,162,155,1,0,0,0,162,
        156,1,0,0,0,162,157,1,0,0,0,162,158,1,0,0,0,163,187,1,0,0,0,164,
        165,10,13,0,0,165,166,7,0,0,0,166,186,3,4,2,14,167,168,10,12,0,0,
        168,169,7,1,0,0,169,186,3,4,2,13,170,171,10,11,0,0,171,172,5,19,
        0,0,172,186,3,4,2,12,173,174,10,10,0,0,174,175,7,2,0,0,175,186,3,
        4,2,11,176,177,10,9,0,0,177,178,7,3,0,0,178,186,3,4,2,10,179,180,
        10,8,0,0,180,181,5,24,0,0,181,186,3,4,2,9,182,183,10,7,0,0,183,184,
        5,25,0,0,184,186,3,4,2,8,185,164,1,0,0,0,185,167,1,0,0,0,185,170,
        1,0,0,0,185,173,1,0,0,0,185,176,1,0,0,0,185,179,1,0,0,0,185,182,
        1,0,0,0,186,189,1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,5,1,
        0,0,0,189,187,1,0,0,0,190,191,7,4,0,0,191,7,1,0,0,0,192,193,3,6,
        3,0,193,198,5,32,0,0,194,195,5,4,0,0,195,197,5,32,0,0,196,194,1,
        0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,203,1,
        0,0,0,200,198,1,0,0,0,201,202,5,1,0,0,202,204,3,4,2,0,203,201,1,
        0,0,0,203,204,1,0,0,0,204,208,1,0,0,0,205,207,5,2,0,0,206,205,1,
        0,0,0,207,210,1,0,0,0,208,206,1,0,0,0,208,209,1,0,0,0,209,212,1,
        0,0,0,210,208,1,0,0,0,211,213,5,36,0,0,212,211,1,0,0,0,212,213,1,
        0,0,0,213,9,1,0,0,0,30,13,22,26,32,36,44,50,54,62,68,72,82,88,92,
        102,110,114,119,123,129,135,139,143,162,185,187,198,203,208,212
    ]

class exprParser ( Parser ):

    grammarFileName = "expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'read'", "','", "'write'", 
                     "'while'", "'('", "')'", "'{'", "'}'", "'if'", "'else'", 
                     "'-'", "'!'", "'*'", "'/'", "'%'", "'+'", "'.'", "'<'", 
                     "'>'", "'=='", "'!='", "'&&'", "'||'", "'int'", "'float'", 
                     "'bool'", "'string'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "COMMENT", "BOOL", "ID", 
                      "INT", "FLOAT", "STRING", "NEWLINE", "WS" ]

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
    COMMENT=30
    BOOL=31
    ID=32
    INT=33
    FLOAT=34
    STRING=35
    NEWLINE=36
    WS=37

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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 136298130156) != 0)):
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



    def stat(self):

        localctx = exprParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
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
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 136298130156) != 0)):
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
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 136298130156) != 0)):
                        break

                self.state = 104
                self.match(exprParser.T__9)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 105
                    self.match(exprParser.T__11)
                    self.state = 106
                    self.match(exprParser.T__8)
                    self.state = 108 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 107
                        self.stat()
                        self.state = 110 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 136298130156) != 0)):
                            break

                    self.state = 112
                    self.match(exprParser.T__9)


                self.state = 119
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 116
                        self.match(exprParser.T__1) 
                    self.state = 121
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                self.state = 123
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 122
                    self.match(exprParser.NEWLINE)


                pass

            elif la_ == 8:
                localctx = exprParser.MultistatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 125
                self.match(exprParser.T__8)
                self.state = 127 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 126
                    self.stat()
                    self.state = 129 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 136298130156) != 0)):
                        break

                self.state = 131
                self.match(exprParser.T__9)
                self.state = 135
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 132
                        self.match(exprParser.T__1) 
                    self.state = 137
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                self.state = 139
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 138
                    self.match(exprParser.NEWLINE)


                pass

            elif la_ == 9:
                localctx = exprParser.EmptysemicolonContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 141
                self.match(exprParser.T__1)
                pass

            elif la_ == 10:
                localctx = exprParser.NewlineContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 142
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
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                localctx = exprParser.AssignexprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 146
                self.match(exprParser.ID)
                self.state = 147
                self.match(exprParser.T__0)
                self.state = 148
                self.expr(16)
                pass

            elif la_ == 2:
                localctx = exprParser.UnaryminusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 149
                self.match(exprParser.T__12)
                self.state = 150
                self.expr(15)
                pass

            elif la_ == 3:
                localctx = exprParser.LogicnotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 151
                self.match(exprParser.T__13)
                self.state = 152
                self.expr(14)
                pass

            elif la_ == 4:
                localctx = exprParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 153
                self.match(exprParser.INT)
                pass

            elif la_ == 5:
                localctx = exprParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 154
                self.match(exprParser.FLOAT)
                pass

            elif la_ == 6:
                localctx = exprParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 155
                self.match(exprParser.BOOL)
                pass

            elif la_ == 7:
                localctx = exprParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 156
                self.match(exprParser.STRING)
                pass

            elif la_ == 8:
                localctx = exprParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 157
                self.match(exprParser.ID)
                pass

            elif la_ == 9:
                localctx = exprParser.ParanthesesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 158
                self.match(exprParser.T__6)
                self.state = 159
                self.expr(0)
                self.state = 160
                self.match(exprParser.T__7)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 187
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 185
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = exprParser.MuldivContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 164
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 165
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 229376) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 166
                        self.expr(14)
                        pass

                    elif la_ == 2:
                        localctx = exprParser.AddsubContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 167
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 168
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==18):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 169
                        self.expr(13)
                        pass

                    elif la_ == 3:
                        localctx = exprParser.StringconcatContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 170
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 171
                        self.match(exprParser.T__18)
                        self.state = 172
                        self.expr(12)
                        pass

                    elif la_ == 4:
                        localctx = exprParser.CompareContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 173
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 174
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 175
                        self.expr(11)
                        pass

                    elif la_ == 5:
                        localctx = exprParser.IsequalContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 176
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 177
                        _la = self._input.LA(1)
                        if not(_la==22 or _la==23):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 178
                        self.expr(10)
                        pass

                    elif la_ == 6:
                        localctx = exprParser.LogicandContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 179
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 180
                        self.match(exprParser.T__23)
                        self.state = 181
                        self.expr(9)
                        pass

                    elif la_ == 7:
                        localctx = exprParser.LogicorContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 182
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 183
                        self.match(exprParser.T__24)
                        self.state = 184
                        self.expr(8)
                        pass

             
                self.state = 189
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
            self.state = 190
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0)):
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
            self.state = 192
            self.vartype()
            self.state = 193
            self.match(exprParser.ID)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 194
                self.match(exprParser.T__3)
                self.state = 195
                self.match(exprParser.ID)
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 201
                self.match(exprParser.T__0)
                self.state = 202
                self.expr(0)


            self.state = 208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 205
                    self.match(exprParser.T__1) 
                self.state = 210
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 211
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
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 7)
         




