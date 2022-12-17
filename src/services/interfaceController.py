class InterfaceController():
    def controllerMainPgs(urlRoute):
        if(urlRoute == "studying"):
            disciplines = [
            {
                "discipline":"Matemática",
                "progress":90,
                "note":100,
                "nameID":"math",
            },
                            {
                "discipline":"Português",
                "progress":75,
                "note":100,
                "nameID":"portuguese",
            },
            {
                "discipline":"Geografia",
                "progress":70,
                "note":100,
                "nameID":"geography",
            },
            {
                "discipline":"História",
                "progress":75,
                "note":100,
                "nameID":"history",
            },
            {
                "discipline":"Química",
                "progress":40,
                "note":100,
                "nameID":"chemistry",
            },
            {
                "discipline":"Biologia",
                "progress":50,
                "note":100,
                "nameID":"biology",
            },
            {
                "discipline":"Física",
                "progress":75,
                "note":100,
                "nameID":"physic",
            },
            {
                "discipline":"Inglês",
                "progress":75,
                "note":100,
                "nameID":"english",
            },
            {
                "discipline":"Filosofia",
                "progress":75,
                "note":100,
                "nameID":"philosophy",
            },
            ]
            return disciplines
        elif(urlRoute == "library"):
            books = [
                    {
                        "title": "O Pequeno Príncipe",
                        "author": "Antoine de Saint-Exupéry",
                        "publisher": "Gallimard",
                        "cover_image": "https://images-americanas.b2w.io/produtos/2019108396/imagens/livro-o-pequeno-principe/2019108396_1_large.jpg",
                    },
                    {
                        "title": "O Mundo de Sofia",
                        "author": "Jostein Gaarder",
                        "publisher": "Aschehoug",
                        "cover_image": "https://images-americanas.b2w.io/produtos/2019108396/imagens/livro-o-pequeno-principe/2019108396_1_large.jpg",
                    },
                    {
                        "title": "Harry Potter e a Pedra Filosofal",
                        "author": "J.K. Rowling",
                        "publisher": "Bloomsbury",
                        "cover_image": "https://images-americanas.b2w.io/produtos/2019108396/imagens/livro-o-pequeno-principe/2019108396_1_large.jpg",
                    },
                    {
                        "title": "1984",
                        "author": "George Orwell",
                        "publisher": "Secker & Warburg",
                        "cover_image": "https://images-americanas.b2w.io/produtos/2019108396/imagens/livro-o-pequeno-principe/2019108396_1_large.jpg",
                    },
                    {
                        "title": "Matar um Mockingbird",
                        "author": "Harper Lee",
                        "publisher": "J.B. Lippincott & Co.",
                        "cover_image": "https://images-americanas.b2w.io/produtos/2019108396/imagens/livro-o-pequeno-principe/2019108396_1_large.jpg",
                    },
                    {
                        "title": "O Senhor dos Anéis",
                        "author": "J.R.R. Tolkien",
                        "publisher": "George Allen & Unwin",
                        "cover_image": "https://images-americanas.b2w.io/produtos/2019108396/imagens/livro-o-pequeno-principe/2019108396_1_large.jpg",
                    }]
            return books
        else:
            return "salve"

    def controllerInsidePgs(urlRoutes):
        if(urlRoutes == "studying/math"):
            math = [
                {
                    'title': '<b>Aula 1</b>: Números inteiros',
                    'description': 'Nesta aula, vamos aprender sobre os números inteiros e suas operações básicas.',
                    'access_link': 'aula1'
                },
                {
                    'title': '<b>Aula 2</b>: Frações',
                    'description': 'Nesta aula, vamos aprender sobre frações e suas operações.',
                    'access_link': 'aula2'
                },
                {
                    'title': '<b>Aula 3</b>: Equações do 1º grau',
                    'description': 'Nesta aula, vamos aprender a resolver equações do 1º grau.',
                    'access_link': 'aula3'
                },
                {
                    'title': '<b>Aula 4</b>: Geometria plana',
                    'description': 'Nesta aula, vamos aprender sobre os conceitos básicos de geometria plana, como ângulos, polígonos e círculos.',
                    'access_link': 'aula4'
                },
                {
                    'title': '<b>Aula 5</b>: Análise combinatória',
                    'description': 'Nesta aula, vamos aprender sobre os principais conceitos de análise combinatória, como arranjos, combinações e permutações.',
                    'access_link': 'aula5'
                },
                {
                    'title': '<b>Aula 6</b>: Estatística básica',
                    'description': 'Nesta aula, vamos aprender sobre os conceitos básicos de estatística, como média, mediana, moda e desvio padrão.',
                    'access_link': 'aula6'
                },
                {
                    'title': '<b>Aula 7</b>: Equações do 2º grau',
                    'description': 'Nesta aula, vamos aprender a resolver equações do 2º grau.',
                    'access_link': 'aula7'
                },
                {
                    'title': '<b>Aula 8</b>: Funções',
                    'description': 'Nesta aula, vamos aprender sobre os conceitos básicos de funções, como gráficos, funções lineares e não lineares.',
                    'access_link': 'aula8'
                }
                ]
            return math
        else:
            return "salve"