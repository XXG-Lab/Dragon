%{
    /* definitions of manifest constants
    LT, LE, EQ, NE, GT, GE,
    IF, THEN, ELSE, WHILE, ID, NUMBER, STRING, RELOP */
%}

/* regular definitions */
delim   [ \t\n]
ws      {delim}+
letter  [A-Za-z]
digit   [0-9]
id      ({letter}|_)({letter}|{digit}|_)*
number  {digit}+(\.{digit}+)?(E[+-]?{digit}+)?
string  "([^\\"]|\\\\|\\")*"

%%

{ws}     {/* no action and no return */}
if       {return(IF);}
then     {return(THEN);}
else     {return(ELSE);}
while    {return(WHILE);}
{id}     {yylval = (int) installID(); return(ID);}
{number} {yylval = (int) installNum(); return(NUM);}
{string} {yylval = (int) installString(); return(STRING);}
"<"      {yylval = LT; return(RELOP);}
"<="     {yylval = LE; return(RELOP);}
"=="     {yylval = EQ; return(RELOP);}
"!="     {yylval = NE; return(RELOP);}
">"      {yylval = GT; return(RELOP);}
">="     {yylval = GE; return(RELOP);}

%%

int installID() {
}

int installNum() {
}

int installString() {
}
