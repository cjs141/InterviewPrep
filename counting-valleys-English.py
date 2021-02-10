def countingValleys(steps, path):
    elev = 0
    valleys = 0
    for i in path:
        if i == "D":
            if(elev == 0):
                valleys += 1
            elev += 1
        if i == "U":
            elev -= 1
    return valleys