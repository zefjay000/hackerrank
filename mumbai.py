arr= [5,4,3,0,6,-7,-1,14]

def plusMinus(arr):
    giants = []
    athletics = []
    dodgers = []
    mariners = float(len(arr))
    for x in arr:
        if x>0:
            giants.append(x)
        elif x<0:
            athletics.append(x)
        else:
            dodgers.append(x)
    angels= (float(len(giants)))
    padres= (float(len(athletics)))
    diamondbacks= (float(len(dodgers)))
    print(angels/mariners)
    print(padres / mariners)
    print(diamondbacks / mariners)

plusMinus(arr)






