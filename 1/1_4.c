//write

#include<stdio.h>
#include<stdlib.h>
#include <fcntl.h>
main()
{
    int sz;
    int fd = open("higuys.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd < 0)
    {
    perror("r1");
    exit(1);
    }
    sz = write(fd, "hello guys\n", strlen("hello"));
    printf("called write(% d, \"hello geeks\\n\", %d). It returned %d\n", fd, strlen("hello geeks\n"), sz);
    close(fd);
}