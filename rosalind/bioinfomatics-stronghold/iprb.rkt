#!/usr/bin/env racket
#lang racket

(define XX 19)
(define Xx 25)
(define xx 17)
(define total (+ XX Xx xx))


(define two-Xx-rate
  (* (/ Xx total)
     (/ (sub1 Xx) (sub1 total))))

(define two-xx-rate
  (* (/ xx total)
     (/ (sub1 xx) (sub1 total))))

(define xx-with-Xx-rate
  (+ (* (/ Xx total)
        (/ xx (sub1 total)))
     (* (/ xx total)
        (/ Xx (sub1 total)))))


(define two-Xx-recessive-rate 0.25)

(define two-xx-recessive-rate 1.00)

(define xx-with-Xx-recessive-rate 0.50)

(define total-dom-rate
  (- 1.00
     (+ (* two-Xx-rate two-Xx-recessive-rate)
        (* two-xx-rate two-xx-recessive-rate)
        (* xx-with-Xx-rate xx-with-Xx-recessive-rate))))

(display total-dom-rate)
(newline)
