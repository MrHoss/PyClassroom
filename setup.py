from src.database.install import migrateAll,seedAll
Run = True
while Run:
    select = input('Você tem certeza que deseja criar as tabelas no banco de dados? Y or n')
    if select == 'Y':
        migrateAll()
        print('tabelas Criadas!')
        Run = False
    elif select == 'n':
        Run = False
while True:
    select = input('Você tem certeza que deseja preencher o banco de dados com os valores padrões? Y or n')
    if select == 'Y':
        seedAll()
        print('Dados criados!')
        exit()
    elif select.lower == 'n':
        exit()