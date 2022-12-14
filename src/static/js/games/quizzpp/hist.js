const question = [
    {
        pergunta:`O século XIX foi um momento repleto de invenções em vários campos do saber. Dentre elas, podemos destacar:`,
        resposta:"A fotografia, o cinema e a eletricidade",
        alternativas:[
            "O rádio, o telefone e a televisão",
            "A locomotiva, o automóvel e a vacina",
            "A fotografia, o cinema e a eletricidade",
            "O para-raios, a calculadora e o telégrafo."
        ],
    },
    {
        pergunta:`Entre as características da Segunda Revolução Industrial podemos citar:`,
        resposta:"Concentrou-se na indústria do aço, automobilística e utilização da eletricidade em larga escala",
        alternativas:[
            "Concentrou-se na indústria do aço, automobilística e utilização da eletricidade em larga escala.",
            "Comparada à primeira etapa da Revolução Industrial é uma fase de menor importância, pois nada significativo foi criado.",
            "Possibilitou a expansão dos capitais financeiros somente no continente europeu e nos Estados Unidos.",
            "Revelou o potencial de países como a Alemanha e a França que se aliaram frente ao poderio britânico."
        ],
    },
    {
        pergunta:`A industrialização não foi um fenômeno isolado e atingiu todas as partes do globo. Neste contexto, o papel dos territórios que conseguiram sua independência política durante a Segunda Revolução Industrial foi:`,
        resposta:"tornaram-se fornecedores de matérias-primas agrícolas para aqueles que estavam industrializando-se.",
        alternativas:[
            "tornaram-se fornecedores de matérias-primas agrícolas para aqueles que estavam industrializando-se.",
            "receberam grande parte dos capitais excedentes europeus",
            "absorveram os camponeses que foram expulsos do campo como foi o caso de franceses, alemães e italianos.",
            "conseguiram atrair capitais e mão de obra qualificada que, por sua vez, possibilitaram o processo de industrialização."
        ],
    },
    {
        pergunta:`O trabalho obrigatório que o servo deveria realizar nas terras do senhor feudal foi chamado de:`,
        resposta:"Corveia.",
        alternativas:[
            "Tostão de Pedro.",
            "Corveia.",
            "Talha.",
            "Banalidades.",
            "Mão Morta."
        ],
    },
    {
        pergunta:`Complete as lacunas: Os nobres que doavam terras aos outros nobres eram os ____________, enquanto os _________________ eram os nobres que recebiam essas terras.`,
        resposta:"Suseranos – vassalos.",
        alternativas:[
            "Burgueses – servos.",
            "Vassalos - suseranos.",
            "Suseranos – vilões.",
            "Suseranos – vassalos.",
            "Vassalos – burgueses."
        ],
    },
    {
        pergunta:`(Unemat) A Segunda Grande Guerra (1939-1945) adquiriu caráter mundial a partir de 7 de dezembro de 1941, quando:`,
        resposta:"os japoneses atacaram a base norte-americana de Pearl Harbor",
        alternativas:[
            "os russos tomaram a iniciativa de anexar os Estados Bálticos.",
            "os alemães invadiram o litoral mediterrâneo da África.",
            "os japoneses atacaram a base norte-americana de Pearl Harbor",
            "os franceses, por determinação do marechal Pétain, ocuparam o Sudeste da Ásia;",
            "os chineses cederam a maior parte de seu território às tropas do Eixo."
        ],
    },
    {
        pergunta:`O rompimento pelos nazistas do Pacto Germano-Soviético assinado entre a Alemanha e a União das Repúblicas Socialistas Soviéticas (URSS), no ano de 1939, causou espanto mundial. Em que consistia este acordo?`,
        resposta:"Acordo de não agressão entre Alemanha e União Soviética por dez anos e uma cláusula que incluía a divisão da Polônia entre os dois países.",
        alternativas:[
            "Tratados realizados entre Hitler e Stalin para que ambos não atacassem a Polônia.",
            "Acordo de não agressão entre Alemanha e União Soviética por dez anos e uma cláusula que incluía a divisão da Polônia entre os dois países.",
            "Política de acordos entre Hitler e Stalin de que estabelecia a neutralidade em caso de um conflito armado na Europa.",
            "Uma aliança político-militar entre ambos os países que garantia o apoio caso algum deles fosse atacado pela Inglaterra ou a França."
        ],
    },
    {
        pergunta:`A II Guerra Mundial foi caracterizada pelo desenvolvimento da indústria bélica. Sobre este assunto é correto afirmar que:`,
        resposta:"A maior invenção deste conflito foi a bomba atômica lançada em cidades japonesas em agosto de 1945.",
        alternativas:[
            "A maior invenção deste conflito foi a bomba atômica lançada em cidades japonesas em agosto de 1945.",
            "Os nazistas conseguiram criar armas como o submarino nuclear e o gás Ziklon-B.",
            "As mesmas estratégias utilizadas na Primeira Guerra foram repetidas na Segunda, como o uso da cavalaria.",
            "A aviação de guerra se restringiu à missões de patrulhamento e reconhecimento."
        ],
    },
]
function incrementPoint(){
pontosHist++;
localStorage.setItem("hist",pontosHist);
return pontosHist;
}