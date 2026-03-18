window.convertCurrency = async function () {

    console.log("clicked");

    const from = document.getElementById("from").value;
    const to = document.getElementById("to").value;
    const amount = document.getElementById("amount").value;

    if (!from || !to || !amount) {
        alert("Please fill all fields");
        return;
    }

    try {
        const response = await fetch("/convert", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                from_currency: from,
                to_currency: to,
                amount: Number(amount)
            })
        });

        const data = await response.json();

        console.log("API DATA:", data);

        const result = document.getElementById("result");

        if (data.error) {
            result.innerText = data.error;
            return;
        }

        result.innerText =
            `${data.amount} ${data.from} = ${data.converted_amount} ${data.to}`;

    } catch (err) {
        document.getElementById("result").innerText = "Request failed";
        console.error(err);
    }
}