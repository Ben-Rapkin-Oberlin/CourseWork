
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int size = 0;
int index = 0; 
struct tree
{
    struct tree *left;
    struct tree *right;
    struct tree *parent;
    int data;
};
typedef struct tree tree;

tree *original;

// A utility function to create a node
tree *newNode(int data)
{
    tree *temp = (tree *)malloc(sizeof(tree));

    temp->data = data;
    temp->left = temp->right = temp->parent = NULL;
    return temp;
}
tree *newL(int data, tree *father)
{
    tree *temp = (tree *)malloc(sizeof(tree));

    temp->data = data;
    temp->parent = father;
    temp->left = temp->right = NULL;
    father->left = temp;
    return temp;
}
tree *newR(int data, tree *father)
{
    tree *temp = (tree *)malloc(sizeof(tree));

    temp->data = data;
    temp->parent = father;
    temp->left = temp->right = NULL;
    father->right = temp;
    return temp;
}

char * getb(){
    index=0;
    char *a[20];
    for (int i=0; i<20;i++){
        a[i]=(char) -1;
    }
    FILE *f=fopen("workHorse.c","w");
    fseek(f,20,SEEK_END);
    char c=(char)fgetc(f);
    while (c!=EOF){
        if (c=='\n'){
            for (int i=0; i<20;i++){
                a[i]=(char) -1;
            }
            index=0;
        }
        else{
            a[index]=c;
            index++;
        }
    }
    char * b[index];
    int count=0;
    while (a[count]!=(char)-1){
        b[count]=a[count];
        count++;
    }
    return b;
}
    
tree *buildleft(tree *current, int *order)
{
    if (current->data == -2)
    {
        while (order[index + 1] == -2)
        {
            current = newL(order[index + 1], current);
            index++;
        }
        // reached leaf of left path
        current = newL(order[index + 1], current);
        index++;
    
        return current;
    }

    else
    {
        return current;
    }
}

tree *buildTree(tree *current, int *order)
{
//    tree *original = newNode(0);
//    original = current;

    if (index >= size)
        return current;

    // finish last node on left which is a leaf
    current = buildleft(current, order);
    // now on to right child
    // we know that this is the bottom
    //  adds a righ brother to left, change our pointer to that
    current = current->parent;
    current = newR(order[index + 1], current);
    index++;
    if (current->data != -2)
    {
        while (current->parent->right)
        {
            // go up until the parent has no right child
            current = current->parent;
            if (current==original){
                return current;
            }
        }
        // go up to that parent, go to
        current = current->parent;
        current = newR(order[index + 1], current);
        index++;
        current = buildTree(current, order);
    }
    else
    {
        current = buildTree(current, order);
    }
    while (current->parent)
    {
        current = current->parent;
    }
    return current;
}

//#############################################################
//#############################################################
//#############################################################
//this function came from https://www.geeksforgeeks.org/level-order-tree-traversal/
/* Function prototypes */
void printCurrentLevel(tree *root, int level);
int height(tree *node);
tree *newNode(int data);

/* Function to print level order traversal a tree*/
void printLevelOrder(tree *root)
{
    int h = height(root);
    int i;
    for (i = 1; i <= h; i++)
    {
        printCurrentLevel(root, i);
        printf("\n");
    }
}

/* Print nodes at a current level */
void printCurrentLevel(tree *root, int level)
{
    if (root == NULL)
        return;
    if (level == 1)
        printf("%d ", root->data);
    else if (level > 1)
    {
        printCurrentLevel(root->left, level - 1);
        printCurrentLevel(root->right, level - 1);
    }
}

/* Compute the "height" of a tree -- the number of
    nodes along the longest path from the root node
    down to the farthest leaf node.*/
int height(tree *node)
{
    if (node == NULL)
        return 0;
    else
    {
        /* compute the height of each subtree */
        int lheight = height(node->left);
        int rheight = height(node->right);

        /* use the larger one */
        if (lheight > rheight)
            return (lheight + 1);
        else
            return (rheight + 1);
    }
}

/* Helper function that allocates a new node with the
given data and NULL left and right pointers. */

/* Driver program to test above functions*/
void lvl(tree *root)
{
    /*
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
    */
    printf("Level Order traversal of binary tree is \n");
    printLevelOrder(root);
}

// Driver code
/*
tree *driver(int *pre, int size)
{
    int pre[] = { 10, 5, 1, 7, 40, 50 };
    for (int i=0; i<size; i++)
    {
        if (isalpha(pre[i]))
            printf("%c\n", (char) pre[i]);
        else{
            printf("%i\n", pre[i]);
        }
    }


    tree *root = constructTree(pre, size);

    // printf("Inorder traversal of the constructed tree: \n");
    // printInorder(root);

    return root;
}
 */
