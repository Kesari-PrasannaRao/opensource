#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n,m,i,s1=0,s2=0;
    scanf("%d %d",&n,&m);
    int a[n];
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++)
    {
        if(a[i]%m==0)
        {
            s1=s1+a[i];
        }
        else
        {
            s2=s2+a[i];
        }
    }
    printf("%d",s1-s2);
    return 0;
}
