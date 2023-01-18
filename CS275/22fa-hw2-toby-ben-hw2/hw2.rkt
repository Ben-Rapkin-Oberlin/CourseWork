;Ben
;Toby
#lang racket

; Export all of our top-level definitions so that tests.rkt
; can import them. See tests.rkt
(provide (all-defined-out))

;2/10
;defining insert helper func
(define (insert n sublst)
  (cond [(empty? sublst) (cons n sublst)]
        [(< n (first sublst)) (cons n sublst)]
        [else (cons (first sublst) (insert n (rest sublst)))]))

;defining sorting helper func
(define (sort-h lst sublst)
  (cond [(empty? lst) sublst]
        [else (sort-h (rest lst) (insert (first lst) sublst))]))

;defining sort wrapper
(define (sort lst)
  (sort-h lst '()))



;1/10
;merge two sorted lsts into 1 sorted lst
;uses Q2 to sort
;flattens structured lists

;empty lst
;nonflat list
;not list of ints
;all-same? helper func
(define (all-same? tst lst)
  (cond[(not(list? lst)) #f]
       [(null? lst) #t]
       [(tst (first lst)) (all-same? tst (rest lst))]
       [else #f]))

(define (merge lst1 lst2)
  (cond[(not (and (list? lst1) (list? lst2))) "please provide two lists"]
       [(and (empty? lst1) (empty? lst2)) empty]
       [(empty? lst1) lst2]
       [(empty? lst2) lst1]
       [else (begin
               (let([a (flatten lst1)]
                    [b (flatten lst2)])
                 (cond[(not (all-same? rational? a)) "please use rational numbers"] 
                      [(not (all-same? rational? b))"please use rational numbers"];
                      [else (sort(append a b))])))]))


;3/10
;determines if biglist contains a particular sublist
;will flatten structured lists
(define (has-sublist? smol big)
  (cond[(not (and (list? smol) (list? big))) "please provide two lists"]
       [(and (empty? smol) (empty? big)) #t]
       [(empty? smol)(list? (member empty big))]; checks if big has the empty list
       [(empty? big) #f]
        ;both are lists and both are non-empty
       [else (begin
               (let([a (flatten smol)]
                    [b (flatten big)])
                  (cond[(> (length a)(length b)) #f]
                       [(eq? (length a) 1)
                        (if (eq? (first smol)(first big)) #t
                            ;else not matching a[0]
                            (if (eq?(length b)1) #f
                                ;else check rest of big
                                (has-sublist? a (rest b))))];to aovid passing and empty list for smol
                       [(eq? (first a)(first b)) (has-sublist? (rest a) (rest b))]
                       [else #f])))]))

;5/10
;person is name associated with github name
;github-map is structured list of ((name,github username),...)
(define (handle person github-map)
     (cond[(not (and (symbol? person) (list? github-map))) "please provide a symbol and a list"]
          [(empty? github-map) 'not-found]
          [(eq? person (first (first github-map))) (second (first github-map))]; if person matches first name in github-map, return github username
          [else (handle person (rest github-map))]))


;7/10
;assumes we should wrap empties
(define (nest lst)
     ;(println (list (first lst)))
     (cond[(not (list? lst)) "please provide a list"]
          [(empty? lst) (list empty)]
          [else (if (eq? (length lst)1) (list lst)
               ;else
               (cons (list (first lst)) (nest (rest lst))))]))

;9/10
;does not assume we should flatten structured lists
(define (exchange old new lst)
     ;(if (not (empty? lst)) (println (first lst)) (println "empty"))
     (cond[(not  (list? lst)) "please provide two objects and a list containing the first object"]
          [(empty? lst) empty]        
          [(eq? lst old) new]
          ;consider head is a list
          [else (if (list? (first lst))
               ;if head is a list
                    (if (and (list? old))
                         ;if old is a list and head is a list, then we need to check if the head of lst is the same as old
                         (if (equal? (first lst) old) (cons new (exchange old new (rest lst))) ; returns new, exchange rest of lst
                              ;else (head is not old)
                              (cons (exchange old new (first lst)) (exchange old new (rest lst))))
                         ;else old is not a list
                         (if (equal? (first lst) old) (cons new (exchange old new (rest lst)))
                              ;if head is old
                              (cons (exchange old new (first lst)) (exchange old new (rest lst)))))
               ;else head is not a list
                    (if (equal? (first lst) old) (cons new (exchange old new (rest lst)))
                    ;else head is not old
                         (cons (first lst) (exchange old new (rest lst)))))]))


;10/10
(define (all-exchange old-lst new-lst lst)      
     (cond[(not (and (list? old-lst) (list? new-lst) (list? lst))) "please provide three lists"]
          [(and(empty? old-lst)(empty? new-lst)) lst];both most be empty because other wise it may switch '() with '(b)
          [(empty? old-lst) (all-exchange old-lst (rest new-lst) (exchange old-lst (first new-lst) lst))]
          [(empty? new-lst) (all-exchange (rest old-lst) new-lst (exchange (first old-lst) new-lst lst))]
          [else (all-exchange (rest old-lst) (rest new-lst) (exchange (first old-lst) (first new-lst) lst))]))        


