#Ben Rapkin and Gawain Liu

C=gcc
CFLAGS= -g -pedantic -Wall -Wextra

all: decode 

decode: decode.c
	$(C) $(CFLAGS) -o decode decode.c workHorse.c -lm 
clean: decode 
	rm -f decode