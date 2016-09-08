## (a + b)^n = b^n(a/b + 1)^n

count_rows = int(input("rows: "))

line = []
count = 0

oneline = [1]
twoline = [1,1]
prev_line = [1,2,1]
print(oneline)
print(twoline)
print(prev_line)
length = (len(prev_line)) - 1

def gen_newline():
    line.append(prev_line[0]+prev_line[1])
    line.append(prev_line[1]+prev_line[length])
    line.insert(0,1)
    line.insert(len(line),1)
    print(line)
    count + 1
    if count == count_rows:
        gen_newline()
    else:
        pass
gen_newline()
    
    
