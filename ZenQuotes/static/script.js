window.getQuote = async function () {

    console.log("clicked");  // debug

    const response = await fetch("/quote");
    const data = await response.json();

    const box = document.getElementById("quoteBox");

    if(data.error){
        box.innerText = data.error;
        return;
    }

    box.innerHTML =
        `"${data.quote}"<br><br>— ${data.author}`;
}