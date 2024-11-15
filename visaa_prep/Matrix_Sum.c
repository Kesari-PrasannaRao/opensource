#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n,i,j,k,sr,sc;
    scanf("%d",&n);
    int a[n][n];
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    for(i=0;i<n;i++)
    {
        sr=0,sc=0;
        for(j=0;j<n;j++)
        {
            sr=sr+a[i][j];
        }
        for(k=0;k<n;k++)
        {
            sc=sc+a[k][i];
        }
        printf("%d ",sr+sc);
    }
    return 0;
}
