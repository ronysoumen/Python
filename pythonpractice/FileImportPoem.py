countwords={}
import statistics as s
with open("poem.txt", "r") as f:
    for line in f:
        for words in line.split():
            #print(words)
            if countwords.get(words):
                countwords[words]=int(countwords.get(words))+1
            #     countwords[words]=countwords.get(words,0) + 1
            else:
                countwords[words] = 1
    max = 0
    maxkey=""
    for k,v in countwords.items():

        if v>max:
            max=v
            maxkey=k
        else:
            continue

    #print(maxkey)
    for k,v in countwords.items():
        if(v==max):
            print(k)
        else:
            continue




