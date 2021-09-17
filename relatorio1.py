import pandas as pd
import unidecode
import util.average as avg

df = pd.read_excel('./samples/sample.xlsx')


def getSubject():
    header = df.columns
    subject = header[2]

    return subject


def getColumns():
    columns = []

    for col in range(df.shape[1]):
        value = str(df.iat[1, col])
        if (value != 'nan'):
            columns.append(unidecode.unidecode(value))

    return columns


def getStudents(columns):
    students = []

    for row in range(df.shape[0]):
        if(row > 1):
            i = 0
            student = {}

            for col in range(df.shape[1]):
                value = str(df.iat[row, col])

                if(value.lower() != 'nan'):
                    student[columns[i]] = value
                    i += 1

            students.append(student)

    return students


def printStudents(students, subject):
    for student in students:
        listCheckpoints = [float(student['checkpoint1']), float(
            student['checkpoint2']), float(student['checkpoint3'])]
        checkpointAverage = float(
            avg.calcCheckpoints(checkpoints=listCheckpoints))

        listChallenges = [float(student['Challenge Sprint 3']), float(
            student['Challenge Sprint 4'])]
        challengeAverage = float(avg.calcChallenges(challenges=listChallenges))

        MS1Value = float(student['Semestre_1'])

        finalGCS = avg.calcFinalGS(
            ms1=MS1Value, checkpointAverage=checkpointAverage, challengeAverage=challengeAverage)

        print("\n\n===================================================")
        print(" Disciplina: " + subject + "\n")
        print(" RM: %g" % float(student['RM']) + ", " + student['Nome'] + "\n")

        print(" Semestre 1: " + str(MS1Value) + "\n")

        print(" \tSemestre 2:")

        print(" Checkpoints (média): " + str(checkpointAverage))
        print(" Challenge (média): " + str(challengeAverage) + "\n")
        print("---------------------------------------------------")
        print(" Nota mínima na Global Solution para aprovação: " + str(finalGCS))
        print("===================================================")


subject = getSubject()
columns = getColumns()
students = getStudents(columns)

printStudents(students, subject)
