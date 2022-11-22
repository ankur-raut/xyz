#include<stdio.h>
#include<fcntl.h>
#include<errno.h>

int errno;

int main(){
    int sz;
    int fd = open("w.txt",O_WRONLY | O_CREAT );
    
    printf("%d",fd);

    if(fd==-1){
        printf("%d",errno);
        perror("error");
    }
    sz = write(fd,"hwlloe guys",strlen("hellow"));
    printf("%d",fd);
    close(fd);

    return 0;
}