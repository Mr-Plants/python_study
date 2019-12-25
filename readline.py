file1=open('demo.txt')

while True:
    line=file1.readline()
    if len(line)==0:
        break
    print line

file1.close()
    
