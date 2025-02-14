function escolhaComp() {
    const jokeipo = ['Pedra', 'Papel', 'Tesoura'];
    var numeroAleatorio = Math.floor(Math.random() * 3);
    return jokeipo[numeroAleatorio];
}

function jogar(escolhaJogador) {
    var comp = escolhaComp();
    var resultado = '';
    console.log(escolhaComp());
    console.log(escolhaJogador);

    if (escolhaJogador === comp) {
        resultado = 'Empate!';
    }else if (escolhaJogador === 'Pedra' && comp === 'Papel') {
        resultado = 'Computador ganhou!';
    }else if (escolhaJogador === 'Pedra' && comp === 'Tesoura') {
        resultado = 'Usuário ganhou!';
    }

    document.getElementById('resultado').innerText = resultado;
}