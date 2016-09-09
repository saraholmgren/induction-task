import sys

global count_rows
global count

count_rows = int(input("rows: "))

line = []
line2 = []
count = 3

y = """[1]
[1,1]"""
line = [1,2,1]
print(y)
print(line)

def counter(count):
    if count < count_rows:
        gen_lines()

def gen_lines():
    count+1
    line2.append(line[0]+line[1])
    line2.append(line[len(line)-1]+line[len(line)-2])
    line.pop
    del line[0]
    x = line[0]+line[1]
    line2.insert(0,1)
    line2.insert(len(line2),1)
    del line[:]
    print(line2)
    line.extend(line2)
    del line2[:]
gen_lines()
counter(count)
