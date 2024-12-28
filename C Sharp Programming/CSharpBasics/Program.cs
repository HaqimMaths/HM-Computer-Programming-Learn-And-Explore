/*
 * Section: C# Basics (Part One)
 * Topic: Basics syntax
 * By: Haqim Maths
 * Programmed on: 29th December 2024
*/

using Integer = int;

namespace HM.CSharp.Basics
{
 class Program
 {
  decimal sumOf(decimal a, decimal b)
  {
   return a + b;
  }
  static void printHelloWorld()
  {
   System.Console.WriteLine("Hello World!");
  }
  static double divideTwoNumbers(double a, double b)
  {
   return a / b;
  }
  static void specifiedOperations()
  {
   int a = -1;
   int b = 4;
   int c = 6;
   System.Console.WriteLine("The sum of a, b & c is: " + (a + b + c));
   long d = 35L;
   long e = 5L;
   long f = 7L;
   System.Console.WriteLine("The result of (35 + 5) % 7 is: " + ((d + e) % 7));
   double g = 14.0;
   double h = -4.0;
   double i = 6.0;
   double j = 11.0;
   System.Console.WriteLine("The result of 14 + -4 * 6 / 11 is: " + (g + h * i / j));
   decimal ax = 2M;
   decimal bx = 15M;
   decimal cx = 6M;
   decimal dx = 1;
   decimal ex = 7;
   decimal fx = 2;
   System.Console.WriteLine("The result of (2 + 15 / 16 * 1 - 7 % 2) is: " + (ax + bx / cx * dx - ex % fx));
  }
  static void swapNum(int a, int b)
  {
   int temp;
   System.Console.WriteLine("Before swapping: a = " + a + " & b = " + b);
   temp = a;
   a = b;
   b = temp;
   System.Console.WriteLine("After swapping: a = " + a + " & b = " + b);
  }
  static long multiplyThreeNumbers(long a, long b, long c)
  {
   return a * b * c;
  }
  static void arithmeticOperations(Integer a, Integer b)
  {
   System.Console.WriteLine("The sum of 10 & 20 is: " + (a + b));
   System.Console.WriteLine("The difference of 10 & 20 is: " + (a - b));
   System.Console.WriteLine("The product of 10 & 20 is: " + (a * b));
   System.Console.WriteLine("The division of 10 & 20 is: " + (a / b));
   System.Console.WriteLine("The remainder of 10 & 20 is: " + (a % b));
  }
  static void multiplicationTableUntilTen(Integer a)
  {
   for(Integer i = 0; i <= 10; i++)
   {
    System.Console.WriteLine(a + " * " + i + " = " + (a * i));
   }
  }
  static void averageOfFourNumbers(decimal a, decimal b, decimal c, decimal d)
  {
   decimal average = (a + b + c + d) / 4;
   System.Console.WriteLine("The average of a, b, c, and e is: " + average);
  }
  static void specifiedFormula(long a, long b, long c)
  {
   System.Console.WriteLine("The result of specified numbers " + a + ", " + b + " & " + c + " is: " + (a + b) * c);
   System.Console.WriteLine("And a * b + b * c is: " + (a * b + b * c));
  }
  static void Main(string[] args)
  {
   Program program = new Program();
   printHelloWorld();
   System.Console.WriteLine("The sum of 1.212 & 12.123 is: " + program.sumOf(1.212M, 12.123M));
   System.Console.WriteLine("The divide of 10 / 2 is: " + divideTwoNumbers(10, 2));
   specifiedOperations();
   swapNum(10, 20);
   System.Console.WriteLine(multiplyThreeNumbers(10L, 20L, 30L));
   System.Console.WriteLine("Test arithmetic operations!");
   System.Console.Write("Input the first number: ");
   Integer a = Integer.Parse(System.Console.ReadLine());
   System.Console.Write("Input the second number: ");
   Integer b = int.Parse(System.Console.ReadLine());
   arithmeticOperations(a, b);
   System.Console.Write("Input the number to generate multiplication table: ");
   Integer c = int.Parse(System.Console.ReadLine());
   multiplicationTableUntilTen(c);
   System.Console.WriteLine("Test average of four numbers!");
   System.Console.Write("Input the first number: ");
   decimal d = decimal.Parse(System.Console.ReadLine());
   System.Console.Write("Input the second number: ");
   decimal e = decimal.Parse(System.Console.ReadLine());
   System.Console.Write("Input the third number: ");
   decimal f = decimal.Parse(System.Console.ReadLine());
   System.Console.Write("Input the fourth number: ");
   decimal g = decimal.Parse(System.Console.ReadLine());
   averageOfFourNumbers(d, e, f, g);
   specifiedFormula(19L, 20L, 21L);
  }
 }
}