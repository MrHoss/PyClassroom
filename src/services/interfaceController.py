class InterfaceController():
    def controllerMainPgs(urlRoute):
        match (urlRoute):
            case "studying":
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
            case "library":
                books = [
                {
                    "book":"Matemática",
                    "autor":90,
                    "description":100,
                    "nameID":"philosophy",
                },
                {
                    "book":"Biologia",
                    "autor":50,
                    "description":100,
                    "nameID":"philosophy",
                },
                {
                    "book":"Química",
                    "autor":40,
                    "description":100,
                    "nameID":"philosophy",
                },
                {
                    "book":"Geografia",
                    "autor":70,
                    "description":100,
                    "nameID":"philosophy",
                },
                {
                    "book":"História",
                    "autor":75,
                    "description":100,
                    "nameID":"philosophy",
                },
                ]
                return books

    def controllerInsidePgs(urlRoutes):
        match (urlRoutes):
            case "studying/math":
                return 'Salve'