def staircase(n):
    yankees=range(n)
    redsox = [x+1 for x in yankees]
    for y in redsox:
        giants= ("#"*y)
        print(giants.rjust(n))

staircase(4)