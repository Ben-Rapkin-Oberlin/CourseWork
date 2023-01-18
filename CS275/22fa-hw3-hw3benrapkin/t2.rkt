#lang racket

(define (aa lst)
    (let*([a (map rational? lst)]
        [b (map integer? a)])
    (print lst)
    (print a)
    (print b)
    ))

(aa '(1 2 3 4 5 6 7 8 9 10))
