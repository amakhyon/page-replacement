import collections 

sequence = []


def accept():
    global sequence,sequence_size,frame_size
    sequence_size = input("  Enter the size of string : ")
    for i in range(sequence_size):
        sequence.append(input(" Enter [%2d] : " % (i+1)))
    frame_size = input("  Enter pages frame size : ")
def use_data():
    global sequence,sequence_size,frame_size
    sequence_size = 12
    frame_size = 3
    sequence = [2,3,2,1,5,2,4,5,3,2,5,2]

#First In First Out pages Replacement Algorithm
def fifo():
    global sequence,sequence_size,frame_size
    f = -1
    page_faults = 0
    pages = []
    for i in range(frame_size):
        pages.append(-1)

    for i in range(sequence_size):
        flag = 0
        for j in range(frame_size):
            if(pages[j] == sequence[i]):
                flag = 1
                break

        if flag == 0:
            f=(f+1)%frame_size
            pages[f] = sequence[i]
            page_faults+=1
            print "\n %d ->" % (sequence[i]),
            for j in range(frame_size):
                if pages[j] != -1:
                    print pages[j],
                else:
                    print "-",
        else:
            print " \n %d ->" % (sequence[i]),
            for j in range(frame_size):
                if pages[j] != -1:
                    print pages[j],
                else:
                    print "-",
            
    print "  Total pages faults : %d." % (page_faults)
  
  
def mfu():
    global sequence,sequence_size,frame_size
    index = 0
    page_faults = 0
    pages = []
    for i in range(frame_size):
        pages.append(-1)

    for i in range(sequence_size):
        flag = 0
        for j in range(frame_size):
            if(pages[j] == sequence[i]):
                flag = 1
                break
            
        if flag == 0:
            if pages[index] != -1:
                max = 0
                for page in range(frame_size):
                    flag = 0
                    j = i # i is current entry in sequence
                    while j>=0:
                        j-=1
                        if(pages[page] == sequence[j]):
                            flag = 1
                            break
                    if (flag == 1 and max < j):
                        max = j
                        index = page

            pages[index] = sequence[i]
            index=(index+1)%frame_size
            page_faults+=1
            print " \n %d ->" % (sequence[i]),
            for j in range(frame_size):
                if pages[j] != -1:
                    print pages[j],
                else:
                    print "-",
        else:
            print " \n %d ->" % (sequence[i]),
            for j in range(frame_size):
                if pages[j] != -1:
                    print pages[j],
                else:
                    print "-",
            
    print "  Total pages faults : %d." % (page_faults)
def lru():
    global sequence,sequence_size,frame_size
    index = 0
    page_faults = 0
    pages = []
    for i in range(frame_size):
        pages.append(-1)

    for i in range(sequence_size):
        flag = 0
        for j in range(frame_size):
            if(pages[j] == sequence[i]):
                flag = 1
                break
            
        if flag == 0:
            if pages[index] != -1:
                min = 999
                for page in range(frame_size):
                    flag = 0
                    j = i # i is current entry in sequence
                    while j>=0:
                        j-=1
                        if(pages[page] == sequence[j]):
                            flag = 1
                            break
                    if (flag == 1 and min > j):
                        min = j
                        index = page

            pages[index] = sequence[i]
            index=(index+1)%frame_size
            page_faults+=1
            print " \n %d ->" % (sequence[i]),
            for j in range(frame_size):
                if pages[j] != -1:
                    print pages[j],
                else:
                    print "-",
        else:
            print " \n %d ->" % (sequence[i]),
            for j in range(frame_size):
                if pages[j] != -1:
                    print pages[j],
                else:
                    print "-",
            
    print "  Total pages faults : %d." % (page_faults)

def optimal():
    global sequence,sequence_size,frame_size
    index = 0
    page_faults = 0
    pages = []
    for i in range(frame_size): #initialize pages with empty spaces
        pages.append(-1)

    for i in range(sequence_size):
        flag = 0
        for j in range(frame_size): 
            if(pages[j] == sequence[i]): # if the current number exists in frame
                flag = 1
                break
            
        if flag == 0:
            if pages[index] != -1:
                max = -1
                for page in range(frame_size):
                    flag = 0
                    j =  i
                    while j<sequence_size-1:
                        j+=1
                        if(pages[page] == sequence[j]):
                            flag = 1
                            break
                    if (flag == 1 and min < j): 
                        max = j
                        index = page

            pages[index] = sequence[i]
            index=(index+1)%frame_size
            page_faults+=1
            print " \n %d ->" % (sequence[i]),
            for j in range(frame_size):
                if pages[j] != -1:
                    print pages[j],
                else:
                    print "-",
        else:
            print " \n %d ->" % (sequence[i]),
            for j in range(frame_size):
                if pages[j] != -1:
                    print pages[j],
                else:
                    print "-",
            
    print "  Total pages faults : %d." % (page_faults)

    

#Displaying the menu and calling the functions.    
while True:
    print " 1. use default config & data " #frame size = 3, sequence = 2 3 2 1 5 2 4 5 3 2 5 2
    print " 2. FIFO"
    print " 3. LRU"
    print " 4. OPT"
    print " 5. MFU " 
    print " 6. Input data & config "
    ch = input(" Select : ")

    if ch == 1:
        use_data()
    if ch == 2:
        fifo()
    if ch == 3:
        lru()
    if ch == 4:
        optimal()
    if ch == 5:
        mfu()
    if ch == 6:
        accept()
        