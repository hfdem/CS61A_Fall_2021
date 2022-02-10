(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (ordered? s)
    (cond ((null? s) #t)
        ((= (length s) 1) #t)
        ((< (cadr s) (car s)) #f)
        (else (ordered? (cdr s)))))

(define (square x) (* x x))

(define (pow base exp) 'YOUR-CODE-HERE)
