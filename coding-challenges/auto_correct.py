# Example:
# For
# trainingWords = ["without", "night", "text", "cellar", "requirement", "some", "park", "instinct", "flourish", "computing", "vision",
#                    "mean", "round", "mistakes", "vain", "exemption", "fast"]
# and typedWords = ["some", "tex", "whith", "mistakesd"]
# the output should be "some text without mistakes"

import numpy as np

def levenshtein_dist(str1, str2):
    rows = len(str1) + 1
    columns = len(str2) + 1
    distance = np.zeros((rows, columns), dtype=int)
    
    for i in range(1, rows):
        for j in range(1, columns):
            distance[i][0] = i
            distance[0][j] = j
    
    for col in range(1, columns):
        for row in range(1, rows):
            if str1[row-1] == str2[col-1]:
                cost = 0
            else:
                cost = 1
            
            distance[row][col] = min(distance[row-1][col]+1,
                                    distance[row][col-1]+1, 
                                    distance[row-1][col-1]+cost)    
    return distance[row][col]
    
def AutoCorrect(trainingWords, typedWords):
    dist = {}
    joined_words = []
    final = []
    
    for typedword in typedWords:
        for trainingword in trainingWords:            
            dist[trainingword] = levenshtein_dist(typedword, trainingword)
            
        dist = sorted(dist.items(), key=lambda x: x[1])
        joined_words.append(list(dist[0]))
        dist = {}
    
    for i in range(len(joined_words)):
        final.append(joined_words[i][0])        
        
    return " ".join(final)
        