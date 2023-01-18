;Ben Rapkin

#lang racket
; Your name(s) here.

(require "keyboard.rkt")
(require racket/stream)
; Export all of our top-level definitions so that tests.rkt
; can import them. See tests.rkt.
(provide (all-defined-out))

(define test-stream
  (stream-cons 'x (stream-cons 'y (stream-cons 'z test-stream))))

;P1
    ;Q1
    (define (stream-remove-all x s)
    (cond[(not (stream? s)) "invalid input"]
        [(stream-empty? s) empty-stream]
        [(equal?(stream-first s) x) (stream-remove-all x (stream-rest s))]
        [else (stream-cons (stream-first s) (stream-remove-all x (stream-rest s)))]))
    
    ;Q2
    (define (stream-replace x y s)
    (cond[(not (stream? s)) "invalid input"]
        [(stream-empty? s) empty-stream]
        [(equal?(stream-first s) x) (stream-cons y(stream-replace x y (stream-rest s)))]
        [else (stream-cons (stream-first s) (stream-replace x y (stream-rest s)))]))

;P2

    ;Q3
    (define (grune-a-b s)
    (cond[(not (stream? s)) "invalid input"]
        [(stream-empty? s) empty-stream]
        [else (begin
                (if (equal? (stream-first s) 'a)
                    (if (equal? (stream-rest s) empty-stream) s
                        ;else
                        (if (equal? (stream-first (stream-rest s)) 'a)
                            (stream-cons 'b (grune-a-b (stream-rest (stream-rest s))))
                            ;else
                            (stream-cons 'a (grune-a-b (stream-rest s)))))
                ;else
                (stream-cons (stream-first s) (grune-a-b (stream-rest s)))))]))


    ;Q4
    (define (grune x y)
        (lambda (s)
        (cond[(not (stream? s)) "invalid input"]
        [(stream-empty? s) empty-stream]
        [else (begin
                (if (equal? (stream-first s) x)
                    (if (equal? (stream-rest s) empty-stream) s
                        ;else
                        (if (equal? (stream-first (stream-rest s)) x)
                            (stream-cons y ((grune x y)  (stream-rest (stream-rest s))))
                            ;else
                            (stream-cons x ((grune x y) (stream-rest s)))))
                ;else
                (stream-cons (stream-first s) ((grune x y) (stream-rest s)))))])))
