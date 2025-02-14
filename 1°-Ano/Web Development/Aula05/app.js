const lista = [1, 12, 10, 5];
const lista_nomes = ['Eduardo', 'Giovanni', 'Parra', 'Rodrigo', 'Roger']
// console.log(`Lista inicial: ${lista}`);

// Adicionar um item ao final do array
lista.push(30);
// console.log(`Push: ${lista}`);

//Remover um ultimo item do array
lista.pop();
// console.log(`Pop: ${lista}`);

//Adicionar um item na primeira posição do array
lista.unshift(8);
// console.log(`Unshift: ${lista}`);

// Remover o primeiro item do array
lista.shift();
// console.log(`Shift: ${lista}`);

// Atualizar o valor de um array
lista[1] += 5;
// console.log(`Atualizando o valor da pos.1: ${lista}`);

// lista_nomes.forEach(
//     function passarNomes(nome) {
//         console.log(`Olá ${nome.toUpperCase()}`);
//     }
// );
// console.log()
// lista_nomes.forEach(nome => console.log(`Olá ${nome.toLowerCase()}`));
// console.log()
// lista_nomes.forEach(nome => console.log(`${nome === 'Roger'?'Olá Roger':'Você não é o Roger!'}`));
// console.log();
// function vaiCorinthians() {
//     return lista_nomes.map(nome => nome + ' Vai Corinthians!!!');
// }
// console.log(vaiCorinthians(['Rafael', 'João Pedro']));

// const filmes = [
//     {
//         nome: "Gente Grande",
//         diretor: "Adam Sandler",
//         ano: 2012
//     },
//     {
//         nome: "Todo mundo em pânico",
//         diretor: "Steven Spilberg",
//         ano: 2006 
//     },
//     {
//         nome: "Meninas Malvadas",
//         diretor: "Lindsey Lohan",
//         ano: 2002
//     }
// ]

// console.log(filmes.filter(filme => filme.ano > 2007));