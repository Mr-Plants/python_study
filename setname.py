#While
while True:
    ms=raw_input('input a name:')
    if ms=='quit':
        break
    if len(ms)<3:
        print 'name too short'
        continue
    print 'success!'
print 'quit set name'
