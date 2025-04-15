# Generated from expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .exprParser import exprParser
else:
    from exprParser import exprParser

# This class defines a complete listener for a parse tree produced by exprParser.
class exprListener(ParseTreeListener):

    # Enter a parse tree produced by exprParser#prog.
    def enterProg(self, ctx:exprParser.ProgContext):
        pass

    # Exit a parse tree produced by exprParser#prog.
    def exitProg(self, ctx:exprParser.ProgContext):
        pass


    # Enter a parse tree produced by exprParser#declar.
    def enterDeclar(self, ctx:exprParser.DeclarContext):
        pass

    # Exit a parse tree produced by exprParser#declar.
    def exitDeclar(self, ctx:exprParser.DeclarContext):
        pass


    # Enter a parse tree produced by exprParser#assign.
    def enterAssign(self, ctx:exprParser.AssignContext):
        pass

    # Exit a parse tree produced by exprParser#assign.
    def exitAssign(self, ctx:exprParser.AssignContext):
        pass


    # Enter a parse tree produced by exprParser#printvar.
    def enterPrintvar(self, ctx:exprParser.PrintvarContext):
        pass

    # Exit a parse tree produced by exprParser#printvar.
    def exitPrintvar(self, ctx:exprParser.PrintvarContext):
        pass


    # Enter a parse tree produced by exprParser#read.
    def enterRead(self, ctx:exprParser.ReadContext):
        pass

    # Exit a parse tree produced by exprParser#read.
    def exitRead(self, ctx:exprParser.ReadContext):
        pass


    # Enter a parse tree produced by exprParser#write.
    def enterWrite(self, ctx:exprParser.WriteContext):
        pass

    # Exit a parse tree produced by exprParser#write.
    def exitWrite(self, ctx:exprParser.WriteContext):
        pass


    # Enter a parse tree produced by exprParser#while.
    def enterWhile(self, ctx:exprParser.WhileContext):
        pass

    # Exit a parse tree produced by exprParser#while.
    def exitWhile(self, ctx:exprParser.WhileContext):
        pass


    # Enter a parse tree produced by exprParser#ifstatement.
    def enterIfstatement(self, ctx:exprParser.IfstatementContext):
        pass

    # Exit a parse tree produced by exprParser#ifstatement.
    def exitIfstatement(self, ctx:exprParser.IfstatementContext):
        pass


    # Enter a parse tree produced by exprParser#multistatement.
    def enterMultistatement(self, ctx:exprParser.MultistatementContext):
        pass

    # Exit a parse tree produced by exprParser#multistatement.
    def exitMultistatement(self, ctx:exprParser.MultistatementContext):
        pass


    # Enter a parse tree produced by exprParser#newline.
    def enterNewline(self, ctx:exprParser.NewlineContext):
        pass

    # Exit a parse tree produced by exprParser#newline.
    def exitNewline(self, ctx:exprParser.NewlineContext):
        pass


    # Enter a parse tree produced by exprParser#compare.
    def enterCompare(self, ctx:exprParser.CompareContext):
        pass

    # Exit a parse tree produced by exprParser#compare.
    def exitCompare(self, ctx:exprParser.CompareContext):
        pass


    # Enter a parse tree produced by exprParser#bool.
    def enterBool(self, ctx:exprParser.BoolContext):
        pass

    # Exit a parse tree produced by exprParser#bool.
    def exitBool(self, ctx:exprParser.BoolContext):
        pass


    # Enter a parse tree produced by exprParser#string.
    def enterString(self, ctx:exprParser.StringContext):
        pass

    # Exit a parse tree produced by exprParser#string.
    def exitString(self, ctx:exprParser.StringContext):
        pass


    # Enter a parse tree produced by exprParser#var.
    def enterVar(self, ctx:exprParser.VarContext):
        pass

    # Exit a parse tree produced by exprParser#var.
    def exitVar(self, ctx:exprParser.VarContext):
        pass


    # Enter a parse tree produced by exprParser#logicor.
    def enterLogicor(self, ctx:exprParser.LogicorContext):
        pass

    # Exit a parse tree produced by exprParser#logicor.
    def exitLogicor(self, ctx:exprParser.LogicorContext):
        pass


    # Enter a parse tree produced by exprParser#parantheses.
    def enterParantheses(self, ctx:exprParser.ParanthesesContext):
        pass

    # Exit a parse tree produced by exprParser#parantheses.
    def exitParantheses(self, ctx:exprParser.ParanthesesContext):
        pass


    # Enter a parse tree produced by exprParser#addsub.
    def enterAddsub(self, ctx:exprParser.AddsubContext):
        pass

    # Exit a parse tree produced by exprParser#addsub.
    def exitAddsub(self, ctx:exprParser.AddsubContext):
        pass


    # Enter a parse tree produced by exprParser#assignexpr.
    def enterAssignexpr(self, ctx:exprParser.AssignexprContext):
        pass

    # Exit a parse tree produced by exprParser#assignexpr.
    def exitAssignexpr(self, ctx:exprParser.AssignexprContext):
        pass


    # Enter a parse tree produced by exprParser#float.
    def enterFloat(self, ctx:exprParser.FloatContext):
        pass

    # Exit a parse tree produced by exprParser#float.
    def exitFloat(self, ctx:exprParser.FloatContext):
        pass


    # Enter a parse tree produced by exprParser#int.
    def enterInt(self, ctx:exprParser.IntContext):
        pass

    # Exit a parse tree produced by exprParser#int.
    def exitInt(self, ctx:exprParser.IntContext):
        pass


    # Enter a parse tree produced by exprParser#muldiv.
    def enterMuldiv(self, ctx:exprParser.MuldivContext):
        pass

    # Exit a parse tree produced by exprParser#muldiv.
    def exitMuldiv(self, ctx:exprParser.MuldivContext):
        pass


    # Enter a parse tree produced by exprParser#logicand.
    def enterLogicand(self, ctx:exprParser.LogicandContext):
        pass

    # Exit a parse tree produced by exprParser#logicand.
    def exitLogicand(self, ctx:exprParser.LogicandContext):
        pass


    # Enter a parse tree produced by exprParser#stringconcat.
    def enterStringconcat(self, ctx:exprParser.StringconcatContext):
        pass

    # Exit a parse tree produced by exprParser#stringconcat.
    def exitStringconcat(self, ctx:exprParser.StringconcatContext):
        pass


    # Enter a parse tree produced by exprParser#logicnot.
    def enterLogicnot(self, ctx:exprParser.LogicnotContext):
        pass

    # Exit a parse tree produced by exprParser#logicnot.
    def exitLogicnot(self, ctx:exprParser.LogicnotContext):
        pass


    # Enter a parse tree produced by exprParser#isequal.
    def enterIsequal(self, ctx:exprParser.IsequalContext):
        pass

    # Exit a parse tree produced by exprParser#isequal.
    def exitIsequal(self, ctx:exprParser.IsequalContext):
        pass


    # Enter a parse tree produced by exprParser#unaryminus.
    def enterUnaryminus(self, ctx:exprParser.UnaryminusContext):
        pass

    # Exit a parse tree produced by exprParser#unaryminus.
    def exitUnaryminus(self, ctx:exprParser.UnaryminusContext):
        pass


    # Enter a parse tree produced by exprParser#vartype.
    def enterVartype(self, ctx:exprParser.VartypeContext):
        pass

    # Exit a parse tree produced by exprParser#vartype.
    def exitVartype(self, ctx:exprParser.VartypeContext):
        pass


    # Enter a parse tree produced by exprParser#decl.
    def enterDecl(self, ctx:exprParser.DeclContext):
        pass

    # Exit a parse tree produced by exprParser#decl.
    def exitDecl(self, ctx:exprParser.DeclContext):
        pass



del exprParser