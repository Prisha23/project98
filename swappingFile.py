def swapFileData():
    data_a=input("sample1.txt:")
    numberofwords=0
    file=open(data_a,"r")
    file=open(data_a,"w")
    print("number of words: ")
    print(numberofwords)

    data_b=input("sample2.txt:")
    numberofwords=0
    file=open(data_b,"r")
    file=open(data_b,"w")

    numberofwords=numberofwords+len(words)
    print("number of words: ")
    print(numberofwords)

swapFileData()