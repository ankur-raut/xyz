#include<stdio.h>
#include<windows.h>

int main()
{ 
    HANDLE file = CreateFile("sample.txt", GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    if (file == INVALID_HANDLE_VALUE) printf("Failed to create file.");
    else printf("File Created Successfully.");
    return 0;
}