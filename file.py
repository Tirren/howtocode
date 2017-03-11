def nLines(n):
    with open('test.txt', encoding='cp1252') as f:
        line = f.readlines()
        print(*(line[i] for i in range(n)), sep='')

def delStr(n):
    line = open('test.txt', encoding='cp1252').readlines()
    line.remove(line[n-1])
    with open('test.txt', mode='w', encoding='cp1252') as f:
        f.writelines(line)

