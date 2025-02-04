package main

import (
    "bytes"
    "encoding/hex"
    "crypto/sha256"
    "fmt"
)

func padBytes(a, b []byte) ([]byte, []byte) {
    // Pad the shorter byte slice with null bytes
    if len(a) < len(b) {
        a = append(a, make([]byte, len(b)-len(a))...)
    } else if len(b) < len(a) {
        b = append(b, make([]byte, len(a)-len(b))...)
    }
    return a, b
}

func xorBytes(a, b []byte) []byte {
    // XOR two byte slices
    a, b = padBytes(a, b)
    length := len(a)
    if len(b) < length {
        length = len(b)
    }
    result := make([]byte, length)
    for i := 0; i < length; i++ {
        result[i] = a[i] ^ b[i]
    }
    return result
}

func main() {
    // Prompt the user for input
    fmt.Print("       ,-'''''-.:-^-._            _,-^-;,-'''''-.\n      /      '  ( `  _\\          /_  ` )  `      \\\n      \\      \\   _ .,-'          `-., _,  ;      /\n       )_\\-._-._((_(                )_))_,-_,-/_(\n")
    fmt.Print("I'm Hungry! Feed me a flag: ")
    ciphertext, _ := hex.DecodeString("df7e37fae9835f8ce5a74cfca4b21f846274d39b264308ee3ec776f03acd3eb859b78e7e0286a9a9080b431acc68829532c7b0056b59ce491ed71f1edd86d4ff7b78076b88fdd662220ac6a578ce2cf627925d893d3f53b6bdb6fa297d4afa84d1a2")
    var input string
    fmt.Scanln(&input)

    // Initialize the xorAccumulator
    xorAccumulator := []byte{}

    for i := 0; i < len(input); i++ {
        // Convert current character to byte
        charByte := []byte{input[i]}
        
        // Compute SHA-256 hash
        hash := sha256.Sum256(append(xorAccumulator, charByte...))
        // XOR the hash with the accumulator
        if i < len(xorAccumulator) {
            xorAccumulator = append(xorAccumulator[:i*2], xorBytes(xorAccumulator[i*2:], hash[:])...)
        } else {
            xorAccumulator = xorBytes(xorAccumulator, hash[:])
        }
    }
    if bytes.Equal(xorAccumulator, ciphertext) {
        fmt.Println("YUM!")
    } else {
        fmt.Println("EW! That's not a flag!")
    }
}
