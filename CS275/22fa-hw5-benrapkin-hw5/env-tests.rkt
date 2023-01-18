;ben rapkin
#lang racket

(require rackunit rackunit/text-ui rackunit/gui)
(require "env.rkt")

; Define an environment for testing.
(define env-one
  (env '(x y z)
       '(1 2 0)
       empty-env))

(define env-two
  (env '(x y)
       '(3 4)
       env-one))

(define env-three
  (env '(a b c d)
       '(5 6 7 8)
       env-two))

(define env-tests
  (test-suite
   "Environment tests"
    (test-equal? "env-three val" (env-vals env-three) '(5 6 7 8))
    (test-equal? "env-three vars" (env-syms env-three) '(a b c d))
    (test-equal? "env-three grandparent" (env-previous(env-previous env-three)) env-one)
    (test-true "recongnizer" (env? env-three))
    (test-true "empty env" (empty-env? empty-env))
;;;;;;;;;;;;;;;;;; above makes sure the stucts are working
    (test-equal? "normal case"  (env-lookup env-one 'x) 1)
    (test-equal? "normal case"  (env-lookup env-two 'y) 4)
    (test-equal? "normal case"  (env-lookup env-three 'a) 5)
    (test-equal? "past env case"  (env-lookup env-three 'x) 3)
    (test-equal? "past env case"  (env-lookup env-three 'z) 0)
    (test-exn "Empty environment has no previous"
          exn:fail?
          (λ () (env-previous empty-env)))
    (test-exn "look-up empty env"
          exn:fail?
          (λ () (env-lookup empty-env 'a)))
    (test-exn "look-up non-env"
          exn:fail?
          (λ () (env-lookup 'a 'a)))  
    (test-exn "look-up non-sym"
          exn:fail?
          (λ () (env-lookup env-three '(1) )))
    (test-exn "look-up not there"
          exn:fail?
          (λ () (env-lookup env-three 'r )))
    
        
     
          
   ))


(run-tests env-tests)
