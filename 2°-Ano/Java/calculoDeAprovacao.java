import java.util.Scanner;

public class calculoDeAprovacao {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite a nota 1: ");
        double nota1 = scanner.nextDouble();

        System.out.print("Digite a nota 2: ");
        double nota2 = scanner.nextDouble();

        System.out.print("Digite a nota do trabalho: ");
        double trabalho = scanner.nextDouble();

        double ms = (nota1*0.4) + (nota2*0.4) + (trabalho*0.2);

        if (ms >= 7) {
            System.out.println("Aprovado com média "+ ms);
        }else {
            System.out.println(ms +" Você ficou de exame...");

            System.out.print("Digite a nota do exame final: ");
            double exame = scanner.nextDouble();

            double notaAprovacao = (ms+exame) / 2;

            if (notaAprovacao >= 5){
                System.out.print("Aprovado!! Você passou no exame");
            }else {
                System.out.print("Reprovado!! Você não passou no exame");
            }
        }

        scanner.close();
    }
}
