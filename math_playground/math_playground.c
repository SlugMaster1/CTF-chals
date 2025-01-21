#include <stdio.h>

void add(int a, int b) {
    printf("Result: %d\n", a + b);
}

void subtract(int a, int b) {
    printf("Result: %d\n", a - b);
}

void multiply(int a, int b) {
    printf("Result: %d\n", a * b);
}

void divide(int a, int b) {
    if (b != 0) {
        printf("Result: %d\n", a / b);
    } else {
        printf("Error: Division by zero\n");
    }
}

void (*operations[4])(int, int) = {add, subtract, multiply, divide};

int main() {
    int choice;
    int a, b;

    printf("Choose a function to use:\n");
    printf("0: Add\n");
    printf("1: Subtract\n");
    printf("2: Multiply\n");
    printf("3: Divide\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    printf("Enter two integers:\n");
    scanf("%d %d", &a, &b);

    (*operations[choice])(a, b);

    return 0;
}
