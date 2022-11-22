#include<stdio.h>
#include<windows.h>

int main()
{ 
    HANDLE file = CreateFile("sample.txt", GENERIC_WRITE, FILE_SHARE_READ, NULL, OPEN_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    DWORD dwBytesWritten;
    BOOLEAN text = WriteFile(file,"Hello World!!\n", strlen("Hello World!!\n"), &dwBytesWritten, NULL);
    if (text) printf("Written in File Successfully.");
    else printf("Failed to write in file.");
    return 0; 
}