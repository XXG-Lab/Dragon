letter    [a-zA-Z]
vowel     [aeiouAEIOU]
consonant [^{vowel}]
vword     {vowel}{letter}*
cword     {letter}+

%%

{vword}   { printf("%s", yytext); printf("ay"); }
{cword}   { printf("%s", yytext + 1); putchar(yytext[0]); printf("ay"); }
.         { ECHO; }

%%

int yywrap() {
    return 1;
}

int main() {
    yylex();
    return 0;
}
