
#include <stdio.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>

struct tree
{
    struct tree *left;
    struct tree *right;
    struct tree *parent;
    int data;
};
typedef struct tree tree;

tree * driver(int * pre, int size);
//void printInorder(tree * node);
void pre_order_traversal(tree* root);
char* getb();
void lvl(tree * root);
tree * buildTree(tree * current, int * order);
tree * newNode(int data);