//read
#include<stdio.h>
#include <fcntl.h>
#include<stdlib.h>
int main()
{
    int fd, sz;
    char *c = (char *) calloc(100, sizeof(char));

    fd = open("w.txt", O_RDONLY);
    if (fd < 0) { 
        perror("r1"); 
        exit(1); 
    }

    sz = read(fd, c, 5);
    printf("called read(% d, c, 5). returned that %d bytes were read.\n", fd, sz);

    c[sz] = '\0';
    printf("Those bytes are as follows: %s\n",c);
}