#lang racket

(require "tree.rkt")

(define T0
    (make-tree 2 (make-tree 4) (make-tree 6) (make-tree 8 (make-tree 10))))

