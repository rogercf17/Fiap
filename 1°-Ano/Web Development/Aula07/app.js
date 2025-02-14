const btnCriar = document.querySelector("#btnCriar");
const listaFilmes = document.querySelector('#listaFilmes');
const inputUsuario = document.querySelector('#inputUsuario');
const inputAno = document.querySelector('#inputAno');
const inputDiretor = document.querySelector('#inputDiretor');

const filmes = [
    {
        nome: "Tropa de Elite",
        ano: "05/10/2008",
        diretor: "José Padilha"
    },
    {
        nome:"Carros",
        ano: "30/06/2006",
        diretor:"John Lasseter"
    },
    {
        nome: "Titanic",
        ano: "1997-01-16",
        diretor: "James Cameron"
    },
    {
        nome: "The Batman",
        ano: "03/03/2022",
        diretor: "Matt Reeves"
    }
];

btnCriar.addEventListener('click', function (infosDoEvento) {
    infosDoEvento.preventDefault();

    criarFilme();
})

// Criar
function criarFilme() {
    // 1 - Pegar os dados digitados
    let filme = {
        nome: inputUsuario.value,
        ano: inputAno.value,
        diretor: inputDiretor.value
    };

    // 2 - Armazenar
    filmes.unshift(filme);

    // 3 - Atualizar o DOM
    renderizarNaTela();
}

// Ler
window.onload = renderizarNaTela();
function renderizarNaTela() {
    listaFilmes.innerHTML = "";
    filmes.forEach(
        filme => {
            let novoFilme = document.createElement('li');
            novoFilme.innerHTML = `
                <h2>${filme.nome}</h2>
                <p>Lançamento: ${filme.ano}</p>
                <p>Diretor: ${filme.diretor}</p>
                <br>
                <br>
                <button id="criar" onclick="editarFilme(${filmes.indexOf(filme)})"> Editar </button>
                <button id="apagar" onclick="apagarFilme(${filmes.indexOf(filme)})"> Apagar </button>
            `;

            listaFilmes.append(novoFilme);
        }
    );
}

// Atualizar
function editarFilme(id) {
    // 1 - Selecionar o filme

    // 2 - Pegar as informações que a pessoa inserir
    let tituloModificado = prompt("Digite o novo nome do filme",filmes[id].nome);

    // 3 - Mudar informações
    filmes[id].nome = tituloModificado;

    // 4 - Atualizar a tela
    renderizarNaTela();
}

// Deletar
function apagarFilme(id) {
    // 1 - Selecionar o filme

    // 2 - Apagar filme
    filmes.splice(id, 1);

    // 3 - Atualizar a tela
    renderizarNaTela();
}

const date = new Date()
console.log(date.toLocaleString())