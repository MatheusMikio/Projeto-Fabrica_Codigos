document.addEventListener("DOMContentLoaded", function() {
    // Seleciona o campo de input e o botão de busca
    const searchInput = document.getElementById("searchInput");
    const searchButton = document.getElementById("searchButton");

    // Função para redirecionar para telaDePesquisa.html
    function redirectToSearchPage() {
        window.location.href = "teladepesquisa.html";
    }

    // Evento para o clique no botão "Buscar"
    searchButton.addEventListener("click", redirectToSearchPage);

    // Evento para pressionar a tecla "Enter" no campo de pesquisa
    searchInput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            redirectToSearchPage();
        }
    });
});

