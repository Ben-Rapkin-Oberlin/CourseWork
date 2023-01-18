;ben rapkin
#lang racket
(provide eval-exp
        init-env
        prim-env
        )

(require "parse.rkt")
(require "env.rkt")


(struct prim-proc (op) #:transparent)
(define primitive-operators '(+ - * / add1 sub1 negate list cons car cdr null? eqv? lt? gt? leq? geq? ))
(define basic-let (let-exp '(x y) (list (lit-exp 1) (lit-exp 2)) (app-exp (var-exp '+) (list (var-exp 'x) (var-exp 'y)(var-exp 'z)))))

(define T (parse '23))

(define prim-env
  (env (cons 'empty-list primitive-operators)
        
       (cons 'null (map prim-proc primitive-operators))
       empty-env))

(define init-env (env '(x y z #t #f)
       '(23 42 7 True False)
       prim-env))

(define empty-list 'null)





(define (apply-primitive-op op args)
  ;(println args)
  (cond [(eq? op '+) (apply + args)]
        [(eq? op '-) (apply - args)]
        [(eq? op '*) (apply * args)]
        [(eq? op '/) (apply / args)]
        [(eq? op 'add1) (apply add1 args)]
        [(eq? op 'sub1) (apply sub1 args)]
        [(eq? op 'negate) (apply (lambda(x) (* -1 x)) args)]
        [(eq? op 'list) (apply list args)]
        [(eq? op 'cons) (apply cons args)]
        [(eq? op 'car) (car args)] ;currently working with input (car 1 2 3) as parse wraps the args in a list
        [(eq? op 'cdr) (cdr args)]
        [(eq? op 'null?) (if (null? args)'True 'False)]
        [(eq? op 'eqv?) (if (apply eqv? args)'True 'False)]
        [(eq? op 'lt?) (if (apply < args) 'True 'False1)]
        [(eq? op 'gt?) (if (apply > args)'True 'False)]
        [(eq? op 'leq?) (if (apply <= args)'True 'False)]
        [(eq? op 'geq?) (if (apply >= args)'True 'False)]
        [else (error 'apply-primitive-op "Unknown primitive: ~s" op)]))



(define (apply-proc proc args)
    ;(println proc)
    ;(println args)
    ;(println (prim-proc? proc))
  (cond [(prim-proc? proc)
         (apply-primitive-op (prim-proc-op proc) args)]
        [else (error 'apply-proc "bad procedure: ~s" proc)]))




(define (eval-exp tree given-env)
    ;might need to implement tree tests
    ;(println tree)
    (cond[(lit-exp? tree) (lit-exp-val tree)]
        [(not(env? given-env)) (error 'eval-exp "given-env is not env")]
        [(var-exp? tree) (env-lookup given-env (var-exp-symbol tree))]
        [(ite-exp? tree) (if (or (eq? (eval-exp (ite-exp-cond tree) given-env) 'False) (eq? (eval-exp (ite-exp-cond tree) given-env) 0)) ;if the condition is false or 0
                                (eval-exp (ite-exp-else tree) given-env)
                                (eval-exp (ite-exp-then tree) given-env))] 
        [(let-exp? tree) (let ([newE (env (let-exp-symbols tree)(map (lambda (x) (eval-exp x given-env)) (let-exp-bindings tree)) given-env)])
                            (eval-exp (let-exp-body tree) newE))]
        [(app-exp? tree)
            (let ([proc (eval-exp (app-exp-proc tree) given-env)]
                    [args (map (lambda (arg) (eval-exp arg given-env)) (app-exp-args tree))])
                (apply-proc proc args))]
        [else (error 'eval-exp "unknown expression type")]))

;(eval-exp (app-exp (var-exp 'cons) (list (lit-exp 5) (lit-exp 6))) init-env)

;(eval-exp (parse '(if (add1 1) (* 2 2) (* 3 3))) init-env)

;(parse 'x)
;(eval-exp (parse 'x) init-env)
;(negate 5)
;(eval-exp (app-exp (var-exp 'negate) (list (lit-exp 5))) init-env)
;(negate 5)
;(parse '(let ((x 1) (y 2)) (+ x y)))

;(apply eqv? '(1 2))
;(eval-exp (parse '(eqv? 1 2)) init-env)
;(eval-exp basic-let init-env)
;(parse '(+ 1 1))
;(eval-exp (parse '(+ 1 1)) init-env)
;(println (read))
;(parse (read))