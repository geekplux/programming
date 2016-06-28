(define (sqrt x)
  (define (average n1 n2)
    (/ (+ n1 n2) 2))
  (define (square guess)
    (* guess guess))
  (define (improve guess)
    (average guess (/ x guess)))
  (define (good-enough? old-guess new-guess)
    (> 0.01 (/ (abs (- new-guess old-guess))
               old-guess)))
  (define (try guess)
    (if (good-enough? guess (improve guess))
        ;; exact->inexact 转化为浮点小数
        (exact->inexact guess)
        (try (improve guess))))
  (try 1))

(sqrt 36)