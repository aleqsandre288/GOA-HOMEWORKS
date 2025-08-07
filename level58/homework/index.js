age = 15;
name = "John Doe";
a = 5;
b = 10;
sunny_weather = true;
console.log(a+b);
console.log("Hello, " + name + "! You are " + age + " years old.");

// საბოლოოდ, დაამატეთ confirm() და მომხმარებელს კითხეთ სურს თუ არა საიტის დატოვება, თუ პასუხი დადებითი იქნება კონსოლში გამოუტანეთ 'you will live the site soon', თუ პასუხი  უარყოფითი იქნება კონსოლში გამოუტანეთ 'you are staying on the site'.
confirm("Do you want to leave the site?");
if (confirm("Do you want to leave the site?")) {
    console.log("You will leave the site soon.");
}

