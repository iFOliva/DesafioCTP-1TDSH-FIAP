import pandas as pd
import unidecode
import average as avg

df = pd.read_excel('sample.xlsx')

def getSubject(df):

    header = df.columns
    subject = header[2]

    return subject

def getColumns(df):

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

                value = str(df.iat[row,col])

                if(value.lower() != 'nan'):
                    
                    student[columns[i]] = value
                    i += 1
        
            students.append(student)

    return students

def printStudents(students, subject):

    for student in students:
              
        listCheckpoints = [float(student['checkpoint1']), float(student['checkpoint2']), float(student['checkpoint3'])]
        listChallenges = [float(student['Challenge Sprint 3']), float(student['Challenge Sprint 4'])]

        checkpointAverage = float(avg.calcCheckpoints(listCheckpoints))
        challengeAverage = float(avg.calcChallenges(listChallenges))

        MS1Average = float(student['Semestre_1'])

        finalGCS = avg.calcFinalGS(MS1Average, checkpointAverage, challengeAverage)

        print("Disciplina : " + subject)
        print(student['RM'] + " " + student['Nome'])
        print("Semestre 1:" + str(MS1Average))
        print("\tSemestre 2:")
        print("Checkpoints (média) " + str(checkpointAverage))
        print("Challenge (média) " + str(challengeAverage))
        print("Nota mínima na Global Solution para aprovação: " + str(finalGCS))

        print('\t\t\t')


subject = getSubject(df)
columns = getColumns(df)
students = getStudents(columns)

printStudents(students, subject)