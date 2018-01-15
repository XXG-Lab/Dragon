%{
/*
  AND, OR, NOT, LB, RB, TRUE, FALSE, NEWLINE
*/
#include "y.tab.h"
int yylval;
%}

delim [ \t]
ws {delim}+
newline \n
lb \(
rb \)

%%

{ws}      { }
{newline} { return (NEWLINE); }
and       { return (AND); }
or        { return (OR); }
not       { return (NOT); }
{lb}      { return (LB); }
{rb}      { return (RB); }
true      { yylval = 1; return (TRUE); }
false     { yylval = 0; return (FALSE); }

%%

int yywrap() {
    return 1;
}

void yyerror(char const *s) {
    fprintf(stderr, "%s\n", s);
}
