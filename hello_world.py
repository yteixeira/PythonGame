import random
from enemyClass import Enemy

max = 7
rows, cols = (max, max)
gameOver = False

posX = random.randint(0, max -1)
posY = random.randint(0, max -1)
value = ""

goal = ' O '
gPosX = random.randint(0, max -1)
gPosY = random.randint(0, max -1)

enemy = ' E '

enemy1Pos = Enemy(random.randint(0, max -1), random.randint(0, max -1))
enemy2Pos = Enemy(random.randint(0, max -1), random.randint(0, max -1))

def Enemy_Move(x):
    if x > 0 and x < max -1:
        x += random.randint(-1, 1)
    elif x == 0:
        x += random.randint(0, 1)
    elif x == max -1:
        x += random.randint(-1, 0)

    return x

while gameOver == False:
    grid = [[' . ' for i in range(cols)] for j in range(rows)]
    grid[gPosY][gPosX] = goal
    grid[posY][posX] = ' X '
    grid[enemy1Pos.posY][enemy1Pos.posX] = enemy
    grid[enemy2Pos.posY][enemy2Pos.posX] = enemy

    for row in grid:
        print(' '.join(map(str, row)))

    #win and lose states
    if grid[posY][posX] == grid[gPosY][gPosX]:
        print("YOU WON !!")
        gameOver = True
        break
    elif grid[posY][posX] == grid[enemy1Pos.posY][enemy1Pos.posX] or grid[posY][posX] == grid[enemy2Pos.posY][enemy2Pos.posX]:
        print("You Lost :(")
        gameOver = True
        break
    else:
        value = input("What is your move? ")

    #player input manager
    if value == "up" and posY > 0:
        posY -= 1
    elif value == "down" and posY < max -1:
        posY += 1
    elif value == "left" and posX > 0:
        posX -= 1
    elif value == "right" and posX < max -1:
        posX += 1
    elif value == "end":
        print("see you later alligator")
        gameOver = True
    else:
        print("invalid value. Use 'up', 'down', 'left' or 'right' and make sure you are within boundary")

    #Enemy Movement
    enemy1Pos.enemyMove(max)
    enemy2Pos.enemyMove(max)