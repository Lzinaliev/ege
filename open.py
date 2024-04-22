file = open('1.txt')
print(file.read())
file.close()

file = open('1.txt',"w")
file.write("4321")
file.close()

with open("№4.txt") as g:
    list = g.readlines()
print(list[0].split())
for i in list:
    print(i.split())


with open("№4.txt", "r") as x:
    for line in x:
        print(line.strip())
