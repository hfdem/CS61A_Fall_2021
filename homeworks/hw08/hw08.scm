(define (my-filter func lst)
  (cond ((null? lst) '())
    ((func (car lst)) (cons (car lst) (my-filter func (cdr lst))))
    (else (my-filter func (cdr lst)))))

(define (interleave s1 s2)
  (cond ((null? s1) s2)
    ((null? s2) s1)
    (else (append (list (car s1)) (list (car s2)) (interleave (cdr s1) (cdr s2))))))

(define (accumulate merger start n term)
  'YOUR-CODE-HERE)

(define (no-repeats lst) 'YOUR-CODE-HERE)
