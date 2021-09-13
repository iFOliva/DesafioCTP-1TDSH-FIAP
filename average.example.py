import average as avg

checkpointAverage = avg.calcCheckpoints([5, 5, 2])
challengeAverage = avg.calcChallenges([5, 5])
GSAverage = avg.calcGS([5, 5])

msFinal = avg.calcMS(challengeAverage=challengeAverage,
                     checkpointAverage=checkpointAverage, GSAverage=GSAverage)

print(
    f"A média do aluno é: {msFinal}")
