public class Calculadora {

    int soma(int a, int b) {
        return a + b;
    }

    int soma(int a, int b, int c) {
        return a + b + c;
    }

    double soma(double a, double b) {
        return a + b;
    }

    int subtrair(int a, int b) {
        return a - b;
    }

    int subtrair(int a, int b, int c) {
        return a - b - c;
    }

    double subtrair(double a, double b) {
        return a - b;
    }

    int multiplicar(int a, int b) {
        return a * b;
    }

    int multiplicar(int a, int b, int c) {
        return a * b * c;
    }

    double multiplicar(double a, double b) {
        return a * b;
    }

    int dividir(int a, int b) {
        if (b == 0) {
            System.out.println("Erro: Divisão por zero!");
            return 0;
        }
        return a / b;
    }

    int dividir(int a, int b, int c) {
        if (b == 0 || c == 0) {
            System.out.println("Erro: Divisão por zero!");
            return 0;
        }
        return a / b / c;
    }

    double dividir(double a, double b) {
        if (b == 0) {
            System.out.println("Erro: Divisão por zero!");
            return 0;
        }
        return a / b;
    }
}