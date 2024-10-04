#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

// MAKEUC{0k_y0u_C4n_h@v3_Y0Ur_d0G_b4Ck}
char *encrypt(char * input){
    char *encrypted = malloc(strlen(input) + 1);
    for (int i = 0; i < strlen(input); i++){
        encrypted[i] = input[i]^(char)(pow(i,2)); 
    }
    return encrypted;
}

int main() {
    printf("We have your dog, here is a picture of fido for proof: \n");
    printf(" / \\__\n");
    printf("(    @\\___\n");
    printf("/         O\n");
    printf("/   (_____/\n");
    printf("/_____/   U\n");
    printf("You know what to do\n\n");

    printf("What is the flag?\n");
    char input[100];
    fgets(input, 100, stdin);
    char flag[] = "\x30\x6a\x5b\x70\x20\x6c\x7b\x72\x74\x3f\x3b\x11\xd0\xdf\xf7\xbe\x59\x11\x11\x1b\xcf\xdd\xd4\x56\x1f\x13\x90\x9a\x7b";
    if (strlen(input) != 38){
        goto fail;
    }else if(strncmp(input,"MAKEUC{",7) || input[36] != '}'){
        goto fail;
    }else if(strncmp(encrypt(input+7),flag,29)){
        goto fail;
    }
    printf("Ok I guess you can have your dog back\n");
    return 0;
fail:
    printf("No dog for you!\n");
    return 1;
}
