package main

import "fmt"

func reverse(x int) int {
	is_minus := false
	acc := 0

	if x < 0 {
		is_minus = true
		x = -x
	}

	for x > 0 {
		rem := x % 10
		x = x / 10
		acc = acc*10 + rem
	}

	if is_minus {
		acc = -acc
	}

	if acc > 1<<31-1 || acc < -1<<31 {
		return 0
	}

	return acc
}

func main() {
	result := reverse(15342364)
	fmt.Println(result)
}
