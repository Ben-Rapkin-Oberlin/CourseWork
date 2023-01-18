#lang racket
; Your name(s) here

(require rackunit rackunit/text-ui rackunit/gui)
(require "hw4.rkt")
(require "tree.rkt")


;P1
  (define replace-tests
    (test-suite
    "replace"
    (test-equal? "normal case" (replace 1 2 (list 1 2 3 1 2 3)) (list 2 2 3 2 2 3))
    (test-equal? "empty list" (replace 1 2 '()) '())
    (test-equal? "no match" (replace 1 2 (list 3 4 5)) (list 3 4 5)) 
    (test-equal? "all matches" (replace 1 2 (list 1 1 1 1 1 1)) (list 2 2 2 2 2 2))
    (test-equal? "strut1" (replace 1 2 '((1 2 3) (3 3 3)( 1 2 3))) '((1 2 3) (3 3 3)( 1 2 3)))
    (test-equal? "struct2" (replace '(1 2 3) 1 '((1 2 3) (3 3 3)( 1 2 3))) '(1 (3 3 3) 1))
    (test-equal? "singelton1" (replace 1 2 '((1)(1))) '((1)(1)))
    (test-equal? "singelton2" (replace '(1) '(2) '((1)(1))) '((2)(2)))
    ))

  (define index-tests
    (test-suite
    "index"
      (test-equal? "normal case" (index 2 (list 1 2 3 4 5)) 1)
      (test-equal? "empty list1" (index 2 '()) -1)
      (test-equal? "empty list2" (index '() '()) 0)
      (test-equal? "no match" (index 2 (list 1 3 4 5)) -1)
      (test-equal? "all matches" (index 2 (list 2 2 2 2 2 2)) 0)
      (test-equal? "strut1" (index 2 '((1 2 3) (3 3 3)( 1 2 3))) -1)
      (test-equal? "struct2" (index '(1 2 3) '((1 2 3) (3 3 3)( 1 2 3))) 0)
      (test-equal? "singelton1" (index 2 '((1)(1))) -1)
      (test-equal? "singelton2" (index '(1) '((1)(1))) 0)
      ))

  (define bags1
    '((duffle 8)
      (garment-bag 2)
      (briefcase 5)
      (valise 7)
      (steamer-trunk 65)))

  (define bags2
    '((duffle 8)
      (garment-bag 2)
      (briefcase 5)
      (valise 7 2)
      (steamer-trunk 65)))

  (define bags3
    '(((duffle 8)
      (garment-bag 2)
      (briefcase 5)
      (valise 2)
      (steamer-trunk 65)
      )))

  (define bags4
    '((duffle 8)
      (garment-bag 2)
      (briefcase a)
      (valise 2)
      (steamer-trunk 65)
      ))

  (define bags5
    '((duffle 8)
      (garment-bag 2)
      (briefcase a)
      (valise 2)
      (steamer-trunk (65))
      ))

  (define bags6
    '((duffle 8)
      (garment-bag 2)
      (briefcase a)
      (valise 2)
      (steamer-trunk (65 4))
      ))

  (define bags7
    '((duffle 8)
      (garment-bag 2)
      (briefcase 2+3i)
      (valise 7)
      (steamer-trunk 65)))

  (define weigh-tests
    (test-suite
    "weigh"
      (test-equal? "normal case" (weigh bags1) 87)
      (test-equal? "empty list" (weigh '()) 0)
      (test-equal? "b2, list size" (weigh bags2) "error")
      (test-equal? "b3, struct" (weigh bags3) "error")
      (test-equal? "b4, not number" (weigh bags4) "error")
      (test-equal? "b5, internal singleton" (weigh bags5) "error")
      (test-equal? "b6, internal list" (weigh bags6) "error")
      (test-equal? "b7, non-rational number" (weigh bags7) "error")
      (test-equal? "single elm" (weigh '((duffle 8))) 8)
      ))   
  
  (define heaviest-tests
    (test-suite
    "heaviest"
      (test-equal? "normal case" (heaviest bags1) 'steamer-trunk)
      (test-equal? "empty list" (heaviest '()) "error")
      (test-equal? "b2, list size" (heaviest bags2) "error")
      (test-equal? "b3, struct" (heaviest bags3) "error")
      (test-equal? "b4, not number" (heaviest bags4) "error")
      (test-equal? "b5, internal singleton" (heaviest bags5) "error")
      (test-equal? "b6, internal list" (heaviest bags6) "error")
      (test-equal? "b7, non-rational number" (heaviest bags7) "error")
      (test-equal? "single elm" (heaviest '((duffle 8))) 'duffle)
      ))


;P2

(define T0
    (make-tree 2 (make-tree 4) (make-tree 6) (make-tree 8 (make-tree 10))))
(define T0prime
    (make-tree 3 (make-tree 5) (make-tree 7) (make-tree 9 (make-tree 11))))
(define T0pp
    (make-tree 6 (make-tree 10) (make-tree 14) (make-tree 18 (make-tree 22))))

  (define child-sum-tests
      (test-suite
      "child-sum"
      (test-equal? "normal case" (child-sum T0) 18)
      (test-equal? "leaf tree" (child-sum (make-tree 2)) 0)
      (test-equal? "empty tree" (child-sum empty-tree) 0)
      (test-equal? "normal 2" (child-sum T8) 173)
      (test-equal? "non-tree" (child-sum 'a) "error")
      (test-equal? "list" (child-sum '(1 2 3)) "error")
      ))

  (define all-sum-tests
    (test-suite
    "all-sum"
    (test-equal? "normal case" (all-sum T0) 30)
    (test-equal? "normal 2" (all-sum T8) 293)
    (test-equal? "leaf tree" (all-sum (make-tree 2)) 2)
    (test-equal? "empty tree" (all-sum empty-tree) 0)  
    (test-equal? "non-tree" (all-sum 'a) "error")
    (test-equal? "list" (all-sum '(1 2 3)) "error")
    ))

  (define vist-tree-tests
        (test-suite
        "visit-tree"
        (test-equal? "normal case" (vist-tree add1 T0) T0prime)
        (test-equal? "leaf tree" (vist-tree (lambda (x) (* 2 x)) T0prime) T0pp)
        (test-equal? "empty tree" (vist-tree add1 empty-tree) "error")
        (test-equal? "non-tree" (vist-tree add1 'a) "error")
        (test-equal? "list" (vist-tree add1 '(1 2 3)) "error")
        ))
  
  (define size-of-tests 
    (test-suite
    "size-of"
    (test-equal? "normal case" (size-of T0) 5)
    (test-equal? "nomral 2" (size-of T8) 8)
    (test-equal? "leaf tree" (size-of (make-tree 2)) 1)
    (test-equal? "empty tree" (size-of empty-tree) 0)
    (test-equal? "non-tree" (size-of 'a) "error")
    (test-equal? "list" (size-of '(1 2 3)) "error")
    ))

  (define height-of-tests
    (test-suite
    "height-of"
    (test-equal? "normal case" (height-of T0) 2)
    (test-equal? "normal 2" (height-of T8) 2)
    (test-equal? "leaf tree" (height-of (make-tree 2)) 0)
    (test-equal? "empty tree" (height-of empty-tree) -1)
    (test-equal? "non-tree" (height-of 'a) "error")
    (test-equal? "list" (height-of '(1 2 3)) "error")
    ))

  (define pre-order-tests
    (test-suite
    "pre-order"
    (test-equal? "normal case" (pre-order T0) '(2 4 6 8 10))
    (test-equal? "normal 2" (pre-order T8) '(16 73 50 22 10 100 5 17))
    (test-equal? "leaf tree" (pre-order (make-tree 2)) '(2))
    (test-equal? "empty tree" (pre-order empty-tree) '())
    (test-equal? "non-tree" (pre-order 'a) "error")
    (test-equal? "list" (pre-order '(1 2 3)) "error")
    ))

  (define post-order-tests
    (test-suite
    "post-order"
    (test-equal? "normal case" (post-order T0) '(4 6 10 8 2))
    (test-equal? "normal 2" (post-order T8) '(50 22 10 73 5 17 100 16))
    (test-equal? "leaf tree" (post-order (make-tree 2)) '(2))
    (test-equal? "empty tree" (post-order empty-tree) '())
    (test-equal? "non-tree" (post-order 'a) "error")
    (test-equal? "list" (post-order '(1 2 3)) "error")
    ))
  









; Define an All Tests test suite.
(define all-tests
  (test-suite
   "All tests"
   replace-tests
   index-tests
  weigh-tests
  heaviest-tests
  child-sum-tests
  all-sum-tests
  vist-tree-tests
  size-of-tests
  height-of-tests
  pre-order-tests
  post-order-tests
   
  

   ))
  

(run-tests all-tests)
