async function getPrice(){

    const coin = document.getElementById("coin").value;
    const currency = document.getElementById("currency").value || "usd";

    const response = await fetch("/price",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            coin:coin,
            currency:currency
        })
    });

    const data = await response.json();

    const container = document.getElementById("result");

    if(data.error){
        container.innerText = data.error;
        return;
    }

    container.innerText =
        `${data.coin} price = ${data.price} ${data.currency}`;
}