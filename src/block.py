import pygame

class Block:
    def __init__(self, screen: pygame.Surface, position: list, cell_size: int, color: str):
        self.position = position
        self.color = color
        self.screen = screen
        self.cell_size = cell_size
    
    def draw(self):
        x,y = self.position
        pygame.draw.rect(self.screen, self.color, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
    
    def get_position(self):
        return self.position
    
    def set_position(self, new_position: list):
        self.position = new_position