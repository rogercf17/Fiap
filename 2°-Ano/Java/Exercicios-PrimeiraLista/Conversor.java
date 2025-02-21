package Ex1PrimeiraLista;

public class Conversor {
    public static double calcularConversao(double valorEmMetros, int valor) {
        double valorConvertido = valorEmMetros * valor;
        return valorConvertido;
    }

    public static void saidaResultado(double m, double cm, double mm) {
        System.out.println("Metros: "+m+"\nCentímetros: "+cm+"\nMilímetros: "+mm);
    }
}
