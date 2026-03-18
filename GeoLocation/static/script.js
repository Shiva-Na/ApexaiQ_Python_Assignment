async function lookupIP(){

    const ip = document.getElementById("ip").value;

    const response = await fetch("/lookup",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            ip:ip
        })
    });

    const data = await response.json();

    const container = document.getElementById("result");

    if(data.error){
        container.innerText = data.error;
        return;
    }

    container.innerHTML =
        `IP: ${data.ip}<br>
         Country: ${data.country}<br>
         Region: ${data.region}<br>
         City: ${data.city}<br>
         ISP: ${data.isp}`;
}