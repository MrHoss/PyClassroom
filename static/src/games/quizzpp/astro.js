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
pontosAstro++;
localStorage.setItem("astro",pontosAstro);
return pontosAstro;
}