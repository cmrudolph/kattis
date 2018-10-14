// https://open.kattis.com/problems/almostperfect

package main

import (
    "bufio"
    "fmt"
    "os"
    "math"
    "strconv"
)

func Factorize(v int) []int {
    cap := (int)(math.Sqrt((float64)(v))) + 1
    var factors []int

    factors = append(factors, 1)
    for i := 2; i < cap; i++ {
        if v % i == 0 {
            if v / i == i {
                factors = append(factors, i)
            } else {
                factors = append(factors, i, v / i)
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
