
const labelCalc = document.querySelector("#calc");
const answerBtn = document.querySelector(".res-btn");
const answerInpt = document.querySelector(".input-quizz");
const thisPointText = document.querySelector("#thisPointsText");
const pointText = document.querySelector("#pointsText");
const notifier = document.querySelector(".notifier");
const resetBtn = document.querySelector(".reset-btn");


var signal = "";
var resultado = 0;
var pontosMath = 0;
var pontosAcumulados = 0


window.onload = conta();
function update(){
    pontosMath = localStorage.getItem('math') ? localStorage.getItem('math'):0;
    pontosAcumulados = pontosMath
    thisPointText.textContent = pontosMath;
    pointText.textContent = pontosAcumulados;
}
update();

function random(){
    return  Math.floor(Math.random() * (999 - 0) ) + 1;
}

function createCount(num1, num2){
    let sub = num1 - num2;
    let sum = num1 + num2;
    let mul = num1 * num2;
    let div = num1 / num2;
    let rand = Math.floor(Math.random() * 4) + 1;
    switch (rand) {
        case 1:
            signal = "-";
            return(sub);
        case 2:
            signal = "+";
            return(sum);
        case 3:
            signal = "x";
            return(mul);
        case 4:
            signal = "÷";
            return(div);
        default:
            console.log("erro")
      }
}

function conta(){
    setTimeout(() => {
        notifier.style.top="-10vh";
    }, 2000);
    var num1 = random()
    var num2 = random()
    resultado = createCount(num1,num2);
    labelCalc.textContent=(`${num1} ${signal} ${num2}`);
}
answerBtn.addEventListener("click", function () {
    if (answerInpt.value == resultado){
        pontosMath++;
        localStorage.setItem('math',pontosMath);
        notifier.style.top="40vh";
        notifier.textContent="Você acertou!"
        notifier.style.backgroundColor="#008000";
    }else{
        notifier.style.top="40vh";
        notifier.textContent=`Você errou!\n O resultado é ${resultado}`
        notifier.style.backgroundColor="#ad2828";
    }
    answerInpt.value=0;
    update();
    conta();
    
});

resetBtn.addEventListener("click", function () {
    localStorage.clear();
    update()
})