var resultado = document.getElementById('resultado');

function somar() {
    // Entrada
    var numero1 = parseFloat(document.getElementById('numero1').value);
    var numero2 = parseFloat(document.getElementById('numero2').value);

    // Processamento
    var soma = numero1 + numero2;

    // Saída
    resultado.innerText = `${numero1} + ${numero2} = ${soma}`;
}

function subtrair() {
    var numero1 = parseFloat(document.getElementById('numero1').value);
    var numero2 = parseFloat(document.getElementById('numero2').value);

    var subtrair = numero1 - numero2;

    resultado.innerText = `${numero1} - ${numero2} = ${subtrair}`;
}

function multiplicar() {
    var numero1 = parseFloat(document.getElementById('numero1').value);
    var numero2 = parseFloat(document.getElementById('numero2').value);

    var multiplicar = numero1 * numero2;

    resultado.innerText = `${numero1} x ${numero2} = ${multiplicar}`;
}

function dividir() {
    var numero1 = parseFloat(document.getElementById('numero1').value);
    var numero2 = parseFloat(document.getElementById('numero2').value);

    if (numero2 === 0) {
        resultado.innerText = 'Impossível dividir por 0'
    }
    else {
        var dividir = numero1 / numero2;
        resultado.innerText = `${numero1} / ${numero2} = ${dividir}`;
    }
}

function limparTela() {
    document.getElementById("numero1").value = '';
    document.getElementById("numero2").value = '';
    resultado.innerText = '';
}