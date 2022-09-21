from db.Aulas import AulaDB
from helper.WriteAJson import writeAJson

aula = AulaDB()

#MENU

newClass = input("Deseja cadastrar uma nova aula? (S - sim | N - não) ")

def newStudents(qtdStudents: int):
    # Cadastre os alunos
    students = []
    while (len(students) < qtdStudents):
        nomeAluno = input("Nome do aluno: ")
        mat = input("Matrícula: ")
        curso = input("Curso: ")
        periodo = input("Período: ")

        students.append({"nome": nomeAluno, "matricula": mat, "curso": curso, "periodo": periodo})
        print(students)

    else:
        pass

    return students


if (newClass == 'S'):

    #Insira o nome do professor e sua especialidade
    nomeProfessor = input("Nome do professor: ")
    especialidade = input("Qual sua especialidade? ")

    professor = aula.newTeacher(nomeProfessor, especialidade);

    newStudent = input("Deseja cadastrar estudantes? (S - sim | N - não) ")
    if (newStudent == 'S'):
        #Insira quantos aluno deseja cadastrar
        qtdStudents = int(input("Quantos alunos deseja cadastrar? "))

        students = newStudents(qtdStudents);

        #Insira o assunto da aula
        className = input("Assunto da aula: ")

        #Insira a aula no banco de dados
        newClass = aula.newClass(className, professor, students)
    else:
        pass
else:
    pass

# addStudent = input("Deseja inserir estudantes em uma aula já existente? (S - sim | N - não) ")
#
# if(addStudent == 'S'):
#     qtdStudents = int(input("Quantos alunos deseja cadastrar? "))
#     id = input("Qual o id da aula em que deseja adicionar novos alunos? ")
#     students = newStudents(qtdStudents)
#     aula.addStudents(id, students)
# else:
#     pass

#Leia as todas as aulas cadastradas
allClasses = aula.getClasses()

#Atualizar uma aula
updateClass = input("Deseja atualizar o nome de alguma aula? (S - sim | N - não) ")

if(updateClass == 'S'):
    id = input("ID da aula: ")
    subject = input("Nome da aula: ")
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


writeAJson(allClasses, "Aulas")
