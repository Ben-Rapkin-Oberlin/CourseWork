;ben rapkin
#lang racket

;EXP → number: parse into lit-exp


(provide (all-defined-out))
         





; The empty environment is null.
(define empty-lit-exp null)
(define empty-lit-exp? null?)

(define empty-var-exp null)
(define empty-var-exp? null?)



(struct lit-exp (val) #:transparent) ; for just numbers
(struct var-exp (symbol) #:transparent) ; for symbols
(struct app-exp (proc args)#:transparent) ; for function application
(struct ite-exp (cond then else)#:transparent) ; for if-then-else
(struct let-exp (symbols bindings body)#:transparent) ; for let

;first name is proc, everything else is args, should call parse recursively on all args


(define (parse input)
    (cond
        [(number? input) (lit-exp input)]
        [(symbol? input) (var-exp input)]
        ;[(list? s) (app-exp (car s) (map parse (cdr s)))]
        [(list? input)
            (cond [(empty? input) (error 'parse-exp "empty list")]
                  [(eq? (first input) 'if) (ite-exp (parse (second input)) (parse (third input)) (parse (fourth input)))]
                  [(eq? (first input) 'let) (let ([binding-list (second input)]) 
                                              ;  (let-exp (map car binding-list) (map cadr binding-list) (parse (third input))))]
                                                (let-exp (map car binding-list) (map parse (map cadr binding-list)) (parse (third input))))]
                  ;[(eq? (first input) 'lambda) ...]
                  [else (app-exp (parse (car input)) (map parse (cdr input)))])]
        [else (error 'parse-exp "non-numeric input")]))


;(parse '(if (add1 1) (* 2 2) (* 3 3)))
;(app-exp? (parse '(+ 1 2)))
;(parse '(if (null? null) (* 2 2 ) (* 3 3)))
;(parse '(let ((x 1) (y 2)) (+ x y)))

;;;(parse '(eqv? 1 2 3 ))
;(parse '(lt? 1 2 3 ))
;(parse '(gt? 1 2 3 ))
;(parse '(leq? 1 2 3 ))
;(parse '(geq? 1 2 3 ))


