const resetBtn = document.querySelector(".reset-btn");
const thisPointMath = document.querySelector("#thisPointsMath");
const thisPointGeo = document.querySelector("#thisPointsGeo");
const thisPointHist = document.querySelector("#thisPointsHist");
const thisPointQuim = document.querySelector("#thisPointsQuim");
const thisPointBio = document.querySelector("#thisPointsBio");
const thisPointPhys = document.querySelector("#thisPointsPhys");
const thisPointAstro = document.querySelector("#thisPointsAstro");
const thisPointTech = document.querySelector("#thisPointsTech");
const pointText = document.querySelector("#pointsText");

var signal = "";
var resultado = 0;

var pontosMath = 0;
var pontosGeo = 0;
var pontosHist = 0;
var pontosQuim = 0;
var pontosBio = 0;
var pontosPhys = 0;
var pontosAstro = 0;
var pontosTech = 0;

var pontosAcumulados =0;

function update(){
    
    pontosMath = localStorage.getItem('math') ? localStorage.getItem('math') : 0 ;
    pontosGeo = localStorage.getItem('geo') ? localStorage.getItem('geo') : 0 ;
    pontosHist = localStorage.getItem('hist') ? localStorage.getItem('hist') : 0 ;
    pontosQuim = localStorage.getItem('quim') ? localStorage.getItem('quim') : 0 ;
    pontosBio = localStorage.getItem('bio') ? localStorage.getItem('bio') : 0 ;
    pontosPhys = localStorage.getItem('phys') ? localStorage.getItem('phys') : 0 ;
    pontosAstro = localStorage.getItem('astro') ? localStorage.getItem('astro') : 0 ;
    pontosTech = localStorage.getItem('tech') ? localStorage.getItem('tech') : 0 ;

    pontosAcumulados =  +pontosMath + 
                        +pontosGeo + 
                        +pontosHist + 
                        +pontosQuim + 
                        +pontosBio + 
                        +pontosPhys + 
                        +pontosAstro + 
                        +pontosTech
    if(thisPointMath){thisPointMath.textContent = pontosMath;}
    if(thisPointGeo){thisPointGeo.textContent = pontosGeo;}
    if(thisPointHist){thisPointHist.textContent = pontosHist;}
    if(thisPointQuim){thisPointQuim.textContent = pontosQuim;}
    if(thisPointBio){thisPointBio.textContent = pontosBio;}
    if(thisPointPhys){thisPointPhys.textContent = pontosPhys;}
    if(thisPointAstro){thisPointAstro.textContent = pontosAstro;}
    if(thisPointTech){thisPointTech.textContent = pontosTech;}
    pointText.textContent = pontosAcumulados;
}
update();

resetBtn.addEventListener("click", function () {
    localStorage.clear();
    update()
})