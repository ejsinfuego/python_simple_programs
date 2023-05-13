file = open('ej.dat', 'w')
file.write('Hello, Friend')
file.close()

file = open('ej.dat', 'r')
f = file.read()
print(f)

def copyFile(oldFile,newFile):
    f1 = open(oldFile, 'r')
    f2 = open(newFile, 'w')
    while True:
        text = f1.read(50)
        if text == '':
            break
        f2.write(text)
        f1.close()
        f2.close()
        return
    
copyFile('ej.dat', 'ej.txt')

c = open("trial.dat", "w")
c.write("line one\nline two\nline three\n")
c.close()

c = open('trial.dat', 'r')
print(c.readline())
print(c.readlines())






