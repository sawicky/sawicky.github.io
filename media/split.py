def itercount(filename):
    return sum(1 for _ in open(filename, 'rb'))

file = input("Enter name of wordlist to split\n")
number = input("Enter how many lines to keep. The rest will be split into a new file\n")
with open(file, 'r', encoding="ascii", errors="surrogateescape") as inputFile:
    count = 0
    linesRemaining = int(number)
    lines = inputFile.readlines()
    newFileName = number+'-'+file
    newFile = open(newFileName, 'w')
    print("Analyzing file")
    totalLines = itercount(file)
    print("Total lines: "+ str(totalLines))
    remainingLines = totalLines - count

    for line in lines:
        if count!=int(number):
            print("\rReading line " +str(count), sep=' ', end='', flush=True)
            count += 1
        else:
            newFile.write(line.encode('ascii', 'ignore').decode('ascii'))
            print("\rWriting line into new file. Remaining: " + str(remainingLines), sep=' ', end='', flush=True)
        remainingLines -= 1
    newFile.close()
    inputFile.close()
    print('\n')


