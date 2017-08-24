package main

import (
	"fmt"
)

func twoSum(nums []int, target int) []int {
    for i, x := range nums {
		diff := target - x
		for j, y := range nums {
			if diff == y && i != j {
				return []int{i, j}
			}
		}
	}

	return []int{-1, -1}
}

func main() {
	nums := []int{3, 2, 4}
	fmt.Println(twoSum(nums, 6))
}