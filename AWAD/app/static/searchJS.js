const q = document.getElementById("search");
q.addEventListener("keyup", () => {
    let query = q.value.trim();

    if (query.length > 0) {
        fetch(`/search/${query}`)
            .then((response) => response.text())
            .then((results) => {
                document.getElementById("resTable").innerHTML = results;
            });
    } else {
        // If the search bar is cleared, reset to show all films
        fetch(`/search/`)
            .then((response) => response.text())
            .then((results) => {
                document.getElementById("films").innerHTML = results;
            });
    }
});
