const question = [
    {
        pergunta:"De onde é a invenção do chuveiro elétrico?",
        resposta:"Brasil",
        alternativas:[
            "França","Inglaterra","Brasil","Austrália","Itália"
        ],
    },
    {
        pergunta:"De onde é a invenção do chuveiro elétrico?",
        resposta:"Brasil",
        alternativas:[
            "França","Inglaterra","Brasil","Austrália","Itália"
        ],
    },
]
function incrementPoint(){
pontosTech++;
localStorage.setItem("tech",pontosTech);
return pontosTech;
}