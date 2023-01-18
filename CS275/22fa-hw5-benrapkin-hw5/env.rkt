;Ben Rapkin
#lang racket
(provide env
         env?
         empty-env
         empty-env?
         env-syms
         env-vals
         env-previous
         env-lookup)




; The empty environment is null.
(define empty-env null)
(define empty-env? null?)

; Define the env data type here
(struct env (syms vals previous) #:transparent)

(define (env-lookup environment symbol)
    (cond[(not (env? environment)) (error 'env-lookup "non-env provided" environment)]
        [(empty-env? environment) (error 'env-lookup "null-env provided" environment)]
        [(not (symbol? symbol)) (error ('env-lookup "non-symbol provided")symbol)]
        [(index-of (env-syms environment) symbol)(list-ref (env-vals environment) (index-of (env-syms environment) symbol))]
        [else (if (empty-env? (env-previous environment)) (error (error 'env-lookup "symbol not found" symbol)) (env-lookup (env-previous environment) symbol))]))


        
