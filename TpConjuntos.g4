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
    | setElement
    ;

setElement:
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

whileStatement:
      'while' booleanExpression 'do'
        (statement)+
      'done'
    ;

booleanExpression:
      operand           op=COMPARATION_OPERATOR operand
    | booleanExpression op=AND_OPERATOR booleanExpression
    | booleanExpression op=OR_OPERATOR booleanExpression
    ;

operand:
      expression
    | VARNAME
    ;

expression: 
      setElement
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
      n=NUMBER      
    | vn=VARNAME               
    | '(' expression ')'     
    ;


AND_OPERATOR : 'and';
OR_OPERATOR : 'or';
COMPARATION_OPERATOR : '=='|'<='|'>='|'<'|'>'|'!=';

VARNAME : [a-z]+;

NUMBER : DIGIT+;
DIGIT  : [0-9];
WS : [ \r\n\t] -> skip; 