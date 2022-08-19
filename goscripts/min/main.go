package main

import "fmt"

type Book struct{
	Title string
	Author string
}

func min(numbers []int){
	min := numbers[0]

	for i :=1; i<len(numbers); i++{
		if numbers[i] < min{
			min = numbers[i]
		}
	}
fmt.Println(min)
}

func max(numbers []int){
	max := numbers[0]

	for i :=1; i<len(numbers); i++{
		if numbers[i] > max{
			max = numbers[i]
		}
	}
fmt.Println(max)
}



func main(){
	numbers := []int {20, 32, 13, 4, 20, 0, -1, 43}
	min(numbers)
	max(numbers)
	
	book1 := Book{ "Lucky's Life", "Lucky Ebere"}
	book2 := Book{ "Lucky's Life", "Lucky Ebere"}

	fmt.Println(book1==book2)
}

