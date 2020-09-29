#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFSIZE 64

char buf1[BUFSIZE], buf2[BUFSIZE];

void bof(FILE * fd1, FILE * fd2)
{
	int idx1, idx2, idx;
	int byte_read1, byte_read2;
	char buf[BUFSIZE];

	memset(buf, BUFSIZE, 0);
	byte_read1 = fread(buf1, 1, BUFSIZE, fd1);
	byte_read2 = fread(buf2, 1, BUFSIZE, fd2);

	buf1[BUFSIZE-1] = 0;
	buf2[BUFSIZE-1] = 0;

	if(byte_read1 != byte_read2)
	{
		printf("Reading different number of bytes from ./exploit1 and ./exploit2!\n");
		return;
	}

	printf("Buffer starts at: %p\n", buf);
	for(idx = 0; idx < byte_read1 + byte_read2; idx++)
	{
		idx1 = (idx % 2) ? BUFSIZE - 1 : idx / 2;
		idx2 = (idx % 2) ? idx / 2 : BUFSIZE - 1;
		buf[idx] = buf1[idx1] + buf2[idx2];
	}

}

int main(void)
{

	FILE *fd1, *fd2;

	fd1 = fopen("./exploit1", "r");
	fd2 = fopen("./exploit2", "r");

	if (!fd1 || !fd2)
		puts("Error opening ./exploit1 or ./exploit2");
	else
		bof(fd1, fd2);

	return 0;
}
