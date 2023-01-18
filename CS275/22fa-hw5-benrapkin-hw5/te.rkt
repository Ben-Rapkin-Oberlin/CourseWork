#lang racket

;(define (t l n)
;    (cond[(index-of l n) "truthy"]
;            [else "falsey"]))

;(t '(1 2 3 4) 7) ; "falsey"

;(define a '('(1) '(2) '(3)))

;(stream-first a)

;(define test-stream2
  ;(stream-cons '(1 2 3) (stream-cons 'b '(c))))

;(stream->list test-stream2)

(symbol? '(foo))