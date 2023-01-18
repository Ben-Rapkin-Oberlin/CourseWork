#lang racket
; Your name(s) here

(require rackunit rackunit/text-ui rackunit/gui)
(require "hw3.rkt")

;TODO 6, 9, and 10
; Tests to check for
; 1. Emplty list
; 2. wrong type for args
; 2. Empty elm
; 3. list of empty lists
; 4. structured lists
; 5. singleton list, i.e. ((x))
; 7. program state (look at notes)


;Q1
(define firsts-tests
  (test-suite
   "firsts"
    (test-equal? "empty list" (firsts '()) '())
    (test-equal? "non-list" (firsts 'a) "please provid a list" )
    ;;;;;
    (test-equal? "list of empty" (firsts (list '() '() '())) '(()()()))
    (test-equal? "normal case" (firsts (list '(1 2 3) '(4 5 6) '(7 8 9))) '(1 4 7))
    (test-equal? "singleton" (firsts (list '(1) '(4) '(7))) '(1 4 7))
    (test-equal? "struct list" (firsts '(((1 2) 3) (4 5 6) ((7) 8 9))) '((1 2) 4 (7)))
    ;;;;
   ))


(define rests-tests
  (test-suite
   "rests"
    (test-equal? "empty list"  (rests '()) "lst should be a structured list of lists with each sublist having >1 element")
    (test-equal? "non list" (rests 'a) "please provid a list" )
    ;;;;;
    (test-equal? "list of empties" (rests (list '() '() '())) "lst should be a structured list of lists with each sublist having >1 element")
    (test-equal? "normal case" (rests (list '(1 2 3) '(4 5 6) '(7 8 9))) (list '(2 3) '(5 6) '(8 9)))
    (test-equal? "singletons" (rests (list '(1) '(4) '(7))) "lst should be a structured list of lists with each sublist having >1 element")
    (test-equal? "struct list" (rests '(((1 2) 3) (4 5 6) ((7) 8 9))) (list '(3) '(5 6) '(8 9)))
    ;;;;
   ))
 
;Q2 add vectors
(define vec-add-tests
  (test-suite
   "vec-add"
    (test-equal? "empty list" (vec-add empty empty) empty)
    (test-equal? "non-lists" (vec-add 'a 'b) "please provid two lists of the same length with either with all rational-numeric or empty elements" )
    (test-equal? "list of emptys" (vec-add (list empty empty empty) (list empty empty empty)) (list empty empty empty))
    (test-equal? "normal case" (vec-add (list 1 2 3) (list 4 5 6)) (list 5 7 9))
    (test-equal? "wrong len"  (vec-add (list 1 2 3) (list 4 5 6 7)) "please provid two lists of the same length with either with all rational-numeric or empty elements")
    (test-equal? "struc list" (vec-add (list '(1) 2 3) (list 4 5 6)) "please provid two lists of the same length with either with all rational-numeric or empty elements")
    (test-equal? "singleton" (vec-add (list '(1)) (list 4)) "please provid two lists of the same length with either with all rational-numeric or empty elements")
    (test-equal? "empty elm" (vec-add (list empty 2 3) (list 4 5 6)) "please provid two lists of the same length with either with all rational-numeric or empty elements")
    (test-equal? "non-numeric" (vec-add (list 1 'a 3) (list empty 5 6)) "please provid two lists of the same length with either with all rational-numeric or empty elements")
   ))

;Q3 dot product
(define dot-product-tests
  (test-suite
   "dot-product"
   (test-equal? "empty list" (dot-product '() '()) 0)
   (test-equal? "non-lists" (dot-product 'a 'b) "please provid two lists of the same length with either with all rational-numeric or empty elements")
   (test-equal? "list of emptys" (dot-product (list empty empty) (list empty empty)) 0)
    (test-equal? "normal case" (dot-product (list 1 2 3) (list 4 5 6)) 32)
    (test-equal? "wrong len"  (dot-product (list 1 2 3) (list 4 5 6 7)) "please provid two lists of the same length with either with all rational-numeric or empty elements")
    (test-equal? "struc list" (dot-product (list '(1) 2 3) (list 4 5 6)) "please provid two lists of the same length with either with all rational-numeric or empty elements")
    (test-equal? "singleton" (dot-product (list '(1)) (list 4)) "please provid two lists of the same length with either with all rational-numeric or empty elements")
    (test-equal? "empty elm" (dot-product (list empty 2 3) (list 4 5 6)) "please provid two lists of the same length with either with all rational-numeric or empty elements")
    (test-equal? "non-numeric" (dot-product (list 1 'a 3) (list 2 5 6)) "please provid two lists of the same length with either with all rational-numeric or empty elements")
    ))
;Q4 repeated dot product
(define mat-vec-mul-tests
  (test-suite
   "mat-vec-mul"
    (test-equal? "empty list" (mat-vec-mul '() '()) 0)
    (test-equal? "non-lists" (mat-vec-mul 'a '())  "matrix and/or vector not valid" )
    (test-equal? "list of empties" (mat-vec-mul (list (list empty empty)(list empty empty)) (list empty empty)) (list 0 0))
    (test-equal? "normal case" (mat-vec-mul (list (list 1 2 3) (list 4 5 6) (list 7 8 9)) (list 1 2 3)) (list 14 32 50))
    (test-equal? "wrong len"  (mat-vec-mul (list (list 1 2 3) (list 4 5 6) (list 7 8 9)) (list 1 2 3 4))  "matrix and/or vector not valid")
    (test-equal? "wrong len2"  (mat-vec-mul (list (list 1 2 3) (list 4 5 6 5) (list 7 8 9)) (list 1 2 3))  "matrix and/or vector not valid")
    (test-equal? "struc vector" (mat-vec-mul (list (list '(1) 2 3) (list 4 5 6) (list 7 8 9)) (list 1 2 3))  "matrix and/or vector not valid")
    (test-equal? "singleton" (mat-vec-mul (list (list '(1)) (list 4) (list 7)) (list 1))  "matrix and/or vector not valid")
    (test-equal? "empty elm" (mat-vec-mul (list (list empty 2 3) (list 4 5 6) (list 7 8 9)) (list 1 2 3))  "matrix and/or vector not valid")
    (test-equal? "non-numeric" (mat-vec-mul (list (list 1 'a 3) (list 4 5 6) (list 7 8 9)) (list 1 2 3))  "matrix and/or vector not valid")
    (test-equal? "non-numeric2" (mat-vec-mul (list (list 1 2 3) (list 4 5 6) (list 7 8 9)) (list 1 'a 3))  "matrix and/or vector not valid")
   ))

;Q5 matrix transpose
(define transpose-tests
  (test-suite
   "transpose"
    (test-equal? "empty list" (transpose (list (list empty))) '((())))
    (test-equal? "non-lists" (transpose 'a) "matrix not valid" )
    (test-equal? "list of emptys" (transpose (list (list empty) (list empty))) (list (list empty empty)))
    (test-equal? "normal case" (transpose (list (list 1 2 3) (list 4 5 6) (list 7 8 9))) (list (list 1 4 7) (list 2 5 8) (list 3 6 9)))
    (test-equal? "wrong len"  (transpose (list (list 1 2 3) (list 4 5 6 5) (list 7 8 9))) "matrix not valid")
    (test-equal? "struc list" (transpose (list (list '(1) 2 3) (list 4 5 6) (list 7 8 9))) "matrix not valid")
    (test-equal? "singleton" (transpose (list (list '(1)) (list 4) (list 7))) "matrix not valid")
    ;(test-equal? "empty elm" (transpose (list (list empty 2 3) (list 4 5 6) (list 7 8 9))) (list (list empty 4 7) (list 2 5 8) (list 3 6 9)))
    (test-equal? "non-numeric" (transpose (list (list 1 'a 3) (list 4 5 6) (list 7 8 9)))  "matrix not valid")
   ))

;Q6 matrix multiplication
; review this test set

(define mat-mat-mul-tests
  (test-suite
    "mat-mat-mul"
      (test-equal? "empty list" (mat-mat-mul '() '()) '())
      (test-equal? "non-lists" (mat-mat-mul 'a '()) "matrix 1 and/or 2 are invalid" )
      (test-equal? "list of emptys" (mat-mat-mul '(empty empty) '((empty empty))) "matrix 1 and/or 2 are invalid")
      (test-equal? "normal case" (mat-mat-mul '((1 0 1) (2 1 1)) '((1 2) (1 0) (1 1))) '((2 3) (4 5)))
      (test-equal? "wrong len"  (mat-mat-mul (list (list 1 2 3) (list 4 5 6 5) (list 7 8 9)) (list (list 1 2 3) (list 4 5 6) (list 7 8 9))) "matrix 1 and/or 2 are invalid")
      (test-equal? "wrong len2"  (mat-mat-mul (list (list 1 2 3) (list 4 5 6) (list 7 8 9)) (list (list 1 2 3) (list 4 5 6 5) (list 7 8 9))) "matrix 1 and/or 2 are invalid")
      (test-equal? "struc list" (mat-mat-mul (list (list '(1) 2 3) (list 4 5 6) (list 7 8 9)) (list (list 1 2 3) (list 4 5 6) (list 7 8 9))) "matrix 1 and/or 2 are invalid")
      (test-equal? "singleton" (mat-mat-mul (list (list '(1)) (list 4) (list 7)) (list (list 1) (list 4))) "matrix 1 and/or 2 are invalid")
      ))
 
;Q7 flatten lst
(define flatten-tests
  (test-suite
   "flatten"
    (test-equal? "empty list" (flatten '()) '() )
    (test-equal? "non-lists" (flatten 'a) "please provide a list" )
    (test-equal? "list of emptys" (flatten (list (list empty) (list empty))) (list empty empty))
    (test-equal? "normal case" (flatten (list (list 1 2 3) (list 4 5 6) (list 7 8 9))) (list 1 2 3 4 5 6 7 8 9))
    (test-equal? "singleton" (flatten (list (list '(1)) (list 4) (list 7))) (list 1 4 7))
    (test-equal? "empty elm" (flatten (list (list empty 2 3) (list 4 5 6) (list 7 8 9))) (list empty 2 3 4 5 6 7 8 9))
    (test-equal? "non-numeric" (flatten (list (list 1 'a 3) (list 4 5 6) (list 'b 8 9))) (list 1 'a 3 4 5 6 'b 8 9))
  ))

;Q8 sum of lst
(define sum-tests
  (test-suite
   "sum"
    (test-equal? "empty list" (sum '()) "please provide a list of rational numbers")
    (test-equal? "non-lists" (sum 'a) "please provide a list" )
    (test-equal? "list of emptys" (sum (list empty empty)) "please provide a list of rational numbers")
    (test-equal? "normal case" (sum (list 1 2 3 4 5 6 7 8 9)) 45)
    (test-equal? "singleton" (sum (list '(1))) 1)
    (test-equal? "empty elm" (sum (list empty 2 3 4 5 6 7 8 9)) "please provide a list of rational numbers")
    (test-equal? "non-numeric" (sum (list 1 'a 3 4 5 6 7 8 9)) "please provide a list of rational numbers")
    (test-equal? "struct" (sum '((1 (2)) (((4))) 5)) 12) "please provide a list of rational numbers")
   )


;Q9 map in place
(define gen-map-tests
  (test-suite
    "gen-map"
      (test-equal? "empty list" (gen-map empty? '()) '())
      (test-equal? "non-lists" (gen-map empty? 'a) "please provide a list" )
      (test-equal? "list of emptys" (gen-map empty? (list empty empty)) (list #t #t))
      (test-equal? "normal case flat" (gen-map empty? (list 1 2 3 4 5 6 7 8 9)) (list #f #f #f #f #f #f #f #f #f))
      (test-equal? "normal case nested" (gen-map empty? (list (list 1 2 3) (list 4 5 6) (list 7 8 9))) (list (list #f #f #f) (list #f #f #f) (list #f #f #f)))
      (test-equal? "singleton" (gen-map empty? (list '((1)))) '((#f)))
      (test-equal? "empty elm" (gen-map empty? (list empty 2 3 4 5 6 7 8 9)) (list #t #f #f #f #f #f #f #f #f))
      ;no test for func error 
    ))


(define element-of?-tests
  (test-suite
    "element-of?"
      (test-equal? "empty list" (element-of? 1 '()) #f)
      (test-equal? "empty list2" (element-of? '() '()) #t)
      (test-equal? "non-lists" (element-of? 1 'a) "please provide a list" )
      (test-equal? "list of emptys" (element-of? empty (list empty empty)) #t)
      (test-equal? "normal case flat" (element-of? 1 (list 1 2 3 4 5 6 7 8 9)) #t)
      (test-equal? "normal case nested" (element-of? 1 (list (list 1 2 3) (list 4 5 6) (list 7 8 9))) #t)
      (test-equal? "singleton" (element-of? '(1) '((1))) #t)
      (test-equal? "empty elm" (element-of? empty (list empty 2 3 4 5 6 7 8 9)) #t)
      (test-equal? "non-numeric" (element-of? 'a (list 1 'a 3 4 5 6 7 8 9)) #t)
      (test-equal? "struct" (element-of? '(1 (2)) '((1 (2)) (((4))) 5)) #t)
    ))


(define all-tests
  (test-suite
   "All tests"
   firsts-tests
   rests-tests
   vec-add-tests
   dot-product-tests
   mat-vec-mul-tests
   transpose-tests
   mat-mat-mul-tests
   flatten-tests
   sum-tests
   gen-map-tests
   element-of?-tests
    ))
    

(run-tests all-tests)
