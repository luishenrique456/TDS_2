function getById(id) {
    return document.getElementById(id)
};

function clique (id, funcao){
    getById(id).addEventListener("click", funcao)
};



// Função para adicionar zeros à esquerda
function adicionarZeros() {
    const caixaTexto = getById("caixatext1").value; // Lê o valor da caixa de texto
    const numeroComZeros = caixaTexto.padStart(5 + caixaTexto.length, '0'); // Adiciona 5 zeros à esquerda
    getById("resultado").textContent = `Resultado: ${numeroComZeros}`; // Exibe o resultado
}

// Associa a função ao botão
clique("botao", adicionarZeros);

// 2) Leia 2 números e exiba as 4 operações matemáticas básicas.

clique ('enviarNumeros', () =>{
    let numero1 = parseFloat(document.getElementById('digitarNumero-1').value);
    let numero2 = parseFloat(document.getElementById('digitarNumero-2').value);
    let soma = numero1 + numero2;
    let subtracao = numero1 - numero2;
    let multiplicacao = numero1 * numero2;
    let divisao = numero1 / numero2;

    getById('mostrarOperacoes').innerHTML =`
        Soma: ${soma}<br>
        Subtração: ${subtracao}<br>
        Multiplicação: ${multiplicacao}<br>
        Divisão: ${divisao}
    `
});


//3) Leia uma temperatura em Celsius e converta para Fahrenheit.
clique ('converterTemperatura', () =>{
    let temperaturaC = parseFloat(document.getElementById('digitarTemperaturaC').value)
    let temperaturaF = (temperaturaC * 9/5) + 32 
    getById('mostrarTemperaturaF').innerHTML=`
        Temperatura em Fahrenheit: ${temperaturaF}
    `
})

clique('botaodate', () => {
    // Obtém a data atual
    const dataAtual = new Date();
    
    // Formata a data no formato "dd/mm/aaaa"
    const dia = String(dataAtual.getDate()).padStart(2, '0');
    const mes = String(dataAtual.getMonth() + 1).padStart(2, '0'); // Os meses começam do 0
    const ano = dataAtual.getFullYear();

    // Exibe apenas a data formatada
    getById('resultadodate').innerHTML = `
        Data Atual: ${dia}/${mes}/${ano}
    `;
});

// Função para copiar o texto de uma caixa para outra em tempo real usando o evento keyup
getById('caixa1').addEventListener('keyup', function() {
    getById('caixa2').value = this.value;
});


