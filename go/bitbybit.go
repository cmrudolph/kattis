// https://open.kattis.com/problems/bitbybit

// OK: Read and process each instruction, modifying the bits as we go.

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const BitCount = 32
const Unknown = -1

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		instructions, _ := strconv.Atoi(line)

		if instructions == 0 {
			break
		}

		var buf [BitCount]int
		for i := 0; i < BitCount; i++ {
			buf[i] = Unknown
		}

		for i := 0; i < instructions; i++ {
			scanner.Scan()
			line := scanner.Text()
			splits := strings.Fields(line)
			instruction := splits[0]

			switch instruction {
			case "SET":
				// Obvious: Force the bit to 1
				bit, _ := strconv.Atoi(splits[1])
				buf[bit] = 1
			case "CLEAR":
				// Obvious: Force the bit to 0
				bit, _ := strconv.Atoi(splits[1])
				buf[bit] = 0
			case "AND":
				idx1, _ := strconv.Atoi(splits[1])
				idx2, _ := strconv.Atoi(splits[2])
				if buf[idx1] == 0 || buf[idx2] == 0 {
					// Either value is 0: AND must be 0
					buf[idx1] = 0
				} else if buf[idx1] == 1 && buf[idx2] == 1 {
					// Both values are 1: AND must be 1
					buf[idx1] = 1
				} else {
					// Ambiguous
					buf[idx1] = Unknown
				}
			case "OR":
				idx1, _ := strconv.Atoi(splits[1])
				idx2, _ := strconv.Atoi(splits[2])
				if buf[idx1] == 1 || buf[idx2] == 1 {
					// Either value is 1: OR must be 1
					buf[idx1] = 1
				} else if buf[idx1] == 0 && buf[idx2] == 0 {
					// Both values are 0: OR must be 0
					buf[idx1] = 0
				} else {
					// Ambiguous
					buf[idx1] = Unknown
				}
			}
		}

		// Walk the array in reverse order (we have been storing things in the
		// natural order for an array - zero = MSB)
		for i := BitCount - 1; i >= 0; i-- {
			toPrint := strconv.Itoa(buf[i])
			if buf[i] == Unknown {
				toPrint = "?"
			}
			fmt.Printf("%v", toPrint)
		}
		fmt.Printf("\n")
	}
}
