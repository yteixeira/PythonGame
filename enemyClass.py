import random

class Enemy():
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def enemyMove(self, boundaryMax):
        if self.posX > 0 and self.posX < boundaryMax - 1:
            self.posX += random.randint(-1, 1)
        elif self.posX == 0:
            self.posX += random.randint(0, 1)
        elif self.posX == boundaryMax - 1:
            self.posX += random.randint(-1, 0)

        if self.posY > 0 and self.posY < boundaryMax - 1:
            self.posY += random.randint(-1, 1)
        elif self.posY == 0:
            self.posY += random.randint(0, 1)
        elif self.posY == boundaryMax - 1:
            self.posY += random.randint(-1, 0)