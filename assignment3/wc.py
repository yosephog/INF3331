import sys

'''
this program reads a given or a group of files and returns the number
of lines,characters and words
'''
counter=1 # used as index when looping through multiply files

# loop untill the length og argv is reached
while counter < len(sys.argv):
    print("file name -:", sys.argv[counter])
    f=open(sys.argv[counter],"r")
    wordCounter=0 # used to count words becomes zero for every file
    emptyLine=0   # counts emptyLine
    charCounter=0
    mylist=[]

    for s in f:
        emptyLine=emptyLine + len(s.split('\n '))
        wordCounter=wordCounter+ len(s.split(' '))

        for t in s.split(' '):
            charCounter=charCounter + len(list(t))
            
    # am minusing here becuase emptyline is also counted as character which is not
    charCounter=charCounter - emptyLine
    print('the number of words ', wordCounter)
    print('number of emptyline',emptyLine)
    print('number of character',charCounter)
    print("--------------------------------------------")
    counter+=1
