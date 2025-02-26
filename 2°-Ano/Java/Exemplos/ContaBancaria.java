public class ContaBancaria {
    private String titular;
    private double saldo;

    public ContaBancaria(String titular, double saldo) {
        this.titular = titular;
        this.saldo = saldo;
    }

    public void depositar(double valor) {
        this.saldo += valor;
    }

    public void sacar(double valor) {
        if (valor <= this.saldo) {
            this.saldo -= valor;
        }
    }

    @Override
    public String toString() {
        return "Conta - Titular: "+titular+" - Saldo: "+saldo;
    }

    public String getNome() {
        return this.titular;
    }

    public void setNome(String nome) {
        this.titular = nome;
    }
}
