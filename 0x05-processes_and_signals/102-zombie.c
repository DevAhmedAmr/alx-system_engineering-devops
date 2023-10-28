#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
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
		else if (pid > 0)
		{
			/*parent proc*/

			sleep(1);
		}
		else
		{
			fprintf(stderr, "failed");
		}
	}
	return (0);
}
