import pandas as pd

tabela = pd.read_excel("./samples/notas_planilha_pronta.xlsx")


def calcMSemGS(semestre1: int, checkpointAverage: int, challengeAverage: int):
    """Recebe a nota do semestre 1, a média de checkpoints, challenges e retorna o nome e RM dos alunos aprovados sem a nota do Global Solutions.
    Fórmula: ((semestre1 * 0.4) + (((checkpointAverage + challengeAverage) / 2) * 0.4)* 0.6)
    Argumentos da função:
    semestre1 - a média final do primeiro semestre. Ex: 10,
    checkpointAverage - a média aritmética dos checkpoints. Ex: 7,
    challengeAverage - a média aritmética dos challenges. Ex: 10,
    """

    secondAverage = (checkpointAverage + challengeAverage)/2

    MSemGS = round((secondAverage * 0.4), 1)

    mediaFinal = round((semestre1 * 0.4 + MSemGS * 0.6), 1)

    if mediaFinal >= 6:

        tabela_nome = (tabela['Unnamed: 1'])
        tabela_rm = (tabela['Disciplina:'])

        for i in range(2, 22):
            print("O aluno(a):", tabela_nome[i], "de RM:",
                  tabela_rm[i], "passou sem precisar da nota do GS")


calcMSemGS(10, 10, 10)
