(define (my-filter func lst)
  (cond ((null? lst) '())
    ((func (car lst)) (cons (car lst) (my-filter func (cdr lst))))
    (else (my-filter func (cdr lst)))))

(define (interleave s1 s2) 'YOUR-CODE-HERE)

(define (accumulate merger start n term)
  'YOUR-CODE-HERE)

(define (no-repeats lst) 'YOUR-CODE-HERE)
