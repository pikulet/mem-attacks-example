.PHONY: all clean

all: format_string

format_string: format_string.c
	gcc format_string.c -o format_string -g -Wno-format-security -fno-stack-protector

clean:
	rm format_string
