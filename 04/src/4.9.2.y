%{
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

struct List {
    char val;
    struct List* next;
};

struct List* head;
struct List* tail;

struct List* createNode(char val) {
    struct List* node = (struct List*) malloc(sizeof(struct List));
    node->val = val;
    node->next = NULL;
    return node;
}

struct List* destroyNode(struct List* node) {
    struct List* next;
    while (node) {
        next = node->next;
        free(node);
        node = next;
    }
}
%}

%token COMMA LB RB CHARA

%%

S : LB L RB
  | CHARA {
            if (tail == NULL) {
                head = createNode(yylval);
                tail = head;
            } else {
                tail->next = createNode(yyval);
                tail = tail->next;
            }
        }
  ;
L : L COMMA S
  | S
  ;

%%

int main() {
    int first;
    yyparse();
    first = 1;
    putchar('(');
    tail = head;
    while (tail) {
        if (first) {
            first = 0;
        } else {
            printf(", ");
        }
        putchar(tail->val);
        tail = tail->next;
    }
    puts(")\n");
    destroyNode(head);
    return 0;
}
