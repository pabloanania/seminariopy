grammar TpConjuntos;

program:
    (statement)+
    ;

statement:
      expression                
    | assignStatement  
    | VARNAME                   
    | booleanExpression          
    | ifStatement
    | setExpression
    ;

setExpression:
      'set[' n_start=NUMBER n_end=NUMBER n_step=NUMBER ']'
    | 'set[' n_start=NUMBER n_end=NUMBER ']'
    ;

assignStatement:
      VARNAME '=' expression
    ;

ifStatement:
      'if' booleanExpression 
      'then ' (statement)+ 
      ('else ' (statement)+ )?
      'fi'
    
    ;

booleanExpression:
    operand COMPARATION_OPERATOR operand  
    ;

operand:
      expression
    | VARNAME
    ;

expression: 
      setExpression
    | term
    | expression '+' term   
    | expression '-' term   
    ;

term:   
    factor                    
    | term '*' factor       
    | term '/' factor       
    ;

factor: 
    NUMBER                     
    | '(' expression ')'     
    ;


COMPARATION_OPERATOR : '=='|'<='|'>='|'<'|'>'|'!=';

VARNAME : [a-z]+;

NUMBER : DIGIT+;
DIGIT  : [0-9];
WS : [ \r\n\t] -> skip; 