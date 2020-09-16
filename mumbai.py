redsox=[[1,2,3,4],
        [9,3,9,5],
        [4,5,6,3],
        [5,8,7,9]]


reds= (len(redsox))

cubs=[]
def hello(l):
    r= 0
    o=reds-1
    while r<reds:
        cardinals= l[r][o]
        cubs.append(cardinals)
        r=r+1
        o=o-1

hello(redsox)
rockies= sum(cubs)

######################################################

orioles= []
def hey(n):
    q = 0
    while q<reds:
        marlins= n[q][q]
        orioles.append(marlins)
        q = q + 1

hey(redsox)
whitesox= sum(orioles)

result= abs(whitesox-rockies)
print(result)