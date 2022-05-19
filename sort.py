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
            self.block_width = round((self.width - selF.SIDE_PAD) / len(sortList))
            self.block = round((self.height - self.TOP_PAD) / (self.maxVal - self.minVal))
            
            self.start_x = self.SIDEPAD // 2

def generateRandomList(numElements, minVal, maxVal):
    sortList = []
    
    for _ in range(numElements):
        sortList.append(random.randint(minVal, maxVal))
    return sortList

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
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event == pygame.QUIT:
                run == False
                
    
    pygame.quit()
    
if __name__ == "__main__":
    main()