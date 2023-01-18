#lang racket

;q1
(define (drop lst n)
    (if (empty? lst)"error two short"
        (if (= 0 n) lst (drop lst (- n 1)))))


(define (select lst)
    (if (empty? lst) '()
        (if (and (< 2.99 (third(first lst))) (or (= 2 (second (first lst)))(= 3 (second (first lst))))) (cons (first lst) (select (rest lst)))
            (select (rest lst)))))
(define students  '(("Brady" 2 3.5) ("Molly" 4 2.4) ("Rin" 2 2.2) ("Taylor" 3 1.6)
                                    ("Ali" 1 4.4) ("Iris" 3 3.1)))

(select students)

(define (duplicate1 lst)
    (if (empty? lst) '()
        (cons (cons (first lst)(list (first lst))) (duplicate1 (rest lst)))))

(define (duplicate2 lst)
    (if (empty? lst) '()
        (letrec ([helper (lambda (lst)
                           (if (empty? lst) '()
                               (cons (first lst) (cons (first lst) (helper (rest lst))))))])
            (helper lst))))

(define (duplicate3 lst)
   (map (lambda (x) (cons x (list x))) lst))

(duplicate2 '(1 2 3 4))

;(select )