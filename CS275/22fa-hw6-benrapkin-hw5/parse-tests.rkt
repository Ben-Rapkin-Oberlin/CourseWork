;ben rapkin
#lang racket

(require rackunit)
(require rackunit rackunit/text-ui rackunit/gui)
(require "parse.rkt")

(provide parse-tests)





(define parse-tests
  (test-suite
   "Parse tests"
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

  ))



;(run-tests parse-tests)
