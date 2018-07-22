from __future__ import print_function

todo = open('file1.txt', 'a')
print('to do something in todo', file=todo)
todo.close()

todo1 = open('file1.txt', 'r')
for chore in todo1:
    print(chore, end='')
todo1.close()
