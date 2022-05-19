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
    
    def __init__(self, width, height, sortList):
        self.width = width
        self.height = height
        
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sort Visualiser")
        
        self.set_list(sortList)
        
        def set_list(self, sortList):
            self.sortList = sortList
            self.min = min(sortList)
            self.max = max(sortList)
            self.block_width = (self.width - selF.SIDE_PAD) / len(sortList)