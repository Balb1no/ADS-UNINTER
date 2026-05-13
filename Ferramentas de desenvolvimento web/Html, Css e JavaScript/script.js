// --- SELEÇÃO DE ELEMENTOS ---
// Criamos constantes para "conversar" com as partes específicas do nosso HTML
const display = document.getElementById('valor'); // Onde o número aparece
const btnMais = document.getElementById('btn-aumentar'); // Botão de somar
const btnReset = document.getElementById('btn-zerar'); // Botão de resetar

// --- VARIÁVEL DE ESTADO ---
// Criamos uma variável let (que pode mudar) para guardar o valor atual do contador
let numeroAtual = 0;

// --- FUNÇÃO PARA AUMENTAR ---
// Esta função será chamada toda vez que o botão 'Aumentar' for clicado
function somarUm() {
    // Adicionamos 1 ao valor da nossa variável
    numeroAtual = numeroAtual + 1;
    
    // Pegamos o elemento 'display' e trocamos o texto dele pelo nosso novo número
    display.innerText = numeroAtual;
    
    // Lógica extra: Se o número for positivo, a cor fica azul
    if (numeroAtual > 0) {
        display.style.color = "#3498db";
    }
}

// --- FUNÇÃO PARA ZERAR ---
// Esta função limpa o contador e volta ao estado original
function resetar() {
    // Voltamos a variável para o valor zero
    numeroAtual = 0;
    
    // Atualizamos a tela com o valor zero
    display.innerText = numeroAtual;
    
    // Voltamos a cor do texto para preto
    display.style.color = "black";
}

// --- EVENTOS (OUVINTES) ---
// Aqui dizemos ao navegador para ficar "vigiando" os cliques nos botões
// Quando clicar em btnMais, execute a função somarUm
btnMais.addEventListener('click', somarUm);

// Quando clicar em btnReset, execute a função resetar
btnReset.addEventListener('click', resetar);