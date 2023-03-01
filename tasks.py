import numpy as np
import matplotlib.pyplot as plt
import cema


def checkKey(realKey, guessedKey):
    keyLength = len(realKey)
    keyBNum = 0
    for x in range(keyLength):
        if (realKey[x] == guessedKey[x]):
            keyBNum += 1
    print("\t\tCorrect number of key bytes: ", keyBNum)
    return keyBNum


def runCEMA(keyLength=16, numPlainTexts=20, noiseLevel=10, traceDuration=20):
    realKey = np.random.randint(256, size=keyLength)
    plainTexts = cema.genPlainTexts(keyLength, numPlainTexts)
    # print(plainTexts.tolist())
    # print(plainTexts)
    H_all = cema.getHypoMatrices(plainTexts, keyLength)
    traceMatrix = cema.genEMTraces(
        realKey, plainTexts, traceDuration, noiseLevel)
    # print(traceMatrix)
    guessedKey = cema.recoverKey(H_all, traceMatrix, keyLength)
    print("\t\tReal key    : ", realKey)
    print("\t\tGuessed key : ", guessedKey)
    return checkKey(realKey, guessedKey)


def task2():
    keyLength = 16
    noiseLevel = 10
    traceDuration = 20
    testNum = 5  # get mean correct keys
    dataX = []
    dataY = []
    for numPlainTexts in range(10, 200, 10):
        print(">> Running CEMA with plain texts: ", numPlainTexts)
        testRes = 0
        for tID in range(testNum):
            print("\t>> Running test num: ", tID)
            testRes += runCEMA(keyLength, numPlainTexts,
                               noiseLevel, traceDuration)
        print("----------------------------------")
        testRes = testRes / testNum
        dataX.append(numPlainTexts)
        dataY.append(testRes)
    plt.plot(dataX, dataY)
    plt.xlabel("Plain Texts")
    plt.ylabel("Correct Key Bytes")
    plt.show()


def task3():
    keyLength = 16
    numPlainTexts = 200
    traceDuration = 20
    testNum = 5  # get mean correct keys
    dataX = []
    dataY = []
    for noiseLevel in range(2, 20, 2):
        print(">> Running CEMA with noise level: ", noiseLevel)
        testRes = 0
        for tID in range(testNum):
            print("\t>> Running test num: ", tID)
            testRes += runCEMA(keyLength, numPlainTexts,
                               noiseLevel, traceDuration)
        print("----------------------------------")
        testRes = testRes / testNum
        dataX.append(noiseLevel)
        dataY.append(testRes)
    plt.plot(dataX, dataY)
    plt.xlabel("Noise Level")
    plt.ylabel("Correct Key Bytes")
    plt.show()
