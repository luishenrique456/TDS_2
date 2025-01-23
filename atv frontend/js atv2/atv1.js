var botao1 = document.getElementById('botao1');
botao1.addEventListener('click', cliqueDoBotao1);

function cliqueDoBotao1(){
    var resultado1 = document.getElementById('resultado1');
    resultado1.innerHTML = 'olá, Boa tarde!';
}

var botao2 = document.getElementById('botao2');
botao2.addEventListener('click',cliqueDoBotao2);

function cliqueDoBotao2(){
    var resultado2 = document.getElementById('resultado2');
    resultado2.innerHTML = 'boa noite! (:';
}

// caixa de texto
var botao3 = document.getElementById('botao3');
botao3.addEventListener('click',clickcaixatexto);

function clickcaixatexto(){
    var resultado3 = document.getElementById('resultado3');
    var caixatexto = document.getElementById('caixatexto');
    resultado3.innerHTML = 'olá, boa tarde ' + caixatexto.value;
}

// Gerar números aleatórios
var botao4 = document.getElementById('botao4');
botao4.addEventListener('click', numeroaleatorio4);

function numeroaleatorio4() {
    var resultado4 = document.getElementById('resultado4');
    var numero = Math.random() * 10 + 1;
    numero = parseInt(numero);
    resultado4.innerHTML = numero;
}
// Gerar números (abs)
var botao5 = document.getElementById('botao5');
botao5.addEventListener('click', numeroAleatorio5);

function numeroAleatorio5() {
    var resultado5 = document.getElementById('resultado5');
    // Gerar um número aleatório entre -100 e 100
    var numero = Math.floor(Math.random() * 201) - 100;
    // Calcular o valor absoluto
    var numeroAbs = Math.abs(numero);
    // Exibir o resultado
   resultado5.innerHTML = 'Número: ' + numero + ' <br> Valor Absoluto: ' + numeroAbs;
    
}

// Leia 2 números e exiba o maior deles (Math.max)
var botao6 = document.getElementById('botao6');
botao6.addEventListener('click',numerosmax);

function numerosmax(){
    var resultado6 = document.getElementById('resultado6');
    
    var num1 = parseInt(document.getElementById('num1').value);
    
    var num2 = parseInt(document.getElementById('num2').value);
    
    var maior = Math.max(num1,num2);
    
    resultado6.innerHTML = 'Número Maior é ' + maior ;
    
}
// Leia um número real e exiba-o de forma arredonda (Math.round)
var resultado7 = document.getElementById('resultado7');
botao7.addEventListener('click',numeroarredonda);

function numeroarredonda(){
    var resultado7 = document.getElementById('resultado7');
    var numero = parseFloat(document.getElementById('numerousuario').value);
    
    var arrendonda = Math.round(numero);
    
    resultado7.innerHTML = 'Número arredonda é  ' + arrendonda
    
}

//dois números e exiba um elevado ao outro (Math.pow)
var resultado8 = document.getElementById('resultado8');
botao8.addEventListener('click',potencia);

function potencia(){
    var resultado8 = document.getElementById('resultado8');
    var base = parseInt(document.getElementById('numero1').value);
    var expoente = parseInt(document.getElementById('numero2').value);
    
    var potencia = Math.pow(base,expoente);
    
    resultado8.innerHTML = 'Resultado é  : ' + potencia
    
}

// Exibe o comprimento do número digitado(length)
var botao9 = document.getElementById('botao9'); 
botao9.addEventListener('click', mostradigito);

function mostradigito() {
    var resultado9 = document.getElementById('resultado9');
    var numero = document.getElementById('valorusuario').value;
    
    var comprimento = numero.length;
    resultado9.innerHTML = 'Dígitos: ' + comprimento;
}
// Converte para minúsculo
var botao10 = document.getElementById('botao10');
botao10.addEventListener('click', mostraminusculo);

function mostraminusculo() {
    var resultado10 = document.getElementById('resultado10');
    var caixatexto1 = document.getElementById('caixadetexto1').value;
    var minusculo = caixatexto1.toLowerCase();
    resultado10.innerHTML = 'Ficou assim em minúsculo: ' + minusculo;
}

// Evento para o botão de substituição
document.getElementById('botaoSubstituir').addEventListener('click', substituirTexto);

function substituirTexto() {
    var textoOriginal = document.getElementById('textoOriginal').value;
    
    // Substituir as letras 'a', 'e', 'i', 'o' por '@', '3', '1', '0'
    var textoSubstituido = textoOriginal
        .replace(/a/g, '@')
        .replace(/e/g, '3')
        .replace(/i/g, '1')
        .replace(/o/g, '0');

    document.getElementById('resultadoSubstituicao').innerHTML = 'Texto com substituições: ' + textoSubstituido;
}

// Acessa o botão e adiciona um evento de clique para chamar a função removeEspacos
var botaoTrim = document.getElementById('botaoTrim');
botaoTrim.addEventListener('click', removeEspacos);

function removeEspacos() {
    // Acessa a entrada de texto e o valor digitado
    var entradaTexto = document.getElementById('entradaTexto').value;
    
    // Remove espaços no início e no final da string com trim()
    var textoSemEspacos = entradaTexto.trim();
    
    // Exibe o resultado
    var resultadoTrim = document.getElementById('resultadoTrim');
    resultadoTrim.innerHTML = 'Texto sem espaços: "' + textoSemEspacos + '"';
}

// Nome completo
var botaocompleto = document.getElementById('botaocompleto'); 
botaocompleto.addEventListener('click',nomecompleto);

function nomecompleto(){
    var nome = document.getElementById('nome').value;
    var sobrenome = document.getElementById('sobrenome').value;
    
    var completo = nome + sobrenome
    
    resultadocompleto.innerHTML = 'Nome completo : ' + completo
    
}

// somar e subtração
var botaoadicao = document.getElementById('botaoadicao'); 
botaoadicao.addEventListener('click',somar);
var botaosub = document.getElementById('botaosub'); 
botaosub.addEventListener('click',subtracao);

function somar(){
    var n1 = parseInt(document.getElementById('n1').value);
    var n2 = parseInt(document.getElementById('n2').value);
    var adicao = n1 + n2
    resultadoadicao.innerHTML = 'Resultado Adição :  ' +adicao
    
}

function subtracao(){
    var n1 = parseInt(document.getElementById('n1').value);
    var n2 = parseInt(document.getElementById('n2').value);
    var subtracao = n1 - n2
    resultadosub.innerHTML = 'Resultado subtração :  ' + subtracao
    
}

//Copie o texto de uma caixa de texto para outra.
var botaocopy = document.getElementById('botaocopy'); 
botaocopy.addEventListener('click',copia);

function copia(){
 var caixaoriginal = document.getElementById('caixaoriginal').value;
 var caixacopy = document.getElementById('caixacopy');
    caixacopy.value = caixaoriginal;
    
}

