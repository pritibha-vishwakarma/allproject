//Student Grade Calculator

import java.util.Scanner;

class result
{
    public static void main(String[] args) 
    {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter Marks of Physics:");
        double Physics=sc.nextDouble();
        System.out.print("Enter Marks of Hindi:");
        double Hindi=sc.nextDouble();
        System.out.print("Enter Marks of Maths:");
        double Maths=sc.nextDouble();
        System.out.print("Enter Marks of English:");
        double English=sc.nextDouble();
        System.out.print("Enter Marks of Biology:");
        double Biology=sc.nextDouble();

        double total = Physics+Hindi+Maths+English+Biology;
        double per=total/5;
        System.out.println("Total Marks="+total);
        System.out.println("Percentage="+per);
        if(per>=33)
        {
            if(per>=45)
            {
                if(per>=60)
             {
            System.out.println("Grade A");
            
             }
         }
         else
         {
            System.out.println("Grade B");
         }
        }
         else
         {
            System.out.println("Grade C");
         
        }
    }  
}


            
        
        
        

        

    

