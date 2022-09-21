from db.Aulas import AulaDB
from helper.WriteAJson import writeAJson

aula = AulaDB()

#MENU

newClass = input("Deseja cadastrar uma nova aula? (S - sim | N - não) ")

if (newClass == 'S'):

    #Insira o nome do professor e sua especialidade
    nomeProfessor = input("Nome do professor: ")
    especialidade = input("Qual sua especialidade? ")

    professor = aula.newTeacher(nomeProfessor, especialidade);


    #Insira quantos aluno deseja cadastrar
    qtdStudents = int(input("Quantos alunos deseja cadastrar? "))

    students = aula.newStudents(qtdStudents)

    #Insira o assunto da aula
    className = input("Assunto da aula: ")

    #Insira a aula no banco de dados
    newClass = aula.newClass(className, professor, students)

else:
    pass


#Leia as todas as aulas cadastradas
viewClass = input("Deseja visualizar as aulas cadastradas? (S - sim | N - não) ")

if(viewClass == 'S'):
    allClasses = aula.getClasses()
    print(allClasses)
else:
    pass

#Atualizar uma aula
updateClass = input("Deseja atualizar o assunto de alguma aula? (S - sim | N - não) ")

if(updateClass == 'S'):
    id = input("ID da aula: ")
    subject = input("Assunto da aula: ")
    res = aula.updateClass(id, subject)
else:
    pass

#Remover uma aula

removeClass = input("Deseja deletar alguma aula? (S - sim | N - não) ")
if(removeClass == 'S'):
    id = input("ID da aula: ")
    res = aula.deleteClass(id)
else:
    pass

