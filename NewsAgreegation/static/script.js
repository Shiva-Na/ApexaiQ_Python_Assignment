window.getNews = async function () {
    const country = document.getElementById("country").value || "in";
    const category = document.getElementById("category").value;

    const response = await fetch("/news", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
    country: country
})
    });

    const data = await response.json();

    console.log(data); // 👈 ADD THIS

    const container = document.getElementById("news");
    container.innerHTML = "";

    if (data.error) {
        container.innerText = data.error;
        return;
    }

    data.articles.forEach(article => {

        const div = document.createElement("div");

        const image = article.image || "https://via.placeholder.com/200";

        div.innerHTML =
            `<img src="${image}" width="200">
             <h3>${article.title}</h3>
             <p>Source: ${article.source}</p>
             <a href="${article.url}" target="_blank">Read more</a>
             <hr>`;

        container.appendChild(div);
    });
}