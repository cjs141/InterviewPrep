# Complete the twoStrings function below.
def twoStrings(s1, s2):
    letters = set()
    for i in range(0, len(s1)):
        letters.add(s1[i])
    for i in range(0, len(s2)):
        if s2[i] not in letters:
            continue
        else:
            return "YES"
    return "NO" 
    