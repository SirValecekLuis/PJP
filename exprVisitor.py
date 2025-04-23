# Generated from expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .exprParser import exprParser
else:
    from exprParser import exprParser

# This class defines a complete generic visitor for a parse tree produced by exprParser.

class exprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by exprParser#prog.
    def visitProg(self, ctx:exprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#declar.
    def visitDeclar(self, ctx:exprParser.DeclarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#assign.
    def visitAssign(self, ctx:exprParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#printvar.
    def visitPrintvar(self, ctx:exprParser.PrintvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#read.
    def visitRead(self, ctx:exprParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#write.
    def visitWrite(self, ctx:exprParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#while.
    def visitWhile(self, ctx:exprParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#ifstatement.
    def visitIfstatement(self, ctx:exprParser.IfstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#multistatement.
    def visitMultistatement(self, ctx:exprParser.MultistatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#filewrite.
    def visitFilewrite(self, ctx:exprParser.FilewriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#emptysemicolon.
    def visitEmptysemicolon(self, ctx:exprParser.EmptysemicolonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#newline.
    def visitNewline(self, ctx:exprParser.NewlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#compare.
    def visitCompare(self, ctx:exprParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#bool.
    def visitBool(self, ctx:exprParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#string.
    def visitString(self, ctx:exprParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#var.
    def visitVar(self, ctx:exprParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#logicor.
    def visitLogicor(self, ctx:exprParser.LogicorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#parantheses.
    def visitParantheses(self, ctx:exprParser.ParanthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#addsub.
    def visitAddsub(self, ctx:exprParser.AddsubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#assignexpr.
    def visitAssignexpr(self, ctx:exprParser.AssignexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#float.
    def visitFloat(self, ctx:exprParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#int.
    def visitInt(self, ctx:exprParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#muldiv.
    def visitMuldiv(self, ctx:exprParser.MuldivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#logicand.
    def visitLogicand(self, ctx:exprParser.LogicandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#file.
    def visitFile(self, ctx:exprParser.FileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#stringconcat.
    def visitStringconcat(self, ctx:exprParser.StringconcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#logicnot.
    def visitLogicnot(self, ctx:exprParser.LogicnotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#isequal.
    def visitIsequal(self, ctx:exprParser.IsequalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#unaryminus.
    def visitUnaryminus(self, ctx:exprParser.UnaryminusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#vartype.
    def visitVartype(self, ctx:exprParser.VartypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#decl.
    def visitDecl(self, ctx:exprParser.DeclContext):
        return self.visitChildren(ctx)



del exprParser