Ben Rapkin
## Overview Questions

- What are the strengths and weaknesses of your language?
    Go is an incredibly intresting langauge for multiple reasons. Firstly is that it has great local type deduction built into the compiler. This allows for simple programs to feel like their dynamically typed
    while provinding the speed and lower overhead of static langauges. This makes the code very fast to type and fast to run, a win win. That being said, it is still generally a good deal slower than rust or C. This can be overcome as all three compile to the same LLVM, however, GO is not designed to compete with these incredibly performant system langauges. It can, but the process to disable things like bounds checking are not intuitive and really not meant to be used for standard cases. Additionally, Go is still young and doesn't have all the features that a large competeter like java does. That being said, it has great built in concerancy methods that make optimizing code on large processers much easier than in other langagues


- For what type(s) of problems/domains is it particularly well suited?
    Go is best suited for server-side programing and that's what it has been largley advertised for. It is quick to write and develope, often faster than Java, and as great multithreading/multicore processes built in, meaning they are far easier to addapt to modern computer archetecture than other langauges, futher cutting down development time

- Other than functional, what other paradigm(s) would the language fall under?
    The code also falls under the paradigms of imperative and object oriented. That being said, they don't have some of the common tools associated with OOP like inheritance, but they can achieve all the same functionallity with things like emmbedding. It just looks fairly diffrent.



## Language Properties

- Are there restrictions on mutation?
    Yes, Go unlike other langagues actually incentives code with mutation.
    The "const" key word which denotes an Final/unchange varible is only applicable to primiatives. You cannot use it when the initilization value is a varible, even if that varible also evaluates to a primative
    https://jesseduffield.com/Gos-Shortcomings-4/

- Are functions first class?
    Yes. The following is perfectly valid (import not included):
    https://go.dev/play/p/Xm_ihamhlEv
    func main() {
	    a := func() {
		    fmt.Println("hello world first class function")
	    }
	    a()
	    fmt.Printf("%T", a)
    }

- What sort of control flow constructs does the language have?
    Golang has all of the standard flow control statments that one would expect of a more modern langauge, however, it is a little less progressive than one might expect in that regards. It has if/else but not elif or the terniary opperator. Additionally, there are switch statments but also goto statments which personally came as a big suprise! It seems that most everyone agrees gotos should be abstracted away and left for compilers to deal with. It has recursions as expected and due to its use a a multithreading software, a variety of wait statments. 

- Is the language statically or dynamically typed?
  The program is Statically typed, however, it often can feel dynamically typed as we can allow the compiler to infer type at compile time by using the := operator. Ex.
    int a = 1
    a := 1

  That being said, you cannot change types, the following is invalid:
    a := 1
    a :="1"

- Is there support for type inference?
    Yes, this is one of the most popular parts via the := opperator. Please refer to above for an example

- What are the core abstractions or features of the language that make it unique? Define and explain those features, especially if they are concepts that are not also present in languages we've discussed in class.
  One of the more unique aspects of golang's abstractions is that generics are very new to the program's base code. For a long time they weren't inculded and so other tools were needed to allow for more flexable programing schemes, notably among these mechanisms is interfaces. Where generics allow for a langauge to make functions that can handle objects with similar feilds or methods, interfaces allow for programers to write a series of fucntions for each case and then write a larger function that calles the smaller ones based on the type of the input. Sort of like a case/switch statments but with more/less (depending on if your reading or writting the code) boilerplate required. Additionally, the langauge doesn't have the same class keyword which allows abstraction/encapsulation of feilds and methods, instead one must uses structs and interfeaces among other methods

- What is difficulty about learning to use this language?
    Go is designed around concurrency. It implements this mechanism in an incredibly improved manner in regards to something like C/C++ or Java, however, it is still concurrency and there is a lot to learn about the system. Additionally, while they do support OOP, there mechanisms are fairly different from standard implmentations, which, while nice once you've learned them, can provide a bit of a steep learning curve. Finally, Go is meant to by user friendly and easy to just start coding, this means a lot is hidden under the hood and things like directly allocating and/or freeing memory is much harder than in C/C++ or Rust because they assume that for the most part you want the Garbage colletor if coding

- What form does the programmer interaction take (compiled/interpreter, virtual machine, interaction shell, work from files, etc.)?
    Go is a compiled langauge, initially being coded in C++ but now it is self hosted. This is part of why it preforms generally faster than Java. Of course, this means that binaries must be compiled for each diffrenet opperating system and some small changes may need to be made. That being said, Go was made with cross-platform compilation in mind, and so it has a number of built in tools which allow code to be generallized for any opperting system.


## Taxonomy/Classification
Should be similar to the Functional Language of the week slide

- What is the history of the language? When was it developed and by whom?
  Go was developed in 2007 with Robert Griesemer, Rob Pike, and Ken Thompson as the main leads. It was created at google to address the difficulty of coding in C++ while keeping the runtime efficeny. 

- What other programming languages is the language related to, if any?
    It is related to python by design. By use of the := opperator to infer types, many simple programs can be written without explicit typing at all, making it feel almost dynamic. Additionally, you can compile and run the code in one short command, further making it feel like a scripting langauge.

- What uses does the language have today (and if it is not used today, why not)?
    The most representative use case is server side programing. The langauge is designed to provide much more simple concerncy methods than its cheif competitor java while also being faster to run!


## Original Code

    Please see examples.go
    Run via <go run examples.go> or <go run .>


## Citations

https://go.dev/play/p/Xm_ihamhlEv

https://golangbot.com/inheritance/

https://en.wikipedia.org/wiki/Go_(programming_language)

https://go.dev/doc/tutorial

https://jesseduffield.com/Gos-Shortcomings-4/

https://www.digitalocean.com/community/tutorials/uilding-go-applications-for-different-operating-systems-and-architectures

https://go101.org/article/control-flows.html

https://pkg.go.dev/fmt#Scanf

https://stackoverflow.com/questions/45171642/how-is-the-empty-interface-different-than-a-generic

https://www.tutorialspoint.com/go/go_goto_statement.htm
