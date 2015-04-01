package main

import "fmt"

func main() {
	fmt.Printf("Enter a dollar amount ($xx.xx): ")
	var dollars, cents int
	n, err := fmt.Scanf("$%d.%02d\n", &dollars, &cents)
	for err != nil {
		fmt.Printf("Try again: ")
		n, err = fmt.Scanf("$%d.%02d", &dollars, &cents)
	}
	_ = n
	cents = dollars*100 + cents

	var coins = []int{25, 10, 5, 1}
	var singular = []string{"quarter", "dime", "nickel", "penny"}
	var plural = []string{"quarters", "dimes", "nickels", "pennies"}
	for i, d := range coins {
		q := cents / d
		cents = cents % d
		switch q {
		case 0:
		case 1:
			fmt.Println(q, singular[i])
		default:
			fmt.Println(q, plural[i])
		}
	}
}
