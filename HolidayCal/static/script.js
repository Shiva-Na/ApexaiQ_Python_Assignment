window.getHolidays = async function () {

    console.log("clicked");

    const countryInput = document.getElementById("country").value;
    const yearInput = document.getElementById("year").value;

    const currentYear = new Date().getFullYear();

    const country = countryInput ? countryInput.toUpperCase().trim() : "IN";
    const year = Number(yearInput) || currentYear;

    const response = await fetch("/holidays", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            country: country,
            year: year
        })
    });

    const data = await response.json();

    console.log("API DATA:", data);

    const container = document.getElementById("results");
    container.innerHTML = "";

    if (data.error) {
        container.innerText = data.error;
        return;
    }

    if (!data.holidays || data.holidays.length === 0) {
        container.innerText = "No holidays found";
        return;
    }

    data.holidays.forEach(h => {

        const div = document.createElement("div");

        div.innerHTML =
        `<h3>${h.name}</h3>
         <p>Date: ${h.date}</p>
         <hr>`;

        container.appendChild(div);

    });
}