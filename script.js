async function getQuote() {
    const response = await fetch("http://127.0.0.1:5000/quote");
    const data = await response.json();

    document.getElementById("quote").innerText = data.content;
    document.getElementById("author").innerText = "- " + data.author;
}