from nltk.corpus import wordnet as wn
def SimScore(synsets1, synsets2):
    """
    Purpose: Computes sentence similarity using Wordnet path_similarity().
    Input: Synset lists representing sentence 1 and sentence 2.
    Output: Similarity score as a float
    """


    # print("-----")
    # print("Synsets1: %s\n" % synsets1)
    # print("Synsets2: %s\n" % synsets2)

    sumSimilarityscores = 0
    scoreCount = 0
    avgScores = 0
    # For each synset in the first sentence...
    for synset1 in synsets1:

        synsetScore = 0
        similarityScores = []

        # For each synset in the second sentence...
        for synset2 in synsets2:

            # Only compare synsets with the same POS tag. Word to word knowledge
            # measures cannot be applied across different POS tags.
            if synset1.pos() == synset2.pos():

                # Note below is the call to path_similarity mentioned above.
                synsetScore = synset1.path_similarity(synset2)

                if synsetScore != None:
                   #print("Path Score %0.2f: %s vs. %s" % (synsetScore, synset1, synset2))
                    similarityScores.append(synsetScore)

                # If there are no similarity results but the SAME WORD is being
                # compared then it gives a max score of 1.
                elif synset1.name().split(".")[0] == synset2.name().split(".")[0]:
                    synsetScore = 1
                    #print("Path MAX-Score %0.2f: %s vs. %s" % (synsetScore, synset1, synset2))
                    similarityScores.append(synsetScore)

                synsetScore = 0

        if (len(similarityScores) > 0):
            sumSimilarityscores += max(similarityScores)
            scoreCount += 1

    # Average the summed, maximum similarity scored and return.
    if scoreCount > 0:
        avgScores = sumSimilarityscores / scoreCount

    #print("Func Score: %0.2f" % avgScores)
    return (avgScores)



if __name__ == "__main__":
    print(SimScore(wn.synsets("计算机",lang="cmn"),wn.synsets("酒",lang="cmn")))