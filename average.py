def calcCheckpoints(checkpoints: list) -> int:
    """Recebe uma lista de 3 notas e devolve a média aritmética dos dois maiores números.

    Argumentos da função:
    checkpoints - uma lista de 3 notas. Ex: [5, 6.5, 10]
    """

    average = 0

    checkpoints.sort(reverse=True)

    for i in checkpoints[0:2]:
        average += round(i, 1)

    return average/2


def calcChallenges(challenges: list) -> int:
    """Recebe uma lista de 2 notas e devolve a média aritmética.

    Argumentos da função:
    challenges - uma lista de 2 notas. Ex: [8.5, 9]
    """

    average = 0

    for i in challenges:
        average += round(i, 1)

    return average/2


def calcGS(sprints: list) -> int:
    """Recebe uma lista de 2 notas e devolve a média aritmética.

    Argumentos da função:
    sprints - uma lista de 2 notas. Ex: [10, 2.5]
    """

    average = 0

    for i in sprints:
        average += round(i, 1)

    return average/2


def calcMedia(finalCheckpoint: int, finalChallenge: int, finalGS: int):
    """Recebe a média de checkpoints, challenges e global solution e devolve a média ponderada final.

    Fórmula: ((finalCheckpoint + finalChallenge) / 2 * 0.4) + (finalGS * 0.6)

    Argumentos da função:
    finalCheckpoint - a média aritmética dos checkpoints. Ex: 7,
    finalChallenge - a média aritmética dos challenges. Ex: 10,
    finalGS - a média aritmética entre as sprints da Global Solution. Ex: 8.5
    """

    firstAverage = (finalCheckpoint + finalChallenge)/2

    msFinal = round((firstAverage
                    * 0.4 + finalGS * 0.6), 1)

    return msFinal
