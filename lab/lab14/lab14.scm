(define (split-at lst n)
    (define (split-car lst n)
        (if (= n 0) nil
            (append (list(car lst)) (split-car (cdr lst) (- n 1)))))
    (define (split-cdr lst n)
        (if (= n 0) lst
            (split-cdr (cdr lst) (- n 1))))
    (if (< n (length lst)) (append (list(split-car lst n)) (split-cdr lst n))
        (list lst)))

(define (compose-all funcs)
    (if (null? funcs) (lambda (x) x)
        (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x)))))
        
