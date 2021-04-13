package experiment6;
import java.util.*;
class ArrayImp
{
	Scanner r=new Scanner(System.in);
	int array1[];
	ArrayImp()
	{
		System.out.println(" enter size ");
		int n = r.nextInt();
		array1=new int[n];
		
	}
	void enteritems( )
	{
		System.out.println("Enter numbers : ");
		for(int i=0;i<array1.length;i++)
		{
			array1[i]=r.nextInt();
		}
	}
	void min( )
	{
		int min = array1[0];
		for(int i = 0; i<array1.length; i++ ) 
		{
	         if(array1[i]<min) 
	         {
	            min = array1[i];
	         }
		}
		System.out.println(" Minimum : "+ min);
	}
	
	void scale( )
	{
		System.out.println(" Enter scale ");
		int s = r.nextInt(); 
		for( int i =0 ; i<array1.length; i++)
		{
			array1[i]=array1[i]*s;
		}
		System.out.println(" The array after multiplying scaling factor :");
		for( int i =0 ; i<array1.length; i++)
		{
			System.out.println(array1[i]);
		}
	}
}
public class ArrayOper 
{
	public static void main( String args[] )
	{
		ArrayImp a1 = new ArrayImp();
		a1.enteritems();
		a1.min();
		a1.scale();	
		System.exit(0);
	}
}
