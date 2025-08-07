function colorChange(){
    let p = document.getElementById("p");
    p.style.color = "blue"

}



function checkNumber() {
  const input = document.getElementById('Input').value;
  const number = parseInt(input, 10);

  if (isNaN(number)) {
    console.log('გთხოვთ, შეიყვანეთ საკმარისი რიცხვი');
    return;
  }

  if (number % 2 === 0) {
    console.log('ლუწი რიცხვია');
  } else {
    console.log('კენტი რიცხვია');
  }
}
