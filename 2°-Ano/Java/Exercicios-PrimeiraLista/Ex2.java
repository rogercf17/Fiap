package Ex2PrimeiraLista;
import java.util.Scanner;

public class Ex2 {
    public static void main(String[] args) {
        Conversor conversor = new Conversor();
        double fahrenheit = entradaDeDados("Digite a temperatura em Fahrenheit: ");
        double celsius = conversor.conversor(fahrenheit);
        saidaDeDados(fahrenheit, celsius);
    }

    private static double entradaDeDados(String input) {
        Scanner scanner = new Scanner(System.in);
        System.out.print(input);
        double fah = scanner.nextDouble();
        scanner.close();
        return fah;
    }

    private static void saidaDeDados(double valorFahrenheit, double valorCelsius) {
        System.out.println("Fahrenheit "+valorFahrenheit+" -> "+valorCelsius+" Celsius");
    }
}
