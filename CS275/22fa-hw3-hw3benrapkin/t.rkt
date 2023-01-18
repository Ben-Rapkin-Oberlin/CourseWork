#lang racket

(define (num-empty? lst)
;returns #t for mixed, #f for pure
    (let*([b (member empty? lst)]
          [c (member #t (map rational? lst))])
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

(valid-vector? (list empty 2 3))




(define (dot-product vec1 vec2)
    (cond[(and (empty? vec1) (empty? vec2)) 0]
        [(not(and (vector? vec1)(vector? vec2))) "please provid two vectors"]
        [(not(= (vector-length vec1)(vector-length vec2))) "please provid two vectors with the same length"]
        [(not (and (all-rational? (vector->list vec1))(all-rational? (vector->list vec2)))) "please provid two vectors with rational elements"]
        [(and (all-empty? (vector->list vec1))(all-empty? (vector->list vec2))) 0]
        [else (let([a (vector-map (lambda (x y)(if (and (empty? x)(empty? y)) empty (if (or (empty? x)(empty? y)) "!!!!" (if (or (list? x)(list? y)) "????" (* x y))))) vec1 vec2)])
                (if (number? (vector-member "!!!!" a)) "Cannot multiply empty by a number, please use 0 if that is the goal" (if (number? (vector-member "????" a)) "Please provide a flat vector of rational numbers, not a structured vector" 
                ;else
                    (if (not (num-empty? a)) (apply + (vector->list a)) ("cannot mix rational and empty, please use 0 if that is the goal")))))]))

        

#|
(define (transpose mat)
    ;(println 'map)
    ; i wrote the code for vectors then realized lists we ok, its dumb but it works
    ;(set! mat (vector-map list->vector (list->vector mat)))
   ; (println 'ere)
    (if (not (list? mat))  "matrix not valid"
        (if (not (apply = (map length mat))) "matrix not valid"
            ;(if (all-false? (vector->list (vector-map num-empty? (vector-map list->vector (list->vector mat))))) "matrix not valid" ;i don't know
           ; (begin 
            ;    (set! mat (map flatten mat))
                (let*([a (vector-map list->vector (list->vector mat))]
                    [b (mat-vec-mul a (first (vector->list a)))]
                    [c (if (vector? b) (vector->list b) 'error)])
                    (if (all-rational? c)
                        ;transpose
                        (begin
                        ;  (set! mat (map vector->list (vector->list mat)))
                            (apply map list mat)

                        )
                        ;else
                        "matrix not valid")))));ix not valid"



|#




;(define (mat-mat-mul mat1 mat2)
#|(define (vec-add vec1 vec2)
    (cond[(and (empty? vec1) (empty? vec2)) empty]
        [(not(and (vector? vec1)(vector? vec2))) "please provid two vectors"]
        [(not(= (vector-length vec1)(vector-length vec2))) "please provid two vectors with the same length"]
        [(not (all-rational? (vector->list vec1))) "please provid two vectors with rational elements"]
        [(not (all-rational? (vector->list vec2))) "please provid two vectors with rational elements"]
        [else (let([a (vector-map (lambda (x y)(if (and (empty? x)(empty? y)) empty (if (or (empty? x)(empty? y)) "!!!!" (if (or (list? x)(list? y)) "????" (+ x y))))) vec1 vec2)])
                 (if (number? (vector-member "!!!!" a)) "Cannot add empty to a number" (if (number? (vector-member "????" a)) "Please provide a flat vector of rational numbers, not a structured vector" a)))])) 
         
|#