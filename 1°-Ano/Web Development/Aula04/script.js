function somar(num1, num2) {
    return num1 + num2;
}

function printarNaTela() {
    let num1 = parseInt(document.getElementById("num1").value);
    let num2 = parseInt(document.getElementById("num2").value);
    var resultado = somar(num1, num2);
    console.log(resultado);
}

function limparTela() {
    document.getElementById('num1').value='';
    document.getElementById('num2').value='';
}

const pessoas = ['Caio', 'Fulano', 'Cliclano', true, 15];
console.log(pessoas[0]);
console.log(pessoas.length);
console.log(typeof pessoas[1]);
console.log(typeof pessoas[3]);
console.log(typeof pessoas[4]);;