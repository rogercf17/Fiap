package Ex5PrimeiraLista;
import java.util.Scanner;

public class Ex5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Area area = new Area();

        double comprimento = entradaValores(scanner, "Digite o comprimento do terreno: ");
        double largura = entradaValores(scanner, "Digite a largura do terreno: ");

        double resultado = area.calcular(comprimento, largura);
        System.out.println("A área do terreno é igual "+resultado+"m²");
    }
    private static double entradaValores(Scanner scanner, String mensagem) {
        System.out.print(mensagem);
        return scanner.nextDouble();
    }
}
