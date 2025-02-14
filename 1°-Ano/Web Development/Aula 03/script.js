// var numero = 2;
// if (numero < 0) {
//     console.log(`${numero} é menor que 0.`)
// }
// else {
//     console.log(`${numero} é maior que 0.`)
// }
// (numero < 0) ? console.log(`${numero} é menor que 0.`) : console.log(`${numero} é maior que 0.`)
// var resultado = document.getElementById("resultado");
// function verifica_velocidade() {
//     var velocidade = parseInt(document.getElementById("velocidade").value);
//     var multa = 100;
//     if (velocidade <= 60) {
//         resultado.innerHTML = `Velocidade = ${velocidade}Km, sem multa!`;
//     }else {
//         multa *= (velocidade - 60);
//         resultado.innerText =  `Velocidade = ${velocidade}Km, acima do valor permitido multa de R$ ${multa}`; 
//     }
// }
let item = 'Queijo';
switch(item) {
    case 'Pão':
        console.log('é pão.'); 
        break;
    case 'Queijo':
        console.log('é queijo.');
        break;
    default:
        console.log('valor inválido.')
        break;
}