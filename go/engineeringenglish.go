// NAME : Engineering English
// URL  : https://open.kattis.com/problems/engineeringenglish
// =============================================================================
// Iterate over the strings in the input and use a map to store values we have
// seen before. A value's existence in the map means we need to replace it
// with our token value.
// =============================================================================

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	m := make(map[string]bool)

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		s := scanner.Text()
		words := strings.Fields(s)
		for i, f := range words {
			// Use a consistent case since the problem is case insensitive
			cased := strings.ToUpper(f)
			_, ok := m[cased]
			if ok {
				// We've seen this word before. Replace it
				words[i] = "."
			}
			m[cased] = true
		}

		fmt.Println(strings.Join(words, " "))
	}
}
