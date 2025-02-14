const btnCriar = document.querySelector('#btnCriar');
const listaFilmes = document.querySelector('#listaFilmes');
const filmeDigitado = document.querySelector('#inputUsuario');

btnCriar.addEventListener('click', function (infosDoEvento) {
    infosDoEvento.preventDefault();

    let novoFilme = document.createElement('li');
    novoFilme.innerHTML = filmeDigitado.value;

    let btnEditar = document.createElement('button');
    btnEditar.innerText = 'Editar';
    btnEditar.addEventListener('click', function() {
        // novoFilme.style.color = 'blue';
        novoFilme.classList.toggle('item-lista');
    });
    
    novoFilme.append(btnEditar);
    listaFilmes.append(novoFilme);

    novoFilme.innerHTML = `
        <h1>${filmeDigitado.value}</h1>
        <p>Avaliação: xxxx</p>
        <span>Só o básico</span>
    `;

    let imagem = document.createElement('img');
    img.src="Link da imagem";

    filmeDigitado.value = '';
});

  // console.log(infosDoEvento);
    // console.log(infosDoEvento.target);
    // console.log(infosDoEvento.target.id);
    // console.log(infosDoEvento.target.parentNode.id);