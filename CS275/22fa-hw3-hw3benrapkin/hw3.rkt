#lang racket
; Your name(s) here.

; Export all of our top-level definitions so that tests.rkt
; can import them. See tests.rkt.
(provide (all-defined-out))
;Q7
(define (flatten lst)
    (cond[(empty? lst) empty]
        [(not (list? lst)) "please provide a list"]
        [else (append (if (and (not (empty? (first lst))) (list? (first lst))) (flatten (first lst)) (list (first lst))) (flatten (rest lst)))]))

;assorted helper functions
    (define (num-empty? lst)
        ;returns #t for mixed, #f for pure
        (let*([b (member empty lst)]
            [c (member #t (map rational? lst))])
         ; (println b)
         ; (println c)
          ;(println (and c b))
            (if (and c b) #t #f)))

    (define (all-rational? lst)
        ;(println lst)
        (cond[(empty? lst) #t]
            [(rational? lst)#t]
            [(not (list? lst))#f]
            [else (if (all-rational? (car lst)) (all-rational? (cdr lst)) #f)]))

    (define (all-empty? lst)
    (if (empty? lst) #t (if (empty? (first lst)) (all-empty? (rest lst)) #f)))

    (define (valid-vector? lst)
        (cond[(not (list? lst)) #f]
            [(num-empty? lst) #f]
            [(not (all-rational? lst)) #f]
            [else (if (equal? lst (flatten lst))#t #f)]))
    
    (define (all-true? lst)
        (if (empty? lst) #t 
            (if (equal? (first lst) #t) (all-true? (rest lst)) #f)))


           
;Q1
(define (firsts lst)
    (if (not (list? lst)) "please provid a list"
        (if (or(eq? (length lst) 1)(eq? (length lst)0)) lst
            (map (lambda (x)(if (null? x) empty (car x))) lst))))
;(car empty)
;(firsts (list '() '() '()))
;(firsts '(((1 2) 3) (4 5 6) ((7) 8 9))) ;'((1 2) 4 (7)))

(define (rests lst)
    (if (not (list? lst)) "please provid a list"
        (if (or(eq? (length lst) 1)(eq? (length lst)0)) "lst should be a structured list of lists with each sublist having >1 element" 
            (let([a (map (lambda (x)(if (<(length x)2) "!!!!"  (cdr x))) lst)])
                (if (member "!!!!" a) "lst should be a structured list of lists with each sublist having >1 element" 
                a)))))
          

;Q2
(define (vec-add lst1 lst2)
     (cond[(not (and (valid-vector? lst1) (valid-vector? lst2))) "please provid two lists of the same length with either with all rational-numeric or empty elements"]
        [(not(= (length lst1)(length lst2))) "please provid two lists of the same length with either with all rational-numeric or empty elements"]
        [(and (all-empty? lst1)(all-empty? lst2)) lst1]
        [else (map + lst1 lst2)]))
         


;(vec-add (vector 1 'a 3) (vector empty 5 6))

;Q3  
(define (dot-product lst1 lst2)
    (cond[(not (and (valid-vector? lst1) (valid-vector? lst2))) "please provid two lists of the same length with either with all rational-numeric or empty elements"]
        [(not(= (length lst1)(length lst2))) "please provid two lists of the same length with either with all rational-numeric or empty elements"]
        [(and (all-empty? lst1)(all-empty? lst2)) 0]
        [else (apply + (map * lst1 lst2))]))





;Q4
(define (mat-vec-mul mat lst)
    (cond[(and (empty? mat) (empty? lst)) 0]
        [(not(and (list? lst)(list? mat))) "matrix and/or vector not valid"]
        [else
            (let*([a  (map ((curry dot-product) lst) mat)]
                [b (map rational? a)])
                ;(println a)))
                (if (member #f b ) "matrix and/or vector not valid" a))]))

;Q5
(define (transpose mat)
    (cond[(not (list? mat)) "matrix not valid"]
         [(empty? mat) mat]
        [(member #f (map valid-vector? mat))"matrix not valid"]
        [(not (apply = (map length mat)))"matrix not valid"]
        [else  (apply map list mat)]))

(define (valid-matrix? lst)
        (let([inverse (transpose lst)])
            (if (equal? inverse "matrix not valid") #f
               (let([valid1 (map valid-vector? lst)]
                    [valid2 (map valid-vector? inverse)])
                    (if (and (all-true? valid1) (all-true? valid2)) #t #f)))))


;Q6
(define (good-dimensions? mat1 mat2)
    (let([a (transpose mat1)])
        (if (not (and (valid-matrix? mat1) (valid-matrix? mat2))) #f
            (if (equal? (length a) (length mat2))#t 'b))))

(define (mat-mat-mul mat1 mat2)
    (if (not (good-dimensions? mat1 mat2)) "matrix 1 and/or 2 are invalid"
        (let([a (transpose mat2)])
            (map (lambda (x)(mat-vec-mul a x)) mat1))))
;(valid-matrix? '((empty) (empty)))
;(valid-matrix? '((empty empty)))
;(good-dimensions? '((empty) (empty)) '((empty empty)))

;Q8
(define (sum lst)
    (let([a (flatten lst)])
        (cond[(not (list? a)) "please provide a list"]
            [(empty? lst)"please provide a list of rational numbers"]
            [(member #t (map empty? a))"please provide a list of rational numbers"]
            [(not (all-rational? lst)) "please provide a list of rational numbers"]
            [else (apply + a)])))

;Q9
;list is often not flat
;assume we don't need to handle errors from provided func, like with map
(define (gen-map func lst)
    ;(println lst)
    (cond[(not(list? lst)) "please provide a list"]
        [(empty? lst) empty]
        [else (cons (if (and (not (empty? (first lst))) (list? (first lst))) (gen-map2 func (first lst)) (func (first lst))) (gen-map func (rest lst)))]))
(define (gen-map2 func lst)
    ;(println lst)
    (cond[(not(list? lst)) "please provide a list"]
        [(empty? lst) empty]
        [else (append (if (and (not (empty? (first lst))) (list? (first lst))) (gen-map2 func (first lst)) (list (func (first lst)))) (gen-map2 func (rest lst)))]))

;Q10
(define (element-of? elm lst)
    (cond[(not(list? lst)) "please provide a list"]
        [(and (empty? lst)(not (empty? elm))) #f]
        [(and (empty? lst)(empty? elm) #t)]
        [else (if (equal? (first lst) elm) #t
                (if (list? (first lst)) (or (element-of? elm (first lst)) (element-of? elm (rest lst)))
                    (element-of? elm (rest lst))))]))
                 

;(element-of? '(1 (2)) ( '(1 (2)) (((4))) 5))
           
        
        
        
        
        
        
         
;(element-of? 1 (list (list 1 2 3) (list 4 5 6) (list 7 8 9)))