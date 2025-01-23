function getById(id){
    return document.getElementById(id);
}

let nometag = getById('nometag');
let conteudotag = getById('conteudotag');
let mostratag = getById('mostratag');
let resultado = getById('resultado');

mostratag.addEventListener('click',function(){
    let taguser = nometag.value;
    let conteudo = conteudotag.value;

    if (taguser && conteudo){
        let tagnew = document.createElement(taguser);

        tagnew.innerHTML = conteudo;

        resultado.appendChild(tagnew);

    }

})