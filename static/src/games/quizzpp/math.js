
const labelCalc = document.querySelector("#calc");
const answerBtn = document.querySelector(".res-btn");
const answerInpt = document.querySelector(".input-quizz");

const notifier = document.querySelector(".notifier");


window.onload = conta();
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
    update();
    answerBtn.disabled = true;
    answerBtn.style.background="#ad2828";
    setTimeout(() => {
        notifier.style.top="-10vh";
        answerInpt.value=0;
        answerBtn.style.background="#008000"
        answerBtn.disabled = false;
        conta();
    }, 2000);
    
});

