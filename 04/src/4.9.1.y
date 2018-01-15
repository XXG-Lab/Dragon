%{
#include <ctype.h>
#include <stdio.h>
%}

%token AND OR NOT LB RB TRUE FALSE NEWLINE

%%

lines : lines bexpr NEWLINE { if ($2) puts("true"); else puts("false"); }
      | lines NEWLINE
      |
      ;
bexpr : bexpr OR bterm { $$ = $1 || $3; }
      | bterm          { $$ = $1; }
      ;
bterm : bterm AND bfactor { $$ = $1 && $3; }
      | bfactor           { $$ = $1; }
      ;
bfactor : NOT bfactor { $$ = !$2; }
        | LB bexpr RB { $$ = $2; }
        | TRUE
        | FALSE
        ;

%%

int main() {
    yyparse();
    return 0;
}
