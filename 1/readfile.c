#include<stdio.h>
#include<windows.h>

int main()
{ 
    char *c = (char *) calloc(100, sizeof(char));
    HANDLE file = CreateFile("sample.txt", GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    DWORD dwBytesRead;
    if (ReadFile(file, c, 256, &dwBytesRead, NULL)) 
    {
        c[dwBytesRead]='\0';
        printf("Contents of file are:\n");
        printf("%s" ,c);
    }
    else printf("Failed to read file.");
    return 0; 
}