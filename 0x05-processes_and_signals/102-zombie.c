#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * infinite_while - a function that creates an infinite loop to make
 * a program stall
 *
 * Return: 0 (Always for success)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - function that makes 5 zombie process
 *
 * Return: 0 on success
 */
int main(void)
{
	int i = 0;

	for (; i < 5; i++)
	{
		int pid = fork();

		if (pid == 0)
		{
			/*child proc*/
			printf("Zombie process created, PID: %i\n", getpid());

			exit(0);
		}
	}
	infinite_while();

	return (0);
}
