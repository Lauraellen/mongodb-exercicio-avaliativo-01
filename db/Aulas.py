from bson import ObjectId

from db.db import Database

class AulaDB:
    def __init__(self):
        self.db = Database(database="dbaulas", collection="Aulas")
        # self.db.resetDatabase()
        self.collection = self.db.collection

    def newTeacher(self, teacher: str, specialty: str):
        res = {"professor": teacher, "especialidade": specialty}
        return res

    def newClass(self, className: str, teacher: object, students: list):
        res = self.collection.insert_one({"assunto": className, "professor": teacher, "alunos": students})
        return res.inserted_id

    def getClasses(self):
        res = self.collection.find()
        allClasses = []
        for aula in res:
            allClasses.append(aula)
        return allClasses


    def updateClass(self, id: str, assunto: str):
        res = self.collection.update_one({"_id": ObjectId(id)}, {"$set": {"assunto": assunto}})
        return res.modified_count

    def deleteClass(self, id):
        res = self.collection.delete_one({"_id": ObjectId(id)})
        return res.deleted_count

    def newStudents(self, qtdStudents: int):
        # Cadastre os alunos
        students = []
        while (len(students) < qtdStudents):
            nomeAluno = input("Nome do aluno: ")
            mat = int(input("Matrícula: "))
            curso = input("Curso: ")
            periodo = int(input("Período: "))

            students.append({"nome": nomeAluno, "matricula": mat, "curso": curso, "periodo": periodo})
            print(students)

        else:
            pass

        return students