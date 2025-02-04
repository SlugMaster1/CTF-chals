#include <stdio.h>
#include <stdint.h>
#include <string.h>

// Function to XOR a value with a 4-byte key
void xor(uint8_t *value, uint8_t *key, size_t len) {
    for (size_t i = 0; i < len; i++) {
        value[i] ^= key[i % 4];
    }
}

// Function to compare two byte arrays
int compare_values(uint8_t *value1, uint8_t *value2, size_t len) {
    return memcmp(value1, value2, len) == 0;
}

int main() {
    // Buffer to store the user input
    char input[256];

    // Prompt the user for input
    printf("I dropped my flag somewhere! Can you find it for me?\n");
    fgets(input, sizeof(input), stdin);

    // Remove the newline character from input
    input[strcspn(input, "\n")] = '\0';

    // Length of the user input
    size_t len = strlen(input);
    uint8_t flag_enc[] = {0x73,0x70,0x70,0x63,0x77,0x48,0x04,0x7f,0x05,0x04,0x6c,0x40,0x05,0x40,0x5d,0x43,0x6e,0x40,0x03,0x68,0x79,0x07,0x41,0x73,0x4c};

    // Convert the user input to a byte array
    uint8_t value[len];
    memcpy(value, input, len);

    // 4-byte key
    uint8_t key[] = {0x31,0x33,0x33,0x37};

    // XOR the value with the key
    xor(value, key, len);

    // Compare the XORed value with the known value
    if (memcmp(value, flag_enc, 25) == 0) {
        printf("There it is!\n");
    } else {
        printf("Hmmm... No that isn't right at all.\n");
    }

    return 0;
}
