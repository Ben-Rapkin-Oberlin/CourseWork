//Ben Rapkin

// A version of factorial written in a style
// that you feel is representative of the 
// language.

package main

import (
	"fmt"
	"time"
	"sync"
//	"bufio"
//	"os"

)
var total int = 0

var race int = 0


var wg sync.WaitGroup
var wg2 sync.WaitGroup

func loopSingle(s,n int)  {
	result := 0
	for i := s; i <= n; i++ {
		result ++
	}
	total+=result
}

func loop(s,n int, group *sync.WaitGroup)  {
	result := 0
	for i := s; i <= n; i++ {
		result ++
	}
	defer group.Done() 
	total+=result
}



//Ex1 - Factorial
func factorial(n int) int {
	if n==0{
		return 1
	}
	return n*factorial(n-1)
}


func example2(reader int)  {
	//this example is a simple implementation of parallelism
	//in go. It compares the time it takes to run a long loop
	//using the standard single call, vs implementing it in parallel
	//using goroutines. The ratio of non-parallel/parallel time is averaged over n runs
	//and printed to stdout. rinted to s
	n:=15
	end:=1200000000
	println("Summing from 1 to ",end)
	println("averaging over ",n," runs")
	println("form of output: (Single instance Runtines)/(Parrallel Runtime)")
	println("#######################################################")
	for cores:=1;cores<=reader;cores+=2{
		if cores==3{cores=4}
		avg:=0.0
		//cores:= 2
		list := make([]int, cores+1) 
		list[0]=1
		for i:=1;i<cores+1;i++{
			list[i]=int(end/cores)*i
			//print(list[i],",")
		}
			
		for i:=0;i<n;i++{
			st:=time.Now()
			loopSingle(1,end)
			t1:=time.Since(st).Milliseconds()
			
			total=0
			st=time.Now()
			wg.Add(cores)
			for j:=0;j<cores;j++{
				go loop(list[j],list[j+1],&wg)

			}
			//os.Exit(3)
			wg.Wait()

			t2:=time.Since(st).Milliseconds()

			if t1 != 0 && t2 != 0{
				avg+=(float64(t1)/float64(t2))
			}
		}


		//fmt.Println(avg)
		fmt.Println("Go Coroutines:", cores ,"|| avg ratio: ",avg/float64(n))

	}
}

func main() {
	//to run, please use <go run examples.go> 

	//uncomment following line to run ex1: Factorial
	
	
	var i int
	var j int

	fmt.Println("Example 1, please provide a number to find the factorial of")
	fmt.Println("please keep in mind that this is not preped for overflow")
	fmt.Scanf("%d\n", &i)
	fmt.Println("Answer: ",factorial(i))
	
	//uncomment following line to run ex2: Parallelism
	fmt.Println("Example 2, Parallelism")
	fmt.Println("Please enter the max number of cores to try (1-12, !2):")
	fmt.Scanf("%d",&j)
	example2(j)
	println("\n")
	





}