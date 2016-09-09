## (a + b)^n = b^n(a/b + 1)^n

count_rows = int(input("rows: "))

line = []
line2 = []
count = 0

oneline = [1]
twoline = [1,1]
prev_line = [1,2,1]
print(oneline)
print(twoline)
print(prev_line)
length = (len(prev_line)) - 1

def gen_lines():
    for x in range(0,count_rows):
        pass
    line2.append(line[0]+line[1])
    line2.append(line[len(line)-1]+line[len(line)-2])
    line.pop()
    del line[0]
    x = line[0]+line[1]
    line2.insert(1,x)
    line2.insert(0,1)
    line2.insert(len(line2),1)
    print(line2)
    
def gen_4line():
    line.append(prev_line[0]+prev_line[1])
    line.append(prev_line[1]+prev_line[length])
    line.insert(0,1)
    line.insert(len(line),1)
    print(line)
    if count_rows == 4:
        pass
    else:
        gen_lines()
gen_4line()
