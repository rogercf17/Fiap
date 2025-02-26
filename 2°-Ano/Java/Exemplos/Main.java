public class Main {
    public static void main(String[] args) {
        /*Pessoa pessoa1 = new Pessoa();
        Pessoa pessoa2 = new Pessoa("Carlos", 30);
        System.out.println(pessoa1);
        System.out.println(pessoa2);*/

        ContaBancaria conta1 = new ContaBancaria("Roger", 1000.0);
        ContaBancaria conta2 = new ContaBancaria("Maria", 2500.0);
        System.out.println(conta1+"\n"+conta2);

        conta1.depositar(500.0);
        conta1.sacar(1000.0);
        conta2.sacar(250.0);
        conta2.depositar(1000.0);
        conta1.setNome("Pedro");
        // System.out.println(conta1.getNome());
        System.out.println(conta1+"\n"+conta2);
    }
}
