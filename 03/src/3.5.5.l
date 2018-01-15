%{
    #define SELECT 0
    #define FROM   1
    #define WHERE  2
    #define ID     3

    int yylval;
    void str2lower(char *);
    int installID();
%}

delim  [ \t\n]
ws     {delim}+
select [sS][eE][lL][eE][cC][tT]
from   [fF][rR][oO][mM]
where  [wW][hH][eE][rR][eE]

letter [a-zA-Z]
digit  [0-9]
id     {letter}({letter}|{digit})*

%%

{ws}      { }
{select}  { return(SELECT); }
{from}    { return(FROM); }
{where}   { return(WHERE); }
{id}      { str2lower(yytext); yylval = (int) installID(); return(ID); }

%%

void str2lower(char* text) {
    while (*text) {
        *text = toupper(*text);
        ++text;
    }
}

int installID() {
}

int yywrap() {
    return 1;
}

int main() {
    yylex();
    return 0;
}
