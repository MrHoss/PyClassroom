const question = [
    {
        pergunta:"Qual o metal cujo símbolo químico é o Au?",
        resposta:"Ouro",
        alternativas:[
            "Cobre","Prata","Mercúrio","Ouro","Manganês"
        ],
    },
    {
        pergunta:`Na Química orgânica, os compostos são reconhecidos pelas cadeias formadas por carbono e hidrogênio. Entretanto, outros elementos podem fazer parte da estrutura química desses compostos, como o oxigênio.

        Selecione a alternativa em que os dois compostos orgânicos apresentam funções orgânicas oxigenadas.`,
        resposta:"propanol e ácido propanoico",
        alternativas:[
            "clorofórmio e metanoato de etila",
            "propanol e ácido propanoico",
            "eteno e etanodiol",
            "etanamida e benzeno"
        ],
    },
]
function incrementPoint(){
pontosQuim++;
localStorage.setItem("quim",pontosQuim);
return pontosQuim;
}