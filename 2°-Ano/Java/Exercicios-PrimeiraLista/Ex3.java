package Ex3PrimeiraLista;
import java.util.Scanner;
import static java.lang.Double.NaN;

public class Ex3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Calculadora calculadora = new Calculadora();

        double valor1 = entrada(scanner, "1");
        double valor2 = entrada(scanner, "2");
        String operacao = entradaOperacao(scanner);

        double resultado = calculadora.calcular(valor1, valor2, operacao);

        saidaResultado(resultado,valor1,valor2,operacao);

        scanner.close();
    }

    private static double entrada(Scanner scanner, String numero) {
        System.out.print("Digite o "+numero+"° valor: ");
        return scanner.nextDouble();
    }

    private static String entradaOperacao(Scanner scanner) {
        System.out.print("Digite o símbolo da operação que deseja realizar: ");
        return scanner.next();
    }

    private static void saidaResultado(double re, double v1, double v2, String o) {
        System.out.println(v1+" "+o+" "+v2+" = "+re);
    }
}