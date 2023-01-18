;ben rapkin
#lang racket

(require rackunit)
(require rackunit rackunit/text-ui rackunit/gui)
(require "parse.rkt")

(provide parse-tests)





(define parse-tests
  (test-suite
   "Parse tests"
   (test-true "null" (var-exp? (parse 'null)))
   (test-true "Literal?" (lit-exp? (parse 5)))
   (test-equal? "lit-exp-val" (lit-exp-val (parse 5))5)
   (test-true "Variable?" (var-exp? (parse 'x)))
   (test-equal? "var-exp-symbol" (var-exp-symbol (parse 'x)) 'x)
   (test-true "Application?" (app-exp? (parse '(+ 1 2))))
   (test-equal? "app-exp-proc" (app-exp-proc (parse '(+ 1 2))) (var-exp '+))
   (test-equal? "app-exp-args" (app-exp-args (parse '(+ 1 2))) (list (lit-exp 1) (lit-exp 2)))
   (test-true "ite?" (ite-exp? (parse '(if (+ 1 2) 3 4))))
   (test-equal? "ite-test" (ite-exp-cond (parse '(if (+ 1 2) 3 4))) (app-exp (var-exp '+) (list (lit-exp 1) (lit-exp 2))))
   (test-equal? "ite-then" (ite-exp-then (parse '(if (+ 1 2) 3 4))) (lit-exp 3))
   (test-equal? "ite-else" (ite-exp-else (parse '(if (+ 1 2) 3 (sub1 5)))) (app-exp (var-exp 'sub1) (list (lit-exp 5) )))
   (test-true "let?" (let-exp? (parse '(let ((x 1) (y 2)) (+ x y)))))
   (test-equal? "let-sym" (let-exp-symbols (parse '(let ((x 1) (y 2)) (+ x y)))) (list 'x 'y))
   (test-equal? "let-bind" (let-exp-bindings (parse '(let ((x 1) (y 2)) (+ x y)))) (list (lit-exp 1) (lit-exp 2)))
   (test-equal? "let-body" (let-exp-body (parse '(let ((x 1) (y 2)) (+ x y)))) (app-exp (var-exp '+) (list (var-exp 'x) (var-exp 'y))))
   (test-equal? "lambda" (parse '((lambda (x) (* x 2))3)) (app-exp (lambda-exp '(x) (app-exp (var-exp '*) (list (var-exp 'x) (lit-exp 2)))) (list (lit-exp 3))))

   (test-equal? "begin/set" (parse '(begin (set! x 1) (set! y 2) (+ x y))) (begin-exp (list (set-exp 'x (lit-exp 1)) (set-exp 'y (lit-exp 2)) (app-exp (var-exp '+) (list (var-exp 'x) (var-exp 'y))))))
   (test-true "letrec" (let-exp? (parse '(letrec([foo (lambda (x)
                                    (if (eqv? x 0) 0 (foo (sub1 x))))])
                                        (foo 2)))))
  ))

;(run-tests parse-tests)
