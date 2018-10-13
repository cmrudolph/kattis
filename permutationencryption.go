// https://open.kattis.com/problems/permutationencryption

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		lineValues := strings.Fields(line)

		// Zero indicates 'end of input'
		if lineValues[0] == "0" {
			fmt.Fprintf(os.Stderr, "DONE\n")
			break
		}

		// First value is the length of the key
		keyLen, _ := strconv.Atoi(lineValues[0])
		fmt.Fprintf(os.Stderr, "L: %v\n", keyLen)

		// Next N integers on the line are the key values (1 <= n <= 20).
		// Make them zero-based for simpler logic.
		keyArr := make([]int, keyLen)
		for i := 0; i < keyLen; i++ {
			keyVal, _ := strconv.Atoi(lineValues[i+1])
			keyArr[i] = keyVal - 1
		}
		fmt.Fprintf(os.Stderr, "KA: %v\n", keyArr)

		scanner.Scan()
		plaintext := scanner.Text()
		plaintextLen := len(plaintext)
		ciphertext := ""

		// Loop over the input string in chunks. Within each chunk, evaluate
		// the substitutions using the key. Key values that run off the end
		// of the input string result in implict spaces (treat the input string
		// as being padded)
		for i := 0; i < plaintextLen; i += keyLen {
			for _, keyVal := range keyArr {
				var substitutionVal string = " "
				if (i + keyVal) < plaintextLen {
					// Corresponding input string value exists - use it instead of the space
					substitutionVal = string((plaintext[i+keyVal]))
				}
				ciphertext += substitutionVal
			}
		}

		fmt.Fprintf(os.Stderr, "PT: %v\n", plaintext)
		fmt.Fprintf(os.Stderr, "CT: %v\n", ciphertext)
		fmt.Printf("'%v'\n", ciphertext)
	}
}
