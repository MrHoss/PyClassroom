const askLbl = document.getElementById("askLabel");
const answerList = document.querySelector('.answerList');
const answerBtn = document.querySelector(".res-btn");
const notifier = document.querySelector(".notifier");
var answerListItems = []
var optionSelect = [];
var answered = '';
var correctAnswer = '';

function randomQuestion(){
    return  Math.floor(Math.random() * (question.length - 0) );
}

const getShuffledArr = arr => {
    const newArr = arr.slice()
    for (let i = newArr.length - 1; i > 0; i--) {
        const rand = Math.floor(Math.random() * (i + 1));
        [newArr[i], newArr[rand]] = [newArr[rand], newArr[i]];
    }
    return newArr
};

createQuestion();
function createQuestion(){
    let questionSelected = randomQuestion()
    correctAnswer = question[questionSelected].resposta;
    let alternatives = question[questionSelected].alternativas;
    let alternativesShffled = alternatives.sort(() => Math.random() - 0.5);
    askLbl.textContent = question[questionSelected].pergunta;
    for(const option of alternativesShffled){
        let optionDiv = document.createElement('div');
        optionDiv.classList.add('alternatives');
        optionDiv.innerHTML = `<label for="answer"><input class="select" name="answer" type="radio" value=${option.replace(/\s/g, '_')}>${option}</label>`
        answerList.append(optionDiv);
        optionSelect = document.querySelectorAll(".answerList .select");
        answerListItems = document.querySelectorAll(".answerList .alternatives");
    }
    for(const option of optionSelect){
        option.addEventListener("click", function () {
        answered = option.value;
        console.log(option.value)
        })
    }
}



answerBtn.addEventListener("click", function () {
    if ((correctAnswer !== '') && (correctAnswer.replace(/\s/g, '_') == answered)){
        
        incrementPoint()
        notifier.style.top="40vh";
        notifier.textContent="Você acertou!"
        notifier.style.backgroundColor="#008000";
        
    }else{
        notifier.style.top="40vh";
        notifier.textContent=`Você errou!\n A resposta é ${correctAnswer}`
        notifier.style.backgroundColor="#ad2828";
    }
    update();
    answerBtn.disabled = true;
    answerBtn.style.background="#ad2828";
    setTimeout(() => {
        for(const item of answerListItems){
            answerList.removeChild(item);
        }
        answered = ''
        notifier.style.top="-10vh";
        answerBtn.style.background="#008000"
        answerBtn.disabled = false;
        createQuestion()
    }, 2000);
    
})