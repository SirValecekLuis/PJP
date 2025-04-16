grammar expr;

prog: stat+;

stat
    : decl                           # declar
    | ID '=' expr (NEWLINE)?            # assign
    | expr (NEWLINE)?                   # printvar
    | 'read' ID (',' ID)*            # read
    | 'write' expr (',' expr)*       # write
    | 'while' '(' expr ')' '{' stat+ '}'   # while
    | 'if' '(' expr ')' '{' stat+ '}' ('else' '{' stat+ '}')? # ifstatement
    | '{' stat+ '}'                  # multistatement
    | ID '<<' expr ('<<' expr)* (NEWLINE)?  # filewrite
    | NEWLINE                        # newline
    ;

expr
    : <assoc=right> ID '=' expr      # assignexpr
    | '-' expr                       # unaryminus
    | '!' expr                       # logicnot
    | expr ('*'|'/'|'%') expr        # muldiv
    | expr ('+'|'-') expr            # addsub
    | expr '.' expr                  # stringconcat
    | expr ('<'|'>') expr            # compare
    | expr ('=='|'!=') expr          # isequal
    | expr '&&' expr                 # logicand
    | expr '||' expr                 # logicor
    | FILE                          # file
    | INT                           # int
    | FLOAT                         # float
    | BOOL                          # bool
    | STRING                        # string
    | ID                            # var
    | '(' expr ')'                  # parantheses
    ;


vartype: 'int' | 'float' | 'bool' | 'string' | 'file';
decl: vartype ID (',' ID)* ('=' expr)? (NEWLINE)?;

BOOL   : 'true' | 'false' ;
ID     : [a-zA-Z][a-zA-Z0-9]* ;
INT    : [0-9]+ ;
FLOAT  : [0-9]+ '.' [0-9]+ ;
STRING : '"' .*? '"' ;
FILE   : STRING;
NEWLINE: '\r'? '\n' ;
WS     : [ \t]+ -> skip ;
