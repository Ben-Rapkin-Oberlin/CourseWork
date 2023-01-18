;Ben
;Toby
#lang racket

(require rackunit rackunit/text-ui rackunit/gui)
(require "hw2.rkt")

;not list
;empty list
;structured list
;list of mixed elm

(define collaborators
  (list '(alex @xela)
    '(able @not-a-machine)
    '(sam @samsamsam)
    '(kiran @kiran)))

;----merge-tests----
(define merge-tests
  (test-suite
   "merge"
   (test-equal? "Odds and evens"
                (merge '(1 3 5 7 9) '(2 4 6 8 10))
                '(1 2 3 4 5 6 7 8 9 10))
   (test-equal? "Two empty lists"
                (merge null null)
                null)
   (test-equal? "structured lists"
                (merge (list '(1 2 3) (list '(4 5) '(6)) '7) '(1 2)) '(1 1 2 2 3 4 5 6 7))
   (test-equal? "non-rational" (merge '(1 2 3 a)'(4 5 6)) "please use rational numbers")
   (test-equal? "non-list" (merge '(1 2 3 a) 'a) "please provide two lists")
   (test-equal? "lst1 null"
                (merge null '(4 5 6 7)) '(4 5 6 7))
   (test-equal? "lst2 null"
                (merge '(1 2 3) null) '(1 2 3))))
   

;----sort-tests----
(define sort-tests
  (test-suite
   "sort"
   (test-equal? "Unsorted list"
                (sort '(5 1 8 3 7)) '(1 3 5 7 8))
   (test-equal? "Sorted list"
                (sort '(1 3 5 7 8)) '(1 3 5 7 8))))
    ;empty lists, structured lists, mixed types, non-list


;----has-sublist?-tests----
(define has-sublist?-tests
  (test-suite
   "has-sublist?"
   (test-equal? "non-list" (has-sublist? '(1 2 3 a) 'a) "please provide two lists")
   (test-true "mixed elmts" (has-sublist? '(a) '(1 2 3 a b 7.6 a)))
   (test-true "smol empty list" (has-sublist? empty (list 1 2 3 'a 'b 7.6 '() )))
   (test-false "big empty list" (has-sublist? (list 1 2 3 'a 'b 7.6 '() ) empty))
   (test-true "both empty list" (has-sublist? empty empty))
   (test-true "structured list" (has-sublist? (list 1 '(2)) (list '(1 2 3) (list '(4 5) '(6)) '7)))))

;----handle-tests----  
(define handle-tests
  (test-suite
    "handle"
    (test-equal? "non-list" (handle 'sam 'a) "please provide a symbol and a list")
    (test-equal? "non-symbol" (handle "sam" '(1 2 3 a)) "please provide a symbol and a list")
    (test-equal? "empty list" (handle 'sam empty) 'not-found)
    (test-equal? "structured list" (handle 'sam collaborators) '@samsamsam)
    (test-equal? "not found" (handle 'ben collaborators) 'not-found)))

;7/10
(define nest-tests
  (test-suite
    "nest"
    (test-equal? "non-list" (nest 'a) "please provide a list")
    (test-equal? "empty list" (nest empty) (list empty))
    (test-equal? "normal case" (nest '(1 2 3)) '((1) (2) (3)))
    (test-equal? "structured list" (nest '(a (b (c d)) e)) '((a) ((b (c d))) (e)))))

;9/10
(define exchange-tests
  (test-suite
    "exchange"
    (test-equal? "normal case" (exchange 'a 'x '(a b r a c a d a b r a)) '(x b r x c x d x b r x))
    (test-equal? "empty list" (exchange 'a 'x empty) empty)
    (test-equal? "non-list" (exchange 'a 'x 'a) "please provide two objects and a list containing the first object")
    (test-equal? "non-symbol" (exchange 'a 'x '(a b r a c a d a b r a)) '(x b r x c x d x b r x))
    (test-equal? "stuctured list" (exchange '(able @not-a-machine) 'x collaborators) '((alex @xela) x (sam @samsamsam) (kiran @kiran)))))

;10/10
(define all-exchange-tests
  (test-suite
  "all-exchange"
  (test-equal? "normal case" (all-exchange'(b o) '(m u) '(b o b)) '(m u m))
  (test-equal? "lst empty" (all-exchange'(b o) '(m u) empty) empty)
  (test-equal? "a empty" (all-exchange'() '(b) (list empty 'b empty)) '(b b b))
  (test-equal? "b empty" (all-exchange'(b) '() (list empty 'b empty)) (list empty empty empty))
  (test-equal? "both empty" (all-exchange'() '() (list empty 'b empty)) (list empty 'b empty))
  (test-equal? "non-list" (all-exchange'(b o) '(m u) 'b) "please provide three lists")
  (test-equal? "structured list" (all-exchange '((b) o) '(m u) '((b) o b)) '(m u b))))


;----all-tests----
(define all-tests
  (test-suite
   "All tests"
   merge-tests
   sort-tests
   has-sublist?-tests
   handle-tests
   exchange-tests
   nest-tests
   all-exchange-tests))

(run-tests all-tests)
