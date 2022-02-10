(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (ordered? s)
    (cond ((null? s) #t)
        ((= (length s) 1) #t)
        ((< (cadr s) (car s)) #f)
        (else (ordered? (cdr s)))))

(define (square x) (* x x))

(define (pow base exp)
    (cond ((= exp 1) base)
        ((even? exp) (square (pow base (/ exp 2))))
        (else (* base (square (pow base (/ (- exp 1) 2)))))))