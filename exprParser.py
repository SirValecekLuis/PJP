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
        4,1,38,167,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,
        0,11,0,12,0,13,1,1,1,1,1,1,1,1,1,1,3,1,21,8,1,1,1,1,1,3,1,25,8,1,
        1,1,1,1,1,1,1,1,5,1,31,8,1,10,1,12,1,34,9,1,1,1,1,1,1,1,1,1,5,1,
        40,8,1,10,1,12,1,43,9,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,51,8,1,11,1,
        12,1,52,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,63,8,1,11,1,12,1,64,
        1,1,1,1,1,1,1,1,4,1,71,8,1,11,1,12,1,72,1,1,1,1,3,1,77,8,1,1,1,1,
        1,4,1,81,8,1,11,1,12,1,82,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,92,8,1,
        10,1,12,1,95,9,1,1,1,3,1,98,8,1,1,1,3,1,101,8,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,121,
        8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,5,2,144,8,2,10,2,12,2,147,9,2,1,3,1,3,1,
        4,1,4,1,4,1,4,5,4,155,8,4,10,4,12,4,158,9,4,1,4,1,4,3,4,162,8,4,
        1,4,3,4,165,8,4,1,4,0,1,4,5,0,2,4,6,8,0,5,1,0,15,17,2,0,13,13,18,
        18,1,0,20,21,1,0,22,23,1,0,26,30,201,0,11,1,0,0,0,2,100,1,0,0,0,
        4,120,1,0,0,0,6,148,1,0,0,0,8,150,1,0,0,0,10,12,3,2,1,0,11,10,1,
        0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,1,1,0,0,0,15,
        101,3,8,4,0,16,17,5,32,0,0,17,18,5,1,0,0,18,20,3,4,2,0,19,21,5,37,
        0,0,20,19,1,0,0,0,20,21,1,0,0,0,21,101,1,0,0,0,22,24,3,4,2,0,23,
        25,5,37,0,0,24,23,1,0,0,0,24,25,1,0,0,0,25,101,1,0,0,0,26,27,5,2,
        0,0,27,32,5,32,0,0,28,29,5,3,0,0,29,31,5,32,0,0,30,28,1,0,0,0,31,
        34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,101,1,0,0,0,34,32,1,0,
        0,0,35,36,5,4,0,0,36,41,3,4,2,0,37,38,5,3,0,0,38,40,3,4,2,0,39,37,
        1,0,0,0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,101,1,0,0,0,
        43,41,1,0,0,0,44,45,5,5,0,0,45,46,5,6,0,0,46,47,3,4,2,0,47,48,5,
        7,0,0,48,50,5,8,0,0,49,51,3,2,1,0,50,49,1,0,0,0,51,52,1,0,0,0,52,
        50,1,0,0,0,52,53,1,0,0,0,53,54,1,0,0,0,54,55,5,9,0,0,55,101,1,0,
        0,0,56,57,5,10,0,0,57,58,5,6,0,0,58,59,3,4,2,0,59,60,5,7,0,0,60,
        62,5,8,0,0,61,63,3,2,1,0,62,61,1,0,0,0,63,64,1,0,0,0,64,62,1,0,0,
        0,64,65,1,0,0,0,65,66,1,0,0,0,66,76,5,9,0,0,67,68,5,11,0,0,68,70,
        5,8,0,0,69,71,3,2,1,0,70,69,1,0,0,0,71,72,1,0,0,0,72,70,1,0,0,0,
        72,73,1,0,0,0,73,74,1,0,0,0,74,75,5,9,0,0,75,77,1,0,0,0,76,67,1,
        0,0,0,76,77,1,0,0,0,77,101,1,0,0,0,78,80,5,8,0,0,79,81,3,2,1,0,80,
        79,1,0,0,0,81,82,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,
        0,84,85,5,9,0,0,85,101,1,0,0,0,86,87,5,32,0,0,87,88,5,12,0,0,88,
        93,3,4,2,0,89,90,5,12,0,0,90,92,3,4,2,0,91,89,1,0,0,0,92,95,1,0,
        0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,96,98,
        5,37,0,0,97,96,1,0,0,0,97,98,1,0,0,0,98,101,1,0,0,0,99,101,5,37,
        0,0,100,15,1,0,0,0,100,16,1,0,0,0,100,22,1,0,0,0,100,26,1,0,0,0,
        100,35,1,0,0,0,100,44,1,0,0,0,100,56,1,0,0,0,100,78,1,0,0,0,100,
        86,1,0,0,0,100,99,1,0,0,0,101,3,1,0,0,0,102,103,6,2,-1,0,103,104,
        5,32,0,0,104,105,5,1,0,0,105,121,3,4,2,17,106,107,5,13,0,0,107,121,
        3,4,2,16,108,109,5,14,0,0,109,121,3,4,2,15,110,121,5,36,0,0,111,
        121,5,33,0,0,112,121,5,34,0,0,113,121,5,31,0,0,114,121,5,35,0,0,
        115,121,5,32,0,0,116,117,5,6,0,0,117,118,3,4,2,0,118,119,5,7,0,0,
        119,121,1,0,0,0,120,102,1,0,0,0,120,106,1,0,0,0,120,108,1,0,0,0,
        120,110,1,0,0,0,120,111,1,0,0,0,120,112,1,0,0,0,120,113,1,0,0,0,
        120,114,1,0,0,0,120,115,1,0,0,0,120,116,1,0,0,0,121,145,1,0,0,0,
        122,123,10,14,0,0,123,124,7,0,0,0,124,144,3,4,2,15,125,126,10,13,
        0,0,126,127,7,1,0,0,127,144,3,4,2,14,128,129,10,12,0,0,129,130,5,
        19,0,0,130,144,3,4,2,13,131,132,10,11,0,0,132,133,7,2,0,0,133,144,
        3,4,2,12,134,135,10,10,0,0,135,136,7,3,0,0,136,144,3,4,2,11,137,
        138,10,9,0,0,138,139,5,24,0,0,139,144,3,4,2,10,140,141,10,8,0,0,
        141,142,5,25,0,0,142,144,3,4,2,9,143,122,1,0,0,0,143,125,1,0,0,0,
        143,128,1,0,0,0,143,131,1,0,0,0,143,134,1,0,0,0,143,137,1,0,0,0,
        143,140,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,
        146,5,1,0,0,0,147,145,1,0,0,0,148,149,7,4,0,0,149,7,1,0,0,0,150,
        151,3,6,3,0,151,156,5,32,0,0,152,153,5,3,0,0,153,155,5,32,0,0,154,
        152,1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,156,157,1,0,0,0,157,
        161,1,0,0,0,158,156,1,0,0,0,159,160,5,1,0,0,160,162,3,4,2,0,161,
        159,1,0,0,0,161,162,1,0,0,0,162,164,1,0,0,0,163,165,5,37,0,0,164,
        163,1,0,0,0,164,165,1,0,0,0,165,9,1,0,0,0,19,13,20,24,32,41,52,64,
        72,76,82,93,97,100,120,143,145,156,161,164
    ]

class exprParser ( Parser ):

    grammarFileName = "expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'read'", "','", "'write'", "'while'", 
                     "'('", "')'", "'{'", "'}'", "'if'", "'else'", "'<<'", 
                     "'-'", "'!'", "'*'", "'/'", "'%'", "'+'", "'.'", "'<'", 
                     "'>'", "'=='", "'!='", "'&&'", "'||'", "'int'", "'float'", 
                     "'bool'", "'string'", "'file'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "BOOL", "ID", 
                      "INT", "FLOAT", "STRING", "FILE", "NEWLINE", "WS" ]

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
    BOOL=31
    ID=32
    INT=33
    FLOAT=34
    STRING=35
    FILE=36
    NEWLINE=37
    WS=38

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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 274810824052) != 0)):
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
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
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
                self.state = 20
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 19
                    self.match(exprParser.NEWLINE)


                pass

            elif la_ == 3:
                localctx = exprParser.PrintvarContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.expr(0)
                self.state = 24
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 23
                    self.match(exprParser.NEWLINE)


                pass

            elif la_ == 4:
                localctx = exprParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.match(exprParser.T__1)
                self.state = 27
                self.match(exprParser.ID)
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 28
                    self.match(exprParser.T__2)
                    self.state = 29
                    self.match(exprParser.ID)
                    self.state = 34
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 5:
                localctx = exprParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 35
                self.match(exprParser.T__3)
                self.state = 36
                self.expr(0)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 37
                    self.match(exprParser.T__2)
                    self.state = 38
                    self.expr(0)
                    self.state = 43
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 6:
                localctx = exprParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 44
                self.match(exprParser.T__4)
                self.state = 45
                self.match(exprParser.T__5)
                self.state = 46
                self.expr(0)
                self.state = 47
                self.match(exprParser.T__6)
                self.state = 48
                self.match(exprParser.T__7)
                self.state = 50 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 49
                    self.stat()
                    self.state = 52 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 274810824052) != 0)):
                        break

                self.state = 54
                self.match(exprParser.T__8)
                pass

            elif la_ == 7:
                localctx = exprParser.IfstatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 56
                self.match(exprParser.T__9)
                self.state = 57
                self.match(exprParser.T__5)
                self.state = 58
                self.expr(0)
                self.state = 59
                self.match(exprParser.T__6)
                self.state = 60
                self.match(exprParser.T__7)
                self.state = 62 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 61
                    self.stat()
                    self.state = 64 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 274810824052) != 0)):
                        break

                self.state = 66
                self.match(exprParser.T__8)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 67
                    self.match(exprParser.T__10)
                    self.state = 68
                    self.match(exprParser.T__7)
                    self.state = 70 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 69
                        self.stat()
                        self.state = 72 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 274810824052) != 0)):
                            break

                    self.state = 74
                    self.match(exprParser.T__8)


                pass

            elif la_ == 8:
                localctx = exprParser.MultistatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 78
                self.match(exprParser.T__7)
                self.state = 80 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 79
                    self.stat()
                    self.state = 82 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 274810824052) != 0)):
                        break

                self.state = 84
                self.match(exprParser.T__8)
                pass

            elif la_ == 9:
                localctx = exprParser.FilewriteContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 86
                self.match(exprParser.ID)
                self.state = 87
                self.match(exprParser.T__11)
                self.state = 88
                self.expr(0)
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 89
                    self.match(exprParser.T__11)
                    self.state = 90
                    self.expr(0)
                    self.state = 95
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 97
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 96
                    self.match(exprParser.NEWLINE)


                pass

            elif la_ == 10:
                localctx = exprParser.NewlineContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 99
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
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = exprParser.AssignexprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 103
                self.match(exprParser.ID)
                self.state = 104
                self.match(exprParser.T__0)
                self.state = 105
                self.expr(17)
                pass

            elif la_ == 2:
                localctx = exprParser.UnaryminusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.match(exprParser.T__12)
                self.state = 107
                self.expr(16)
                pass

            elif la_ == 3:
                localctx = exprParser.LogicnotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 108
                self.match(exprParser.T__13)
                self.state = 109
                self.expr(15)
                pass

            elif la_ == 4:
                localctx = exprParser.FileContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 110
                self.match(exprParser.FILE)
                pass

            elif la_ == 5:
                localctx = exprParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 111
                self.match(exprParser.INT)
                pass

            elif la_ == 6:
                localctx = exprParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 112
                self.match(exprParser.FLOAT)
                pass

            elif la_ == 7:
                localctx = exprParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 113
                self.match(exprParser.BOOL)
                pass

            elif la_ == 8:
                localctx = exprParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 114
                self.match(exprParser.STRING)
                pass

            elif la_ == 9:
                localctx = exprParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 115
                self.match(exprParser.ID)
                pass

            elif la_ == 10:
                localctx = exprParser.ParanthesesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 116
                self.match(exprParser.T__5)
                self.state = 117
                self.expr(0)
                self.state = 118
                self.match(exprParser.T__6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 143
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = exprParser.MuldivContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 122
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 123
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 229376) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 124
                        self.expr(15)
                        pass

                    elif la_ == 2:
                        localctx = exprParser.AddsubContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 125
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 126
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==18):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 127
                        self.expr(14)
                        pass

                    elif la_ == 3:
                        localctx = exprParser.StringconcatContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 128
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 129
                        self.match(exprParser.T__18)
                        self.state = 130
                        self.expr(13)
                        pass

                    elif la_ == 4:
                        localctx = exprParser.CompareContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 131
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 132
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 133
                        self.expr(12)
                        pass

                    elif la_ == 5:
                        localctx = exprParser.IsequalContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 134
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 135
                        _la = self._input.LA(1)
                        if not(_la==22 or _la==23):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 136
                        self.expr(11)
                        pass

                    elif la_ == 6:
                        localctx = exprParser.LogicandContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 137
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 138
                        self.match(exprParser.T__23)
                        self.state = 139
                        self.expr(10)
                        pass

                    elif la_ == 7:
                        localctx = exprParser.LogicorContext(self, exprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 140
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 141
                        self.match(exprParser.T__24)
                        self.state = 142
                        self.expr(9)
                        pass

             
                self.state = 147
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
            self.state = 148
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2080374784) != 0)):
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
            self.state = 150
            self.vartype()
            self.state = 151
            self.match(exprParser.ID)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 152
                self.match(exprParser.T__2)
                self.state = 153
                self.match(exprParser.ID)
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 159
                self.match(exprParser.T__0)
                self.state = 160
                self.expr(0)


            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 163
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
         




