public class Pessoa {
    private String nome;
    private int idade;

    // Construtor Padrão (sem parâmetros)
    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    // Construtor com parâmetros
    public Pessoa() {
        this.nome = "nome";
        this.idade = 0;
    }

    @Override
    public String toString() {
        return "Pessoa [nome=" + nome + ", idade=" + idade + "]";
    }

}


