#include <stdio.h>
int main()
{
   FILE *fr;
   char s[40];
   int n;
   fr = fopen("test.txt", "w");
   printf("Enter a string and a number");
   scanf("%s%d", s, &n); /*read from keyboard*/
   fprintf(fr, "%s %d", s, n); /*  write to file*/
   fclose(fr);
   fr = fopen("test.txt", "r");
   fscanf(fr, "%s%d", s, &n); /*read from file*/
   printf("%s %d", s, n); /*display on screen*/
   fclose(fr);
   return 0;
}
 
output:
enter a string and a number
jeevan
12597