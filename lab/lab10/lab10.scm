(define (over-or-under num1 num2)
    (cond
        ((< num1 num2) -1)
        ((> num1 num2) 1)
        (else 0)
    )
)

(define (make-adder num)
    (lambda (inc) 
        (+ num inc))
)

(define (composed f g)
    (lambda (x) 
        (f (g x)))
)

(define lst 'YOUR-CODE-HERE)

(define (remove item lst) 'YOUR-CODE-HERE)
