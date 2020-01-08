#include<stdio.h>
int main()
{
    int n, i;
    printf("Enter an Integer Number : ");
    scanf("%d", &n);
    for(i=2; i<=n/2; i++)
    {
        if(n%i==0)
        {
            break;
        }
    }
    if(i>n/2)
        printf("%d is PRIME",n);
    else
        printf("%d is NOT PRIME", n);
}