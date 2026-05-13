// --- PASSO 1: Selecionar os elementos do HTML que vamos usar ---
// Usamos o 'document.getElementById' para "pegar" o elemento pelo ID dele
const displayValor = document.getElementById('valor-contador');
const botaoContar = document.getElementById('btn-contar');
const botaoZerar = document.getElementById('btn-zerar');

// --- PASSO 2: Criar a variável que vai guardar o número ---
let contador = 0; // Usamos 'let' porque o valor vai mudar

// --- PASSO 3: Criar a função que aumenta o número ---
function aumentarContador() {
    // Aumentamos o valor da variável em 1
    contador = contador + 1;
    
    // Atualizamos o texto que aparece no HTML
    displayValor.innerText = contador;
    
    // Lógica extra: Se o número for maior que 10, fica verde
    if (contador >= 10) {
        displayValor.style.color = "green";
    }
}

// --- PASSO 4: Criar a função para zerar ---
function zerarContador() {
    contador = 0; // Volta a variável para zero
    displayValor.innerText = contador; // Atualiza a tela
    displayValor.style.color = "black"; // Volta a cor para preto
}

// --- PASSO 5: "Ouvir" os cliques do usuário ---
// Dizemos ao navegador: "Quando o botaoContar for clicado, execute a função aumentarContador"
botaoContar.addEventListener('click', aumentarContador);

// Mesma coisa para o botão de zerar
botaoZerar.addEventListener('click', zerarContador);