def getFixedPointsXY(i, numSides,w,h):
    # temporario, vo fazer essa funcao direito dps
    if numSides == 3:
        if i == 0:
            return w/2, h
        elif i == 1:
            return 0, 0
        elif i == 2:
            return w,0
        else:
           return -1,-1

def biggerPoint(x,y):
    # temporario, vo tirar essa funcao dps
    
    print(x,y)
    
    point(x,y)
    point(x+1,y)
    point(x-1,y)
    point(x,y+1)
    point(x,y-1)

def setup():
    global numSides,x,y,fixedPoints
    size(800,600)
    background(200,180,5)
    frameRate(25)
    
    
    w = 800
    h = 600
    x = w/2
    y = h/2
    numSides = 3
    fixedPoints = [getFixedPointsXY(i,numSides,w,h) for i in range(numSides)]

    
    
    for i in range(numSides):
        biggerPoint(fixedPoints[i][0],fixedPoints[i][1])
    
def draw():
    global x,y,fixedPoints
    randomNum = int(random(0,numSides));
    
    if randomNum <= numSides:
        x = (x + fixedPoints[randomNum][0])/2
        y = (y + fixedPoints[randomNum][1])/2
    else:
        print('aconteceu algo errado hein cara\n c o randomNum provavelmente')
    
    biggerPoint(x,y)