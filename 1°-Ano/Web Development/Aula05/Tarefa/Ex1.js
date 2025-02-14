const lista = [1, 2, 3, 4, 5];

function dobrarNumerosDaLista(listaDobrada) {
    return listaDobrada.map(numero => numero * 2);
}
const listaDobrada = dobrarNumerosDaLista(lista);

console.log(`Lista original: ${lista}\nLista original dobrada: ${listaDobrada}`)