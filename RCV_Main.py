# Ranked choice voting algorithm
# Luke Maymir

import numpy

lastVote = False
rankList=[]
numCan = int(input("Please input the number of candidates:\n")) #Number of candidates
rank = numpy.zeros(numCan)

def count(voteList):
    tally = numpy.zeros(len(voteList[0]))
    for vote in voteList:
        for i in range(len(vote)):
            if vote[i] == 1:
                tally[i] += 1
    return tally

def eliminate(voteList, elimInd):
    newVL = []
    for vote in voteList:
        if vote[elimInd] == 1:
            vote -= 1
        newVL.append(vote)    
    return newVL

while not lastVote:

    print("\n")
    for i in range(numCan):
        rank[i] = int(input("Please input the ranking for Canditate "+str(i+1)+":\n"))
    print("\n")
    
    rankList.append(rank.copy())

    resp = (input("Enter another vote? (Y/N)\n"))

    if resp == "N":
        lastVote = True

done = False
rnd = 1

while not done:
    
    voteTally = count(rankList)
    print("\nRound "+str(rnd)+":\n")
    for x in range(numCan):
        print("\nCandidate "+str(x+1)+": "+str(voteTally[x]))

    maxVote = numpy.max(voteTally)
    maxIndTup = numpy.where(voteTally == maxVote)
    maxIndA = maxIndTup[0]
    maxInd = maxIndA[0]
    sumVote = numpy.sum(voteTally)
    minVote = numpy.min(voteTally)
    minIndTup = numpy.where(voteTally == minVote)
    minInd = minIndTup[0]
    numMin = len(minInd)
    leftIndTup = numpy.where(voteTally > 0)
    numLeft = len(leftIndTup[0])

    if maxVote > (0.5*sumVote):
        done = True
        result = "Candidate "+str(maxInd + 1)+" wins!"
    elif numLeft == 1:
        done = True
        result = "No candidate was able to obtain a majority of the vote."
    elif maxVote == minVote:
        done = True
        result = "It's a tie!"
    elif rnd >= (numCan -1):
        done = True
        result = "Unable to determine winner."
    else:
        for i in minInd:
            rankList = eliminate(rankList, i)

    rnd += 1
    
print("\n\n"+result+"\n\n")

for x in range(numCan):
    print("\nCandidate "+str(x+1)+": "+str(voteTally[x]))