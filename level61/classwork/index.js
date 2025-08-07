let person = {
    name: "aleqsandre",
    surname: "Dolidze",
    age: 16,
    academy: "GOA",
    hobby: "programming",
    sports: "basketball",
}


let h1 = document.getElementById("h1");
let p = document.getElementById("p");
let btn = document.getElementById("btn");
console.log(h1, p, btn);


p.textContent = person.name;
console.log(p.textContent);
