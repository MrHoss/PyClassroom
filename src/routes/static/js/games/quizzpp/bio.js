const question = [
    {
        pergunta:"Quais dos órgãos abaixo pertencem ao sistema respiratório?",
        resposta:"Pulmões e faringe",
        alternativas:[
            "Laringe e traqueia","Pulmões e faringe","Esôfago e brônquios","Tireoide e hipófise","Pâncreas e vasos sanguíneos"
        ],
    },
    {
        pergunta:"(Fuvest) A maior parte do nitrogênio que compõe as moléculas orgânicas ingressa nos ecossistemas pela ação de:",
        resposta:"bactérias",
        alternativas:[
            "algas marinhas","animais","bactérias","fungos","plantas terrestres"
        ],
    },
    {
        pergunta:"(PUC) As cianobactérias podem ser consideradas seres vivos auto-suficientes porque são capazes de:",
        resposta:"fixar tanto N2 quanto CO2 sob a forma de matéria orgânica",
        alternativas:[
            "fixar tanto N2 quanto CO2 sob a forma de matéria orgânica",
            "absorver cálcio e nitrogênio diretamente das rochas",
            "fixar o H2 atmosférico sob a forma de matéria orgânica",
            "degradar qualquer tipo de matéria inorgânica ou orgânica",
            "disponibilizar o fósforo para outros seres vivos"
        ],
    },
    {
        pergunta:" (UnB) Qual a afirmativa correta:",
        resposta:"O local do ecossistema onde vive uma determinada espécie é denominado de habitat",
        alternativas:[
            "O local do ecossistema onde vive uma determinada espécie é denominado de hábitat",
            "Populações são conjuntos de indivíduos geneticamente iguais",
            "Clone é um grupo de indivíduos da mesma espécie que vivem no mesmo hábitat",
            "Ecossistema é a palavra empregada para indicar o conjunto de populações de um ambiente",
            "Comunidade é a palavra que indica o conjunto de indivíduos de uma mesma espécie que habitam uma região"
        ],
    },
    {
        pergunta:"(USP) Num ecossistema, um fungo, uma coruja e um coelho podem desempenhar os papéis, respectivamente, de:",
        resposta:"decompositor, consumidor de 2ª ordem e consumidor de 1ª ordem.",
        alternativas:[
            "decompositor, consumidor de 2ª ordem e consumidor de 1ª ordem",
            "produtor, consumidor de 1ª ordem e consumidor de 2ª ordem",
            "consumidor de 1ª ordem, consumidor de 2ª ordem e consumidor de 1ª ordem",
            "consumidor de 2ª ordem, consumidor de 3ª ordem e consumidor de 1ª ordem",
            "decompositor, consumidor de 1ª ordem e decompositor"
        ],
    },
    {
        pergunta:"Alguns exemplos de fungos são:",
        resposta:"cogumelos e mofos.",
        alternativas:[
            "bactérias e protozoários.",
            "cogumelos e mofos.",
            "algas e cianofíceas.",
            "musgos e samambaias.",
            "vacas e aves."
        ],
    },{
        pergunta:`(Enem/2018)

        O deserto é um bioma que se localiza em regiões de pouca umidade. A fauna é, predominantemente, composta por animais roedores, aves, répteis e artrópodes.
        
        Uma adaptação, associada a esse bioma, presente nos seres vivos dos grupos citados é o(a):`,
        resposta:"eliminação de excretas nitrogenadas de forma concentrada.",
        alternativas:[
            "existência de numerosas glândulas sudoríparas na epiderme.",
            "eliminação de excretas nitrogenadas de forma concentrada.",
            "desenvolvimento do embrião no interior de ovo com casca.",
            "capacidade de controlar a temperatura corporal.",
            "respiração realizada por pulmões foliáceos."
        ],
    },
    
]
function incrementPoint(){
pontosBio++;
localStorage.setItem("bio",pontosBio);
return pontosBio;
}