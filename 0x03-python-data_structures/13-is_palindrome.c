#include <stdio.h>
#include <stdlib.h>
void push(int **stack, int *top, int value) {
    (*top)++;
    (*stack)[*top] = value;
}

/* Function to pop a value from the stack */
int pop(int **stack, int *top) {
    int value = (*stack)[*top];
    (*top)--;
    return value;
}
int is_palindrome(struct ListNode **head) {
    struct ListNode *current = *head;
    int *stack = NULL;
    int top = -1;
    int is_palindrome = 1; // Assume palindrome initially

    // Traverse the linked list and push each element onto the stack
    while (current != NULL) {
        push(&stack, &top, current->val);
        current = current->next;
    }

    // Traverse the linked list again and compare each element with the popped elements from the stack
    current = *head;
    while (current != NULL) {
        int stack_value = pop(&stack, &top);
        if (current->val != stack_value) {
            is_palindrome = 0;
            break;
        }
        current = current->next;
    }

    // Free the dynamically allocated stack memory
    free(stack);

    return is_palindrome;
}
