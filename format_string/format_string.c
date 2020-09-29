#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>

int jackpot;

void fmt_str(void)
{
	char buf[128];
	puts("Give me a string to print");
	read(0, buf, 128);
	printf(buf);

	printf("jackpot @ %p = %d [0x%08x]\n", &jackpot, jackpot, jackpot);
	if (jackpot == 0x1337)
		puts("You won!");
	else
		puts("You lost :(");

}

int main(void)
{
	srand(time(0));
	setbuf(stdout, 0);

	jackpot = rand();
	fmt_str();	
	return 0;
}
