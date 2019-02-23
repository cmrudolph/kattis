// NAME : Almost Perfect
// URL  : https://open.kattis.com/problems/almostperfect
// =============================================================================
// Compute all factor pairs of the specified value using a division test. The
// factors are then summed and compared to the original value to determine
// which conclusion is most relevant (exact, almost, none).
// =============================================================================

package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func Factorize(v int) []int {
	cap := (int)(math.Sqrt((float64)(v))) + 1
	var factors []int

	factors = append(factors, 1)
	for i := 2; i < cap; i++ {
		if v%i == 0 {
			if v/i == i {
				// Factor is the square of the value - report it once
				factors = append(factors, i)
			} else {
				// Factors are distinct - report them both
				factors = append(factors, i, v/i)
			}
		}
	}

	return factors
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		n, _ := strconv.Atoi(line)

		factors := Factorize(n)
		sum := 0
		for _, i := range factors {
			sum += i
		}

		difference := n - sum
		if difference == 0 {
			fmt.Printf("%v perfect\n", n)
		} else if difference >= -2 && difference <= 2 {
			fmt.Printf("%v almost perfect\n", n)
		} else {
			fmt.Printf("%v not perfect\n", n)
		}
	}
}
