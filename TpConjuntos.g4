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
    | setFunction
    ;

setElement:
      'set[' n_start=NUMBER n_end=NUMBER n_step=NUMBER ']'
    | 'set[' n_start=NUMBER n_end=NUMBER ']'
    | VARNAME
    ;

setFunction:
      setBelongs
    | setElementSum
    | setElementAverage
    | setLength
    | setIntersection
    | setUnion
    | setDifference
    | setComplement
    ;

setBelongs:
    s_name=VARNAME '.belongs(' n_belongs=NUMBER ')'
    ;

setElementSum:
    s_name=VARNAME '.elementSum()'
    ;

setElementAverage:
    s_name=VARNAME '.elementAvg()'
    ;

setLength:
    s_name=VARNAME '.length()'
    ;

setIntersection:
    s_name=VARNAME '.intersection(' s_comp_name=VARNAME ')'
    ;

setUnion:
    s_name=VARNAME '.union(' s_comp_name=VARNAME ')'
    ;

setDifference:
    s_name=VARNAME '.difference(' s_comp_name=VARNAME ')'
    ;

setComplement:
    s_name=VARNAME '.complement(' s_comp_name=VARNAME ')'
    ;

assignStatement:
      VARNAME '=' expression
    | VARNAME '=' setElement
    | VARNAME '=' setFunction
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
      term
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