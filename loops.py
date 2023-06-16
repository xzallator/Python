
def loops_iterations():
    n = 0
    while True:
        if n == 3:
            break
        print(n)
        n = n + 1
loops_iterations()

def definite_loops():
    for i in [2, 1, 5]:
        print(i)
definite_loops()

while True:
    userInput = int(input('LOOPS CASE : \n\n1.Loops Iterations\n2.Definite Loops\n\nCHOOSE THE PROGRAM : '))
    if(userInput == 1):
        loops_iterations()
    elif(userInput == 2):
        definite_loops()
    else:
        break