'''
#exceção ZeroDivisionError

a = int(input('digite o primeiro numero'))
b = int(input('digite o divisor'))
cond = True

try:
    print(a/b)
    
except ZeroDivisionError:
    print("Não é possível dividir por zero! Troque o divisor")
'''  
'''
print('Give me 2 numbers, and I will divide them.')
print("Enter 'q' to quit.")

while True:
    first_num = input('\nFirst Number:')
    if first_num == 'q':
        break
    second_num = input('Second Number:')
    if second_num == 'q':
        break
    
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print('You cant divide by 0.')
    else:   
        print(answer)
'''

# excecao FileNotFoundError

filename = 'arquivotestado.txt'

try:
    with open(filename) as f_obj:
        contents = f.obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist;"
    print(msg)