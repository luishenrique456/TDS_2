function getById(id){
    return document.getElementById(id);

}
//  1 questão usando keyup

let texto_original = getById('texto_original');
texto_original.addEventListener('keyup',()=>{
    texto_detinatario = getById('texto_destinatario');
    texto_detinatario.value = texto_original.value;

});

// 2 questão convertendo para maiúsculo .toUpperCase();

let caixa_original = getById('caixa_original');
caixa_original.addEventListener('keyup',()=>{
    caixa_destino = getById('caixa_destino')
    caixa_destino.value = caixa_original.value.toUpperCase();;

})
