//open
#include<stdio.h>
#include<fcntl.h>
#include<errno.h>
int errno;
int main()
{
// if file does not have in directory
// then file foo.txt is created.
int fd = open("w.txt",O_RDONLY | O_CREAT);
printf("fd = %d/n", fd);
if (fd ==-1)
{
// print which type of error have in a code
printf("Error Number % d\n", errno);
// print program detail "Success or failure"
perror("Program");
}
return 0;
}