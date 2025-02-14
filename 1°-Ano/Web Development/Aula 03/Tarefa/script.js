var resultado = document.getElementById("resultado");
function verifica_cargo() {
    var cargo = document.getElementById("cargo").value;
    var base = 3000;
    var salario = base;
    switch(cargo) {
        case 'Junior':
            salario = salario;
            break;
        case 'Pleno':
            salario *= 2;
            break;
        case 'Senior':
            salario *= 3;
            break;
        case 'Techlead':
            salario *= 4;
            break;
        case 'Diretor':
            salario *= 5;
            break;
        default:
            resultado.innerText = 'Valor inválido';
            break;
    }
    resultado.innerText = `Você é ${cargo} e ganhará R$ ${salario}.`;
}