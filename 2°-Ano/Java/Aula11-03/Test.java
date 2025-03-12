class Test {
    public static void main(String[] args) {
        Calculadora calc = new Calculadora();
        System.out.println("Soma: " + calc.soma(2, 3));  // Saída: 5
        System.out.println("Soma: " + calc.soma(2, 3, 4));  // Saída: 9
        System.out.println("Soma: " + calc.soma(2.5, 3.5));  // Saída: 6.0

        System.out.println("Subtração: " + calc.subtrair(5, 3));  // Saída: 2
        System.out.println("Subtração: " + calc.subtrair(10, 4, 2));  // Saída: 4
        System.out.println("Subtração: " + calc.subtrair(5.5, 3.2));  // Saída: 2.3

        System.out.println("Multiplicação: " + calc.multiplicar(2, 3));  // Saída: 6
        System.out.println("Multiplicação: " + calc.multiplicar(2, 3, 4));  // Saída: 24
        System.out.println("Multiplicação: " + calc.multiplicar(2.5, 4.0));  // Saída: 10.0

        System.out.println("Divisão: " + calc.dividir(6, 3));  // Saída: 2
        System.out.println("Divisão: " + calc.dividir(12, 4, 2));  // Saída: 1
        System.out.println("Divisão: " + calc.dividir(7.0, 2.0));  // Saída: 3.5
    }
}