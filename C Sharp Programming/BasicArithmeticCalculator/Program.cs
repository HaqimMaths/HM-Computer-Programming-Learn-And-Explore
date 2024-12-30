namespace BasicArithmeticCalculator{
  class Program{
    static void Main(string[] args){
      double a;
      double b;
      char operation;
      double result;
      System.Console.WriteLine("Enter any real numbers for a: ");
      a = double.Parse(Console.ReadLine());
      System.Console.WriteLine("Enter any real numbers for b: ");
      b = double.Parse(Console.ReadLine());
      System.Console.WriteLine("Enter an operation: (+ - * / %): ");
      operation = char.Parse(Console.ReadLine());
      switch(operation){
        case '+':
          result = a + b;
          break;
        case '-':
          result = a - b;
          break;
        case '*':
          result = a * b;
          break;
        case '/':
          result = a / b;
          break;
        case '%':
          result = (int) a / (int) b;
          break;
        default:
          result = -1;
          break;
      }
      System.Console.WriteLine($@"
      The result of your {a} {operation} {b} is:
          {result:F2}
      ");
    }
  }
}