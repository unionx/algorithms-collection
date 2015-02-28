main.out : main.o

main.o : main.c
		cc -c main.c

clean :
		rm main.out main.o
