import pygame
import random
pygame.init()

class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0 
    RED = 255, 0, 0 
    BLUE = 0, 0, 255 
    BACKGROUND = WHITE
    SIDE_PAD = 100
    TOP_PAD = 150
    
    GRADIENTS = [
        (110, 110, 110),
        (150, 150, 150),
        (190, 190, 190)
    ]
    
    
    def __init__(self, width, height, sortList):
        self.width = width
        self.height = height
        
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sort Visualiser")
        
        self.set_list(sortList)

    def set_list(self, sortList):
            self.sortList = sortList
            self.minVal = min(sortList)
            self.maxVal = max(sortList)
            self.blockWidth = round((self.width - self.SIDE_PAD) / len(sortList))
            self.blockHeight = round((self.height - self.TOP_PAD) / (self.maxVal - self.minVal))
            
            self.start_x = self.SIDE_PAD // 2

def generateRandomList(numElements, minVal, maxVal):
    sortList = []
    
    for _ in range(numElements):
        sortList.append(random.randint(minVal, maxVal))
    return sortList

def draw(drawInformation):
    drawInformation.window.fill(DrawInformation.BACKGROUND)
    drawList(drawInformation)
    pygame.display.update()

def drawList(drawInformation):
    sortList = drawInformation.sortList
    
    for i, val in enumerate(sortList):
        x = drawInformation.start_x + i * drawInformation.blockWidth
        y = drawInformation.height - (val - drawInformation.minVal) * drawInformation.blockHeight
        
        color = drawInformation.GRADIENTS[i % 3]
        pygame.draw.rect(drawInformation.window, color, \
                        (x, y, drawInformation.blockWidth, drawInformation.height))


def main():
    run = True
    clock = pygame.time.Clock()
    
    numElements = 50
    minVal = 0 
    maxVal = 100
    
    sortList = generateRandomList(numElements, minVal, maxVal)
    drawInfo = DrawInformation(1000, 1000, sortList)
    
    while run:
        clock.tick(60)
        
        draw(drawInfo)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type != pygame.KEYDOWN:
                continue 
            
            if event.key == pygame.K_r:
                sortList = generateRandomList(numElements, minVal, maxVal)
                drawInfo.set_list(sortList)
    
    exit()
    
if __name__ == "__main__":
    main()