#!/usr/bin/env racket
#lang racket

(define n 36)
(define k 3)


(define (produce-rabbits total-month multiple)
  (define (produce-result month big-cnt small-cnt)
    (if (= 1 month)
        (+ big-cnt small-cnt)
        (produce-result (sub1 month)
                        (+ big-cnt small-cnt)
                        (* big-cnt multiple))))
  (produce-result total-month 0 1))

(display (produce-rabbits n k))
(newline)
