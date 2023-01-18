;ben rapkin
#lang racket

(require rackunit)
(require "env.rkt" "parse.rkt" "interp.rkt")
(require rackunit rackunit/text-ui rackunit/gui)

(provide interp-tests init-env )

 ;'(+ - * / add1 sub1 negate list cons car cdr null?)

(define test-env
  (env '(x y) '(10 23) init-env))

(define basic-if-then (ite-exp (app-exp (var-exp 'add1) (list (lit-exp 1))) (app-exp (var-exp '*) (list (lit-exp 2) (lit-exp 2))) (app-exp (var-exp '*) (list (lit-exp 3) (lit-exp 3))))) ;gives non-zero value
(define basic-if-else (ite-exp (app-exp (var-exp 'sub1) (list (lit-exp 1))) (app-exp (var-exp '*) (list (lit-exp 2) (lit-exp 2))) (app-exp (var-exp '*) (list (lit-exp 3) (lit-exp 3))))) ;gives zero value

(define basic-if-then-2 (ite-exp (app-exp (var-exp 'null?) (list (lit-exp 1))) (app-exp (var-exp '*) (list (lit-exp 2) (lit-exp 2))) (app-exp (var-exp '*) (list (lit-exp 3) (lit-exp 3))))) ;gives #f as 1 is not null
;(define basic-if-else-2 (ite-exp (app-exp (var-exp 'null?) (list (var-exp null))) (app-exp (var-exp '*) (list (lit-exp 2) (lit-exp 2))) (app-exp (var-exp '*) (list (lit-exp 3) (lit-exp 3))))) ;gives #t as null is null

(define basic-let (let-exp '(x y) (list (lit-exp 1) (lit-exp 2)) (app-exp (var-exp '+) (list (var-exp 'x) (var-exp 'y)(var-exp 'z)))))
(define new-symbol-let (let-exp '(x a) (list (lit-exp 1) (lit-exp 2)) (app-exp (var-exp '+) (list (var-exp 'x) (var-exp 'a)(var-exp 'z)))))

(define a (var-exp 'x))

(define interp-tests
  (test-suite
   "Interpreter tests"
  
  (test-equal? "lit" (eval-exp (lit-exp 5) empty-env)   5)
  (test-equal? "var1" (eval-exp (var-exp 'x) init-env) 23)
  (test-equal? "var2" (eval-exp (var-exp 'y) init-env) 42)
  (test-exn "no env var"
          exn:fail?
          (λ () (eval-exp (var-exp 'x) empty-env)))
  (test-equal? "add" (eval-exp (app-exp (var-exp '+) (list (lit-exp 5) (lit-exp 6))) init-env) 11)
  (test-equal? "sub" (eval-exp (app-exp (var-exp '-) (list (lit-exp 5) (lit-exp 6))) init-env) -1)
  (test-equal? "mul" (eval-exp (app-exp (var-exp '*)(list (lit-exp 5) (lit-exp 6))) init-env) 30)
  (test-equal? "div" (eval-exp (app-exp (var-exp '/) (list (lit-exp 5) (lit-exp 6))) init-env) 5/6)
  (test-equal? "add1" (eval-exp (app-exp (var-exp 'add1) (list (lit-exp 5))) init-env) 6)
  (test-equal? "sub1" (eval-exp (app-exp (var-exp 'sub1) (list (lit-exp 5))) init-env) 4)
  (test-equal? "negate" (eval-exp (app-exp (var-exp 'negate) (list (lit-exp 5))) init-env) -5)
  (test-equal? "list" (eval-exp (app-exp (var-exp 'list) (list (lit-exp 5) (lit-exp 6))) init-env) (list 5 6))
  (test-equal? "cons" (eval-exp (app-exp (var-exp 'cons) (list (lit-exp 5) (lit-exp 6))) init-env) (cons 5 6))
  (test-equal? "car" (eval-exp (parse '(car (list 1 2 3 4)))init-env) 1)
  (test-equal? "cdr" (eval-exp (parse '(cdr (list 1 2 3 4)))init-env) '(2 3 4))
  (test-exn "not prim"
          exn:fail?
          (λ () (eval-exp (app-exp (var-exp 'foo)((lit-exp 5) (lit-exp 6))) init-env)))
  (test-equal? "if-then" (eval-exp basic-if-then init-env) 4)
  (test-equal? "if-else" (eval-exp basic-if-else init-env) 9)
  (test-equal? "if-then-2" (eval-exp basic-if-then-2 init-env) 9)
  ;(test-equal? "if-else-2" (eval-exp basic-if-else-2 init-env) 4)
  (test-equal? "let" (eval-exp basic-let init-env) 10)
  (test-equal? "new symbol let" (eval-exp new-symbol-let init-env) 10)
  (test-equal? "eqv" (eval-exp (app-exp (var-exp 'eqv?) (list (lit-exp 1) (lit-exp 2))) init-env) 'False)
  (test-equal? "lt" (eval-exp (app-exp (var-exp 'lt?) (list (lit-exp 1) (lit-exp 2))) init-env) 'True)
  (test-equal? "gt" (eval-exp (app-exp (var-exp 'gt?) (list (lit-exp 1) (lit-exp 2))) init-env) 'False)
  (test-equal? "null?" (eval-exp (app-exp (var-exp 'null?) (list (lit-exp 1))) init-env) 'False)
  (test-equal? "leq?" (eval-exp (app-exp (var-exp 'leq?) (list (lit-exp 1) (lit-exp 2))) init-env) 'True)
  (test-equal? "geq?" (eval-exp (app-exp (var-exp 'geq?) (list (lit-exp 1) (lit-exp 2))) init-env) 'False)

  (test-equal? "lambda" (eval-exp (app-exp (lambda-exp '(x) (app-exp (var-exp '*) (list (var-exp 'x) (lit-exp 2)))) (list (lit-exp 3)))
                         init-env) 6)
  (test-equal? "set!/begin" (eval-exp (begin-exp (list (set-exp 'x (lit-exp 1)) (set-exp 'y (lit-exp 2)) (app-exp (var-exp '+) (list (var-exp 'x) (var-exp 'y)))))
   init-env) 3)
  (test-equal? "letrec" (eval-exp
    (let-exp '(foo) (list (lit-exp 0)) (let-exp '(g1140) (list (lambda-exp '(x) (ite-exp (app-exp (var-exp 'eqv?) (list (var-exp 'x) (lit-exp 0))) (lit-exp 0) (app-exp (var-exp 'foo) (list (app-exp (var-exp 'sub1) (list (var-exp 'x)))))))) (begin-exp (list (set-exp 'foo (var-exp 'g1140)) (app-exp (var-exp 'foo) (list (lit-exp 2)))))))
   init-env) 0)        

  ))

;(run-tests interp-tests)
