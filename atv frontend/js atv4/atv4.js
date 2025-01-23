function getById(id){
    return document.getElementById(id);
}

let exibircaixa = getById('exibircaixa');
let ocultarcaixa = getById('ocultarcaixa');
let resultado = getById('resultado');

exibircaixa.addEventListener('click', () =>{
    resultado.style.visibility = 'visible';
});

ocultarcaixa.addEventListener('click', () =>{
    resultado.style.visibility = 'hidden';
});