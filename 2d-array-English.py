# Complete the hourglassSum function below.
def hourglassSum(arr):
    sums = set()
    startRow = 0
    startCol = 0
    for i in range(0, 4):
        for j in range(0,4):
            sums.add(oneHourGlassSum(arr, i, j))
    return max(sums)
        
    

def oneHourGlassSum(arr,startRow,startCol):
    sum = 0
    for i in range(startRow, startRow + 3):
        for j in range(startCol, startCol + 3):
            if i == startRow + 1:
                if j == startCol:
                    continue
                if j == startCol + 2:
                    continue
            sum += arr[i][j]
    return sum
    