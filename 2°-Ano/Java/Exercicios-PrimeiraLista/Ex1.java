package Ex1PrimeiraLista;

import java.util.Scanner;

public class Ex1 {
    public static void main(String[] args) {
        Conversor conversor = new Conversor();

        double metros = realizarEntradaValor("Digite o valor em metros: ");
        double centimetros = conversor.calcularConversao(metros, 100);
        double milimetros = conversor.calcularConversao(metros, 1000);
        conversor.saidaResultado(metros, centimetros, milimetros);
    }

    private static double realizarEntradaValor(String valorInput) {
        Scanner scanner = new Scanner(System.in);
        System.out.print(valorInput);
        double valor = scanner.nextDouble();
        scanner.close();
        return valor;
    }


}