import pygame
from Menu import *
from Displayable import *
from Displayable import ManiaStage
import os

# Game
class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.RIGHT_KEY, self.LEFT_KEY = False, False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1920, 1080
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

        self.main_menu = MainMenu(self)
        self.songselect = SongMenu(self)
        self.difficulty = DifficultyMenu(self)
        self.settings = SettingsMenu(self)
        self.volume = VolumeMenu(self)
        self.quit = QuitMenu(self)
        self.curr_menu = self.main_menu
        
        self.mania_stage = ManiaStage(self)

# Game loop
    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.BACK_KEY:
                self.playing= False
            self.window.blit(self.display, (0,0))
            self.s_left()
            pygame.display.update()
            self.reset_keys()


# Check events method
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                    
                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = True
                    
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                    
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                    
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
                    
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True

# Reset keys method
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.RIGHT_KEY, self.LEFT_KEY = False, False, False, False, False, False

# Draw text method
    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)