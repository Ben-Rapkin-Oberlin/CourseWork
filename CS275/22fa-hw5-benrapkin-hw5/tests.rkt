;Ben Rapkin

#lang racket

(require rackunit rackunit/text-ui rackunit/gui)
(require "hw5.rkt")

(define test-stream
  (stream-cons 'x (stream-cons 'y (stream-cons 'z test-stream))))

(define test-stream2
  (stream-cons '(1 2 3) (stream-cons 'b '(c))))

(define stream-remove-all-tests
  (test-suite
    "stream-remove"
    (test-equal? "normal case " (stream->list(stream-take (stream-remove-all 'z (stream-remove-all 'y test-stream)) 10)) '(x x x x x x x x x x))
    (test-equal? "remove all" (stream->list(stream-remove-all 'x (stream-remove-all 'x '(x x x x)))) '())
    (test-equal? "not found" (stream->list(stream-take (stream-remove-all 'a test-stream) 10)) '(x y z x y z x y z x))
    (test-equal? "remove none" (stream->list(stream-take (stream-remove-all 'a test-stream) 10)) '(x y z x y z x y z x))
    (test-equal? "remove a stream" (stream->list(stream-remove-all '(1 2 3) test-stream2)) '(b c))
    (test-equal? "singleton 1" (stream->list(stream-remove-all '1 '((1) (2) (3)))) '((1) (2) (3)))
    (test-equal? "singleton 2" (stream->list(stream-remove-all '(1) '((1) (2) (3)))) '((2) (3)))
    (test-equal? "not stream" (stream-remove-all '1 'a) "invalid input")
   ))

(define stream-replace-tests
  (test-suite
    "stream-replace"
    (test-equal? "normal case" (stream->list(stream-take (stream-replace 'x 'y test-stream) 10)) '(y y z y y z y y z y))
    (test-equal? "empty stream" (stream->list(stream-replace 'x 'y '()) ) '())
    (test-equal? "not found" (stream->list(stream-take (stream-replace 'a 'b test-stream) 10)) '(x y z x y z x y z x))  
    (test-equal? "replace all" (stream->list(stream-replace 'x 'y '(x x x x))) '(y y y y))
    (test-equal? "replace a stream" (stream->list(stream-replace '(1 2 3) 'a test-stream2)) '(a b c))
    (test-equal? "singleton 1" (stream->list(stream-replace '1 'a '((1) (2) (3)))) '((1) (2) (3)))
    (test-equal? "singleton 2" (stream->list(stream-replace '(1) '(a) '((1) (2) (3)))) '((a) (2) (3)))
    (test-equal? "not stream" (stream-replace '1 'a 'a) "invalid input")
    ))

(define grune-a-b-tests
  (test-suite
    "grune-a-b"
    (test-equal? "normal case" (stream->list (grune-a-b '(a b c d a a a b a a))) '(a b c d b a b b))
    (test-equal? "empty list" (stream->list (grune-a-b '())) '())
    (test-equal? "no a" (stream->list (grune-a-b '(b b b b b b b b b b))) '(b b b b b b b b b b))
    (test-equal? "not stream" (grune-a-b 'a) "invalid input")
  ))

(define grune-tests
  (test-suite
    "grune"
    (test-equal? "normal case" (stream->list ((grune 'a 'b) '(a b c d a a a b a a))) '(a b c d b a b b))
    (test-equal? "empty list" (stream->list ((grune 'a 'b) '())) '())
    (test-equal? "no a" (stream->list ((grune 'a 'b) '(b b b b b b b b b b))) '(b b b b b b b b b b))
    (test-equal? "not stream" ((grune 'a 'b) 'a) "invalid input")
    (test-equal? "stream" (stream->list((grune '(1 2 3) 'a) '((1 2 3) (1 2 3) b c))) '(a b c))
  ))


; Define an All Tests test suite.
(define all-tests
  (test-suite
   "All tests"
   stream-remove-all-tests
   stream-replace-tests
    grune-a-b-tests
    grune-tests
  
  ))

(run-tests all-tests)
