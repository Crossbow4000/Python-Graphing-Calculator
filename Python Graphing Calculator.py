gridRender = {}

yCoord = -10000

for xGrid in range(-10, 11):
    for yGrid in range(-10, 11):
        gridRender[xGrid, yGrid] = "░░"
        gridRender[0, yGrid] = "▒▒"
        gridRender[xGrid, 0] = "▒▒"

for xCoord in range(-10, 11):
    try:
        yCoord = round(sin(xCoord))
    except:
        yCoord = -10000
    gridRender[xCoord, yCoord] = "██"
    
for yRender in range(10, -11, -1):
    print(''.join(gridRender[xRender, yRender] for xRender in range(-10, 11)))
