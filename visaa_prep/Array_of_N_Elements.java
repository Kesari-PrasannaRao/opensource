import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        int n,i;
        n=s.nextInt();
        System.out.print("[");
        for(i=0;i<n;i++)
        {
            if(i!=n-1)
            {
                System.out.print(i+", ");
            }
            else
            {
                System.out.print(i);
            }
        }
        System.out.print("]");
    }
}
