%{
/*
  COMMA, LB, RB, CHARA
*/
#include "y.tab.h"
char yylval;
%}

delim [ \t\n]
ws {delim}+
newline \n
lb \(
rb \)
chara [a-zA-Z]

%%

{ws}      { }
,         { return (COMMA); }
{lb}      { return (LB); }
{rb}      { return (RB); }
{chara}   { yylval = yytext[0]; return (CHARA); }

%%

int yywrap() {
    return 1;
}

void yyerror(char const *s) {
    fprintf(stderr, "%s\n", s);
}
