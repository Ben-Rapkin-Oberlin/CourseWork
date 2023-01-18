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
(struct lambda-exp (symbols body)#:transparent) ; for lambda
(struct set-exp (symbol exp)#:transparent) ; for set!
(struct begin-exp (exps) #:transparent) ; for begin

;first name is proc, everything else is args, should call parse recursively on all args


(define (parse input)
    ;(println input)
    (cond
        [(number? input) (lit-exp input)]
        [(symbol? input) (var-exp input)]
        ;[(or (equal? input 'False)(equal? input 'True))(lit-exp input)]

        [(list? input)
            (cond ;[(empty? input) (error 'parse-exp "empty list")]
                [(empty? input) (var-exp 'null)]
                [(eq? (first input) 'if) 
                    (if (eq? (length input)4) 
                        (ite-exp (parse (second input)) (parse (third input)) (parse (fourth input)))
                        ;else
                    (begin (println (length input)) (error 'parse-exp "if must have 3 arguments")(print input)))]
                [(eq? (first input) 'let) 
                    (let ([binding-list (second input)]) 
                    ;check for right expression set up
                        (if (eq? (length input)3)
                        ;check to make sure all bindings follow correct size
                            (if (eq? (length binding-list) (length (filter (lambda (x) (eq? (length x) 2)) binding-list)))                    
                                (let-exp (map car binding-list) (map parse (map cadr binding-list)) (parse (third input)))
                                ;else
                            (error 'parse-exp "let bindings must be of the form (symbol value)"))
                        ;else
                        (error 'parse-exp "let should be 3 args, (let, binding list, code to execute")))]
                [(eq? (first input) 'letrec)
                    (if (eq? (length input)3)
                        (let* ([syms (map first (second input))]
                            [exps (map second (second input))]
                            [body (third input)]
                            [new-syms (map (lambda (x) (gensym)) syms)])
                            ;(println new-syms)
                            
                            ;outer let
                            ;symbols, bindings, body/ inner let->begin->set!->body
                            (let-exp syms (map (lambda (s)(lit-exp 0)) syms)
                                ;inner letd
                                ;symbols, bindings, body/begin->set!->body
                                (let-exp new-syms (map parse exps)
                                ;begin
                                    (begin-exp 
                                        (foldr (lambda (s new-s acc) (cons (set-exp s (var-exp new-s)) acc))
                                                (list (parse body)) syms new-syms))))) 
                        
                    ;else
                    (error 'parse-exp "letrec should be 3 args, (letrec, binding list, code to execute)") )]

                [(eq? (first input) 'lambda)
                    (if (eq? (length input)3)
                        (lambda-exp (second input) (parse (third input))) ;params are intinally not parsed
                    ;else
                    (error 'parse-exp "lambda should be 3 args, (lambda, list of symbols, code to execute)"))]
                [(eq? (first input) 'set!)
                    (if (eq? (length input)3)
                        (set-exp (second input) (parse (third input)))
                    ;else
                    (error 'parse-exp "set! should be 3 args, (set!, symbol, exp to set to)"))]
                [(eq? (first input) 'begin)
                    (begin-exp (map parse (rest input)))]                
                [else (app-exp (parse (car input)) (map parse (cdr input)))])]
        [else (error 'parse-exp "non-numeric input")]))


