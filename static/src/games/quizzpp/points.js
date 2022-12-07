const resetBtn = document.querySelector(".reset-btn");
const thisPointMath = document.querySelector("#thisPointsMath");
const thisPointGeo = document.querySelector("#thisPointsGeo");
const pointText = document.querySelector("#pointsText");

var signal = "";
var resultado = 0;
var pontosMath = 0;
var pontosGeo = 0;
var pontosAcumulados =0;

function update(){
    
    pontosMath = localStorage.getItem('math') ? localStorage.getItem('math') : 0 ;
    pontosGeo = localStorage.getItem('geo') ? localStorage.getItem('geo') : 0 ;
    pontosAcumulados = +pontosMath + +pontosGeo
    if(thisPointMath){thisPointMath.textContent = pontosMath;}
    if(thisPointGeo){thisPointGeo.textContent = pontosGeo;}
    pointText.textContent = pontosAcumulados;
}
update();

resetBtn.addEventListener("click", function () {
    localStorage.clear();
    update()
})