// What is the longest sequence of primes that add to a prime below 1,000,000.
package main

import (
	"fmt"
	"math"
)

const N = 1000000

var primes []int

func init() {
	for i := 2; i <= N; i++ {
		primes = append(primes, i)
	}
	fmt.Println("sieving")
	cutoff := int(math.Ceil(math.Sqrt(N)))
	for i := 0; primes[i] <= cutoff; i++ {
		var next []int
		p := primes[i]
		for _, n := range primes {
			if n == p || n%p != 0 {
				next = append(next, n)
			}
		}
		primes = next
	}
}

func bsearch(n int, list []int) bool {
	lo, hi := 0, len(list)
	for lo < hi {
		i := lo + (hi-lo)/2
		if list[i] == n {
			return true
		}
		if n < list[i] {
			hi = i
		} else {
			lo = i + 1
		}

	}
	return false
}

type result struct {
	len    int
	total  int
	primes []int
}

var c = make(chan result)

func main() {
	go search()
	var best result
	for r := range c {
		if r.len > best.len {
			best = r
		}
	}
	fmt.Println(best.total, "is the sum of", best.len, "consecutive primes")
	// 997651
}

func search() {
	fmt.Println("searching")
	for i := range primes {
		t := primes[i]
		for j := i + 1; j < len(primes); j++ {
			if t >= N {
				break
			}
			if bsearch(t, primes) {
				c <- result{j - i, t, primes[i:j]}
			}
			t += primes[j]
		}
	}
	close(c)
}
