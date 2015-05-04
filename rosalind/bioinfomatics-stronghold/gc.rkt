#!/usr/bin/env racket
#lang racket

(define dna (make-hash))
(define current-label #f)
(define highest-label #f)
(define highest-value 0)

(define (read-fasta input)
  (let((this-line (read-line input)))
    (if (eof-object? this-line)
        #t
        (begin
          (if (char=? #\> (string-ref this-line 0))
              (let ((label (substring this-line 1)))
                (hash-set! dna label "")
                (set! current-label label))
              (let* ((dna-string (hash-ref dna current-label))
                     (new-dna-string (string-append dna-string this-line)))
                (hash-set! dna current-label new-dna-string)))
          (read-fasta input)))))

(call-with-input-file "./gc-data.txt" read-fasta)

(define (compute-highest-gc-content)
  (define (calc-gc-content s)
    (let ((all-len (string-length s))
          (gc-len (string-length
                   (string-replace (string-replace s "A" "") "T" ""))))
      (* 100.0 (/ gc-len all-len))))
  (hash-for-each dna
                 (lambda (k v)
                   (let ((gc-content (calc-gc-content v)))
                     (when (> gc-content highest-value)
                       (begin
                         (set! highest-label k)
                         (set! highest-value gc-content)))))))


(compute-highest-gc-content)
(display highest-label)
(newline)
(display highest-value)
(newline)
