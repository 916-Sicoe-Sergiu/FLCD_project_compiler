%{
#include <stdio.h>
%}

digit           [0-9]
nondigit        [a-z]
nonzerodigit    [1-9]

identifier      {nondigit}({nondigit}|{digit})*
int_constant    [+-]?({nonzerodigit}{digit}*|{digit}+)
string_constant \"([^\\"]|\\.)*\"
operator        [\+\-\*/%=\!<>]{1,2}
separator       [(),;\[\]{}]
reserved        int|string|read|write|if|elif|else|for|exit|max

%%

{reserved}      { printf("Reserved Word: %s\n", yytext); return 0; }
{identifier}    { printf("Identifier: %s\n", yytext); return 0; }
{int_constant}  { printf("Integer Constant: %s\n", yytext); return 0; }
{string_constant} { printf("String Constant: %s\n", yytext); return 0; }
{operator}      { printf("Operator: %s\n", yytext); return 0; }
{separator}     { printf("Separator: %s\n", yytext); return 0; }

[ \t\n]+        ;
.               { printf("Unknown character: %s\n", yytext); }

%%

int main(void)
{
    yylex(); // Start the lexer
    return 0;
}

