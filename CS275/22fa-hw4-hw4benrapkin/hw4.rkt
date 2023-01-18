#lang racket
; Ben Rapkin
(require "tree.rkt")


; Export all of our top-level definitions so that tests.rkt
; can import them. See tests.rkt.
(provide (all-defined-out))

;P1


    (define (base-list-test lst)
        (cond[(not(list? lst)) #f]
            [(not (equal? (flatten lst) lst)) #f]
            [else #t]))



    (define (replace a b lst)
        (cond [(null? lst) '()]
            [(not (list? lst)) (error "replace: not a list" lst)]
            [else (foldr (lambda (x y) (if (equal? x a) (cons b y) (cons x y))) '() lst)]))


    (define (index x lst)
        (cond [(not (list? lst)) "error"]
            [(and (empty? lst) (empty? x)) 0]
            [else (let([i (foldl (lambda (b a) (if (first a) a
                                                        (if  (equal? b x ) (list #t (second a)) (list #f (add1 (second a))))))
                                    '(#f 0) lst)])
                        (if (first i)(second i) -1))]))


    (define (weigh bags)
        (cond [(null? bags) 0]
            [(not (list? bags)) "error"]
            [(not (foldl (lambda (x last) (and (list? x) (equal? 2 (length x))(rational? (second x)) last)) #t bags)) "error"]
            [else (foldl (lambda (b a)(+ a (second b))) 0 bags)]))


    (define (heaviest bags)
        (cond [(null? bags) "error"]
            [(not (list? bags)) "error"]
            [(not (foldl (lambda (x last) (and (list? x) (equal? 2 (length x))(rational? (second x)) last)) #t bags)) "error"]
            [else (first (foldl (lambda (b a) (if (> (second b) (second a)) b a)) (first bags) bags))]))

;P2

    ;trees are numeric
    ;empty tree is defined as null

    ;contructor:
    ;(tree value (list child-1 child-2 ... child-n))
    ;(make-tree value child-1 child-2 ... child-n)

    ;recognizer:
    ;(empty-tree? t) ; Returns #t if t is an empty tree
    ;(tree? t)       ; Returns #t if t is a nonempty tree
    ;(leaf? t) ; Returns #t if t has no children

    ;accessor:
    ;(tree-value t)    ; Returns t's value
    ;(tree-children t) ; Returns t's list of children
    (define (valid-tree tree) ;not tested 
       (cond [(empty-tree? tree) #t]
             [(not (tree? tree)) #f]
             [(not (list? (tree-children tree))) #f]
             [else (foldl (lambda (x last) (and (tree? x) last)) #t (tree-children tree))]))




    (define (child-sum t)
        ;only intermidiate children
        (cond[(not(valid-tree t)) "error"]
            [(empty-tree? t) 0]
            [(leaf? t) 0]
            [else (foldl (lambda (tree sum)(+ sum (tree-value tree))) 0 (tree-children t))]))
    
    (define (all-sum t)
        ;all children
        (cond[(not (valid-tree t)) "error"]
            [(empty-tree? t) 0]
            [(leaf? t) (tree-value t)]
            [else (foldl (lambda (tree sum)(+ sum (all-sum tree))) (tree-value t) (tree-children t))]))

    (define (vist-tree f t)
        ;does not treat empty as 0
        (cond[(not (valid-tree t)) "error"]
            [(empty-tree? t) "error"]
            [(leaf? t) (make-tree (f (tree-value t)))]
            ;it's value, It's children
            [else 
                (apply (curry make-tree (f (tree-value t))) (map (lambda (x) (vist-tree f x)) (tree-children t)))])) ;makes a list of n args

    (define (size-of t)
        (cond[(not (valid-tree t)) "error"]
            [(empty-tree? t) 0]
            [(leaf? t) 1]
            [else (foldl (lambda (tree sum)(+ sum (size-of tree))) 1 (tree-children t))]))


    (define (height-of t)
        ;height of tree
        ;1+max height of children
        (cond[(not (valid-tree t)) "error"]
            [(empty-tree? t) -1]
            [(leaf? t) 0]
            [else  (+ 1 (apply max (map height-of (tree-children t))))]))


    (define (pre-order t)
        (cond[(not (valid-tree t)) "error"]
            [(empty-tree? t) '()]
            [(leaf? t) (list (tree-value t))]
            [else (cons (tree-value t) (foldl (lambda (tree lst) (append lst (pre-order tree))) '() (tree-children t)))]))

    (define (post-order t)
        (cond[(not (valid-tree t)) "error"]
            [(empty-tree? t) '()]
            [(leaf? t) (list (tree-value t))]        
            [else (flatten (append (map post-order (tree-children t)) (list (tree-value t))))]))

(define T0
    (make-tree 2 (make-tree 4) (make-tree 6) (make-tree 8 (make-tree 10))))


