document.addEventListener("DOMContentLoaded", function() {
    const searchResultInput = document.getElementById("searchResultInput");
    const urlParams = new URLSearchParams(window.location.search);
    const produto = urlParams.get("produto");

    // Exibe o nome do produto pesquisado no campo de pesquisa
    if (produto) {
        searchResultInput.value = decodeURIComponent(produto);
    }

    // Evento para redirecionar com nova pesquisa
    document.getElementById("newSearchButton").addEventListener("click", function() {
        const newQuery = searchResultInput.value.trim();
        if (newQuery) {
            window.location.href = `teladepesquisa.html?produto=${encodeURIComponent(newQuery)}`;
        }
    });
});
