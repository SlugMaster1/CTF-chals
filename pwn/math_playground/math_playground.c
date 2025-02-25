#include <stdio.h>
#include <sys/personality.h>

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

int main(int argc, char **argv) {
    const int old_personality = personality(ADDR_NO_RANDOMIZE);
    if (!(old_personality & ADDR_NO_RANDOMIZE)) {
        const int new_personality = personality(ADDR_NO_RANDOMIZE); // Disable ASLR for process
        if (new_personality & ADDR_NO_RANDOMIZE) {
            execv(argv[0], argv);
        }
    }
    int choice;
    int a, b;

    setvbuf(stdout, NULL, _IONBF, 0);

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
