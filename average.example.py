import average as avg

chk = avg.calcCheckpoints([5, 5, 2])
chg = avg.calcChallenges([5, 5])
gs = avg.calcGS([5, 5])

print(
    f"A média do aluno é: {avg.calcMedia(finalCheckpoint=chk, finalChallenge=chg, finalGS=gs)}")
