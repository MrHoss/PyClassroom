class InterfaceController():
    def controllerMainPgs(urlRoute):
        if(urlRoute == "studying"):
            disciplines = [
            {
                "discipline":"Matemática",
                "progress":90,
                "note":100,
                "titleID":"math",
            },
                            {
                "discipline":"Português",
                "progress":75,
                "note":100,
                "titleID":"portuguese",
            },
            {
                "discipline":"Geografia",
                "progress":70,
                "note":100,
                "titleID":"geography",
            },
            {
                "discipline":"História",
                "progress":75,
                "note":100,
                "titleID":"history",
            },
            {
                "discipline":"Química",
                "progress":40,
                "note":100,
                "titleID":"chemistry",
            },
            {
                "discipline":"Biologia",
                "progress":50,
                "note":100,
                "titleID":"biology",
            },
            {
                "discipline":"Física",
                "progress":75,
                "note":100,
                "titleID":"physic",
            },
            {
                "discipline":"Inglês",
                "progress":75,
                "note":100,
                "titleID":"english",
            },
            {
                "discipline":"Filosofia",
                "progress":75,
                "note":100,
                "titleID":"philosophy",
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
                        "cover_image": "https://m.media-amazon.com/images/I/91U9VjiT-xL.jpg",
                    },
                    {
                        "title": "Harry Potter e a Pedra Filosofal",
                        "author": "J.K. Rowling",
                        "publisher": "Bloomsbury",
                        "cover_image": "https://m.media-amazon.com/images/I/81ibfYk4qmL.jpg",
                    },
                    {
                        "title": "1984",
                        "author": "George Orwell",
                        "publisher": "Secker & Warburg",
                        "cover_image": "https://m.media-amazon.com/images/I/61t0bwt1s3L.jpg",
                    },
                    {
                        "title": "Matar um Mockingbird",
                        "author": "Harper Lee",
                        "publisher": "J.B. Lippincott & Co.",
                        "cover_image": "https://m.media-amazon.com/images/I/81aY1lxk+9L.jpg",
                    },
                    {
                        "title": "O Senhor dos Anéis",
                        "author": "J.R.R. Tolkien",
                        "publisher": "George Allen & Unwin",
                        "cover_image": "https://img2.doceru.com/image/l/csx5nx.png",
                    }]
            return books
        elif(urlRoute == "events"):
            events = [    {'name': 'Assembléia de Pais', 'date': '2022-01-20', 'location': 'Salão Nobre'},    {'name': 'Feira de Ciências', 'date': '2022-03-15', 'location': 'Ginásio'},    {'name': 'Gincana Escolar', 'date': '2022-05-10', 'location': 'Campo de Futebol'},    {'name': 'Festa Junina', 'date': '2022-06-24', 'location': 'Quadra Poliesportiva'},    {'name': 'Formatura', 'date': '2022-07-20', 'location': 'Teatro Municipal'}]
            return events

        elif(urlRoute == "courses"):
            courses = [
                    {
                        "title": "Curso de Desenvolvimento Web",
                        "description": "Aprenda a desenvolver aplicações web usando HTML, CSS e JavaScript.",
                        "duration": "6 meses",
                        "price": "R$ 1.000,00"
                    },
                    {
                        "title": "Curso de Design Gráfico",
                        "description": "Aprenda a criar designs atraentes e eficazes usando programas de design gráfico.",
                        "duration": "4 meses",
                        "price": "R$ 800,00"
                    },
                    {
                        "title": "Curso de Programação para Iniciantes",
                        "description": "Aprenda os fundamentos da programação e comece a desenvolver seus próprios aplicativos.",
                        "duration": "8 meses",
                        "price": "R$ 1.500,00"
                    },
                    {
                        "title": "Curso de Marketing Digital",
                        "description": "Aprenda as técnicas e estratégias mais eficazes para promover produtos e serviços online.",
                        "duration": "5 meses",
                        "price": "R$ 1.200,00"
                    },
                    {
                        "title": "Curso de Redes de Computadores",
                        "description": "Aprenda a projetar, configurar e gerenciar redes de computadores.",
                        "duration": "7 meses",
                        "price": "R$ 1.800,00"
                    },
                    {
                        "title": "Curso de Desenvolvimento de Jogos",
                        "description": "Aprenda a criar jogos para diferentes plataformas usando diferentes tecnologias.",
                        "duration": "9 meses",
                        "price": "R$ 2.500,00"
                    },
                    {
                        "title": "Curso de Fotografia",
                        "description": "Aprenda a tirar fotos incríveis e a editá-las usando técnicas avançadas.",
                        "duration": "4 meses",
                        "price": "R$ 1.000,00",
                    },]
            return courses
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