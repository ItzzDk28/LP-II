public class Calculator {
   public static Integer add(Integer num1, Integer num2) {
        return num1 + num2;
    }
    
    public static Integer subtract(Integer num1, Integer num2) {
        return num1 - num2;
    }
    
    public static Integer multiply(Integer num1, Integer num2) {
        return num1 * num2;
    }
    
    public static Decimal divide(Integer num1, Integer num2) {
        if(num2 == 0) {
            throw new System.MathException('Cannot divide by zero');
        }
        return num1 / num2;
    }
}



Debug Code - 

Integer result = Calculator.add(5, 3);
System.debug('Addition: ' + result);

result = Calculator.subtract(10, 4);
System.debug('Subtraction: ' + result);

result = Calculator.multiply(6, 2);
System.debug('Multiplication: ' + result);

Decimal divisionResult = Calculator.divide(20, 5);
System.debug('Division: ' + divisionResult);
