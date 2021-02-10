def sockMerchant(n, ar):
    unique = {0}#to keep track of new numbers encountered
    counter = 0#to keep track of number of duplicates
    pairs = 0#to keep track of number of pairs
    for i in range(0, len(ar)):
        pairs = pairs + int(counter / 2)
        counter = 0
        if ar[i] not in unique:
            print(ar[i])
            unique.add(ar[i])
            counter += 1
            for j in range(i+1, len(ar)):
                if ar[i] == ar[j]:
                    counter += 1
                
    return pairs