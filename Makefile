# variables
objects = main.o

main.out : $(objects)
		cc -o main.out $(objects)

# we can omit the *.c file
main.o : main.c
		cc -c main.c

.PHONY : clean

clean :
		-rm main.out $(objects)
