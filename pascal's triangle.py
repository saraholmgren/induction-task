prevline = [1]
lines_left = int(input("input rows: "))

def loopymcloopface(prevline,lines_left):
    while lines_left >= 0:
        newline = []
        print(prevline)
        newline.append(1)
        for i in range(1,len(prevline)+1):
            try:
                newline.append(int(prevline[i])+int(prevline[i-1]))
            except:
                newline.append(1)
        lines_left -= 1
        prevline = newline
loopymcloopface(prevline,lines_left)
