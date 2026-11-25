// script.js - manda al server la parola scritta e mostra la risposta nella pagina
const modulo = document.getElementById("modulo");
const risultato = document.getElementById("risultato");
modulo.addEventListener("submit", async function (evento) {
  evento.preventDefault(); // la pagina non si ricarica
  // 1. prepariamo il colpo, con il nome del campo della classe Colpo
  const colpo = {
    parola: document.getElementById("parola").value,
  };
  // 2. lo mandiamo al server con una richiesta POST
  const risposta = await fetch("/gioca", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(colpo),
  });
  // 3. leggiamo la risposta (in JSON) e la scriviamo nella pagina
  const dati = await risposta.json();
  risultato.textContent = "Il server risponde: " + dati.risposta;
});