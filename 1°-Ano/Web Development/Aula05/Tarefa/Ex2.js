const listaStringsMinusculo = ['oi', 'tudo', 'bem?'];

function transformarStringsEmMaisculas (letrasMaiusculas) {
    return letrasMaiusculas.map(string => string.toUpperCase());
}
const ListaStringsMaiusculo = transformarStringsEmMaisculas(listaStringsMinusculo);

console.log(`Frase em minusculo: ${listaStringsMinusculo}\nFrase em maiusculo: ${ListaStringsMaiusculo}`);