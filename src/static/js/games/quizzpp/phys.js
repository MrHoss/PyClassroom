const question = [
    {
        pergunta:"Quantos continentes existem?",
        resposta:"6",
        alternativas:[
            "2","4","6","8","10"
        ],
    },
]
function incrementPoint(){
pontosPhys++;
localStorage.setItem("phys",pontosPhys);
return pontosPhys;
}