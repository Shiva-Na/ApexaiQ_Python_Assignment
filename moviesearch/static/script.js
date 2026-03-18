async function searchMovie() {

    const query = document.getElementById("query").value;
    const year = document.getElementById("year").value;
    const page = document.getElementById("page").value || 1;

    const response = await fetch("/search", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            query: query,
            page: Number(page),
            year: year ? Number(year) : null
        })
    });

    const data = await response.json();

    const container = document.getElementById("results");
    container.innerHTML = "";

    if (data.error) {
        container.innerText = data.error;
        return;
    }

    data.movies.forEach(movie => {
        const div = document.createElement("div");

        div.innerHTML =
            `<b>${movie.title}</b> (${movie.year}) <br>
             <img src="${movie.poster}" width="100"><hr>`;

        container.appendChild(div);
    });
}