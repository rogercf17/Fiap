package Ex3PrimeiraLista;

public class Calculadora {
    public static double calcular(double valor1, double valor2, String operacao) {
        switch (operacao) {
            case "+":
                return valor1 + valor2;
            case "-":
                return valor1 - valor2;
            case "*":
                return valor1 * valor2;
            case "/":
                if (valor2 != 0.0) {
                    return valor1 / valor2;

                }else {
                    System.out.println("Erro: divisão por zero não permitida");
                    return Double.NaN;
                }
            default:
                System.out.println("Operação inválida, tente novamente");
                return Double.NaN;
        }
    }
}