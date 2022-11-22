#include<stdio.h>
#include<windows.h>

int main()
{ 
    HANDLE file = CreateFile("sample.txt", GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    printf("File Created Successfully.\n");
    if (CloseHandle(file) ==-1) printf("Failed to close.");
    else printf("File Closed Successfully.");
    return 0; 
}