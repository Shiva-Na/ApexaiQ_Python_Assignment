async function getWeather() {

    const city = document.getElementById("city").value;

    const response = await fetch("/weather", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ city: city })
    });

    const data = await response.json();

    document.getElementById("weatherResult").innerText =
        `Temp: ${data.temperature}°C | ${data.description}`;
}


async function getRepo() {

    const owner = document.getElementById("owner").value;
    const repo = document.getElementById("repo").value;

    const response = await fetch("/github", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ owner: owner, repo: repo })
    });

    const data = await response.json();

    document.getElementById("repoResult").innerText =
        `Stars: ${data.stars} | Forks: ${data.forks} | Issues: ${data.open_issues}`;
}