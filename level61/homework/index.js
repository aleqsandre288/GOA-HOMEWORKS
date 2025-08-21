function colorChange(){
    let p = document.getElementById("p");
    p.style.color = "blue"

}


function checkAdmin() {
            const input = document.getElementById('input').value;
            if (input === 'admin') {
                document.body.style.backgroundColor = 'green';
            } else {
                document.body.style.backgroundColor = 'red';
            }
        }
