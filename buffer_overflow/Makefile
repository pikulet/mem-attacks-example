.PHONY: all clean

all: buffer_overflow

buffer_overflow: buffer_overflow.c
	gcc buffer_overflow.c -o buffer_overflow -g -fno-stack-protector -z execstack

clean:
	rm buffer_overflow
