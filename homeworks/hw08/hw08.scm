(define (my-filter func lst)
  (cond ((null? lst) '())
    ((func (car lst)) (cons (car lst) (my-filter func (cdr lst))))
    (else (my-filter func (cdr lst)))))

(define (interleave s1 s2)
  (cond ((null? s1) s2)
    ((null? s2) s1)
    (else (append (list (car s1)) (list (car s2)) (interleave (cdr s1) (cdr s2))))))

(define (accumulate merger start n term)
  (if (= n 0) start
    (accumulate merger (merger start (term n)) (- n 1) term)))

(define (no-repeats lst)
  (if (null? lst) lst
    (append (list (car lst)) (no-repeats (my-filter (lambda (x) (not (= x (car lst)))) lst)))))