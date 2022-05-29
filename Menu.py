import pygame
from logging import *
from tkinter import *
from tkinter.ttk import *
from time import *
from pygame import *
from PIL import Image, ImageDraw
from Displayable import *

# Music
mixer.init()
pygame.mixer.music.set_volume(0.5)
def menu_music():
    mixer.music.load('kurxxed emeraldz.wav') 
    mixer.music.play(-1, fade_ms=200)
    
menu_music()

def the_perfect_girl_preview():
    mixer.music.load('the perfect girl preview.wav'), mixer.music.play(-1)
    mixer.music.play(-1, fade_ms=200)

        
def dreamcore_preview():
    mixer.music.load('dreamcore preview.wav'), mixer.music.play(-1)
    mixer.music.play(-1, fade_ms=200)
    
def call_me_preview():
    mixer.music.load('call me preview.wav'), mixer.music.play(-1)
    mixer.music.play(-1, fade_ms=200)

# Sound effects
menu_move_sound = mixer.Sound('menu move sound.wav')
menu_select_sound = mixer.Sound('menu select sound2.wav')

# Menu and cursors
class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 40, 40)
        self.cursor_rect2 = pygame.Rect(0, 0, -40, -40)
        self.cursor_rect3 = pygame.Rect(-20, -20, 0, 0)

# Menu offset values        
        self.offsety = -4
        self.offsety2 = -4
        self.offsetx = -4
        self.offsetx2 = 4
        
# Menu states offset values    
        self.offsetx_songselect = - 150
        self.offsetx2_songselect = 150
        
        self.offsetx_settings = - 110
        self.offsetx2_settings = 110

        self.offsetx_quit = - 130
        self.offsetx2_quit = 130      
        
# Song offset values
        self.offsetx_song1 = - 200
        self.offsetx2_song1 = 200

        self.offsetx_song2 = - 150
        self.offsetx2_song2 = 150
        
        self.offsetx_song3 = - 100
        self.offsetx2_song3 = 100

# Settings offset values
        self.offsetx_volume = -90
        self.offsetx2_volume = 90
        
        self.offsetx_controls = -110
        self.offsetx2_controls = 110
    
# Volume cursor offset values
        self.offsetx_vol = 0
        self.offsety_vol = 40
        
# Difficulty offset values
        self.offsetx_easy = - 60
        self.offsetx2_easy = 60
        
        self.offsetx_normal = - 90
        self.offsetx2_normal = 90
        
        self.offsetx_hard = - 60
        self.offsetx2_hard = 60
  
# Draw cursor
    def draw_cursor(self):
        self.game.draw_text('>', 25, self.cursor_rect.x, self.cursor_rect.y)
        self.game.draw_text('<', 25, self.cursor_rect2.x, self.cursor_rect2.y)
        self.game.draw_text('^', 25, self.cursor_rect3.x, self.cursor_rect3.y)

# Update screen
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()
        
# Main menu options
class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Song select"
        self.songselectx, self.songselecty = self.mid_w, self.mid_h + 40
        self.settingsx, self.settingsy = self.mid_w, self.mid_h + 100
        self.quitx, self.quity = self.mid_w, self.mid_h + 160
        
        self.cursor_rect.midtop = (self.songselectx + self.offsetx_songselect, self.songselecty + self.offsety)
        self.cursor_rect2.midtop = (self.songselectx + self.offsetx2_songselect, self.songselecty + self.offsety2)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            
            self.game.draw_text('Mania', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100)
            self.game.draw_text("Song select", 50, self.songselectx, self.songselecty)
            self.game.draw_text("Settings", 50, self.settingsx, self.settingsy)
            self.game.draw_text("Quit game", 50, self.quitx, self.quity)
            self.draw_cursor()
            self.blit_screen()
            pygame.display.update()
            
# Main menu move cursor
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Song select':
                self.cursor_rect.midtop = (self.settingsx + self.offsetx_settings, self.settingsy + self.offsety)
                self.cursor_rect2.midtop = (self.settingsx + self.offsetx2_settings, self.settingsy + self.offsety2)
                self.state = 'Settings'
                menu_move_sound.play()
                
            elif self.state == 'Settings':
                self.cursor_rect.midtop = (self.quitx + self.offsetx_quit, self.quity + self.offsety)
                self.cursor_rect2.midtop = (self.quitx + self.offsetx2_quit, self.quity + self.offsety2)
                self.state = 'Quit game'
                menu_move_sound.play()
                
            elif self.state == 'Quit game':
                self.cursor_rect.midtop = (self.songselectx + self.offsetx_songselect, self.songselecty + self.offsety)
                self.cursor_rect2.midtop = (self.songselectx + self.offsetx2_songselect, self.songselecty + self.offsety2)
                self.state = 'Song select'
                menu_move_sound.play()
                
        elif self.game.UP_KEY:
            if self.state == 'Song select':
                self.cursor_rect.midtop = (self.quitx + self.offsetx_quit, self.quity + self.offsety)
                self.cursor_rect2.midtop = (self.quitx + self.offsetx2_quit, self.quity + self.offsety2)
                self.state = 'Quit game'
                menu_move_sound.play()
                
            elif self.state == 'Settings':
                self.cursor_rect.midtop = (self.songselectx + self.offsetx_songselect, self.songselecty + self.offsety)
                self.cursor_rect2.midtop = (self.songselectx + self.offsetx2_songselect, self.songselecty + self.offsety2)
                self.state = 'Song select'
                menu_move_sound.play()
                
            elif self.state == 'Quit game':
                self.cursor_rect.midtop = (self.settingsx + self.offsetx_settings, self.settingsy + self.offsety)
                self.cursor_rect2.midtop = (self.settingsx + self.offsetx2_settings, self.settingsy + self.offsety2)
                self.state = 'Settings'
                menu_move_sound.play()

# Main menu state + event
    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Song select':
                self.game.curr_menu = self.game.songselect
                menu_select_sound.play()
                mixer.fadeout(500)
                the_perfect_girl_preview()
                
            elif self.state == 'Settings':
                self.game.curr_menu = self.game.settings
                menu_select_sound.play()
                
            elif self.state == 'Quit game':
                self.game.curr_menu = self.game.quit
                menu_select_sound.play() 
            self.run_display = False
                
# Song select menu
class SongMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'The Perfect Girl'
        self.song1x, self.song1y = self.mid_w, self.mid_h + 40
        self.song2x, self.song2y = self.mid_w, self.mid_h + 100
        self.song3x, self.song3y = self.mid_w, self.mid_h + 160
        
        self.cursor_rect.midtop = (self.song1x + self.offsetx_song1, self.song1y + self.offsety)
        self.cursor_rect2.midtop = (self.song1x + self.offsetx2_song1, self.song1y + self.offsety2)        

# Song select menu options
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()  
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Song select', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100)
            self.game.draw_text("The Perfect Girl", 50, self.song1x, self.song1y)
            self.game.draw_text("dreamcore//", 50, self.song2x, self.song2y)
            self.game.draw_text("Call Me", 50, self.song3x, self.song3y)
            self.draw_cursor()
            self.blit_screen()
            
# Song select menu state + event
    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
            menu_music()
            
        elif self.game.DOWN_KEY:
            if self.state == 'The Perfect Girl':
                self.state = 'dreamcore//'
                self.cursor_rect.midtop = (self.song2x + self.offsetx_song2, self.song2y + self.offsety)
                self.cursor_rect2.midtop = (self.song2x + self.offsetx2_song2, self.song2y + self.offsety2)
                menu_move_sound.play()
                mixer.fadeout(500)
                dreamcore_preview()
                
            elif self.state == 'dreamcore//':
                self.state = 'Call Me'
                self.cursor_rect.midtop = (self.song3x + self.offsetx_song3, self.song3y + self.offsety)
                self.cursor_rect2.midtop = (self.song3x + self.offsetx2_song3, self.song3y + self.offsety2)
                menu_move_sound.play()
                mixer.fadeout(500)
                call_me_preview()
            
            elif self.state == 'Call Me':
                self.state = 'The Perfect Girl'
                self.cursor_rect.midtop = (self.song1x + self.offsetx_song1, self.song1y + self.offsety)
                self.cursor_rect2.midtop = (self.song1x + self.offsetx2_song1, self.song1y + self.offsety2)
                menu_move_sound.play()
                mixer.fadeout(500)
                the_perfect_girl_preview()
                 
        elif self.game.UP_KEY:
            if self.state == 'The Perfect Girl':
                self.state = 'Call Me'
                self.cursor_rect.midtop = (self.song3x + self.offsetx_song3, self.song3y + self.offsety)
                self.cursor_rect2.midtop = (self.song3x + self.offsetx2_song3, self.song3y + self.offsety)
                menu_move_sound.play()
                mixer.fadeout(500)
                call_me_preview()
                
            elif self.state == 'Call Me':
                self.state = 'dreamcore//'
                self.cursor_rect.midtop = (self.song2x + self.offsetx_song2, self.song2y + self.offsety)
                self.cursor_rect2.midtop = (self.song2x + self.offsetx2_song2, self.song2y + self.offsety2)
                menu_move_sound.play()
                mixer.fadeout(500)
                dreamcore_preview()
            
            elif self.state == 'dreamcore//':
                self.state = 'The Perfect Girl'
                self.cursor_rect.midtop = (self.song1x + self.offsetx_song1, self.song1y + self.offsety)
                self.cursor_rect2.midtop = (self.song1x + self.offsetx2_song1, self.song1y + self.offsety2)
                menu_move_sound.play()
                mixer.fadeout(500)
                the_perfect_girl_preview()
                           
        elif self.game.START_KEY:
            if self.state == 'The Perfect Girl':
                self.game.curr_menu = self.game.difficulty
                menu_select_sound.play()
                
            elif self.state == 'dreamcore//':
                self.game.curr_menu = self.game.difficulty
                menu_select_sound.play() 
            
            elif self.state == 'Call Me':
                self.game.curr_menu = self.game.difficulty
                menu_select_sound.play() 
            self.run_display = False

# Difficulty menu
class DifficultyMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Easy'
        
        self.easyx, self.easyy = self.mid_w, self.mid_h + 40
        self.normalx, self.normaly = self.mid_w, self.mid_h + 100
        self.hardx, self.hardy = self.mid_w, self.mid_h + 160
        
        self.cursor_rect.midtop = (self.easyx + self.offsetx_easy, self.easyy + self.offsety)
        self.cursor_rect2.midtop = (self.easyx + self.offsetx2_easy, self.easyy + self.offsety2)        

# Difficulty menu options
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()  
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Difficulty', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100)
            self.game.draw_text("Easy", 50, self.easyx, self.easyy)
            self.game.draw_text("Normal", 50, self.normalx, self.normaly)
            self.game.draw_text("Hard", 50, self.hardx, self.hardy)
            
            self.draw_cursor()
            self.blit_screen()
            
# Difficulty menu state + event
    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.songselect
            self.run_display = False
            
            
        elif self.game.DOWN_KEY:
            if self.state == 'Easy':
                self.state = 'Normal'
                self.cursor_rect.midtop = (self.normalx + self.offsetx_normal, self.normaly + self.offsety)
                self.cursor_rect2.midtop = (self.normalx + self.offsetx2_normal, self.normaly + self.offsety2)
                menu_move_sound.play()
                
            elif self.state == 'Normal':
                self.state = 'Hard'
                self.cursor_rect.midtop = (self.hardx + self.offsetx_hard, self.hardy + self.offsety)
                self.cursor_rect2.midtop = (self.hardx + self.offsetx2_hard, self.hardy + self.offsety2)
                menu_move_sound.play()
            
            elif self.state == 'Hard':
                self.state = 'Easy'
                self.cursor_rect.midtop = (self.easyx + self.offsetx_easy, self.easyy + self.offsety)
                self.cursor_rect2.midtop = (self.easyx + self.offsetx2_easy, self.easyy + self.offsety2)
                menu_move_sound.play()
                 
        elif self.game.UP_KEY:
            if self.state == 'Easy':
                self.state = 'Hard'
                self.cursor_rect.midtop = (self.hardx + self.offsetx_hard, self.hardy + self.offsety)
                self.cursor_rect2.midtop = (self.hardx + self.offsetx2_hard, self.hardy + self.offsety)
                menu_move_sound.play()
                
            elif self.state == 'Hard':
                self.state = 'Normal'
                self.cursor_rect.midtop = (self.normalx + self.offsetx_normal, self.normaly + self.offsety)
                self.cursor_rect2.midtop = (self.normalx + self.offsetx2_normal, self.normaly + self.offsety2)
                menu_move_sound.play()
            
            elif self.state == 'Normal':
                self.state = 'Easy'
                self.cursor_rect.midtop = (self.easyx + self.offsetx_easy, self.easyy + self.offsety)
                self.cursor_rect2.midtop = (self.easyx + self.offsetx2_easy, self.easyy + self.offsety2)
                menu_move_sound.play()
                                               
        elif self.game.START_KEY:
            if self.state == 'Easy':
                self.game.curr_menu = self.game.mania_stage
                menu_select_sound.play()
                
            elif self.state == 'Normal':
                self.game.playing = True
                menu_select_sound.play() 
            
            elif self.state == 'Hard':
                self.game.playing = True
                menu_select_sound.play() 
            self.run_display = False
            
# Settings menu           
class SettingsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        
        self.volumex, self.volumey = self.mid_w, self.mid_h + 40
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 100
        
        self.cursor_rect.midtop = (self.volumex + self.offsetx_volume, self.volumey + self.offsety)
        self.cursor_rect2.midtop = (self.volumex + self.offsetx2_volume, self.volumey + self.offsety2)        

# Settings menu options
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()  
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Settings', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100)
            self.game.draw_text("Volume", 50, self.volumex, self.volumey)
            
            self.draw_cursor()
            self.blit_screen()
            
# Settings menu state + event
    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
                                             
        elif self.game.START_KEY:
            if self.state == 'Volume':
                self.game.curr_menu = self.game.volume
                self.run_display = False
                menu_select_sound.play()
                
# Volume menu
class VolumeMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = '5'
        
        self.vol1x, self.vol1y = self.mid_w -270, self.mid_h
        self.vol2x, self.vol2y = self.mid_w -210, self.mid_h
        self.vol3x, self.vol3y = self.mid_w -150, self.mid_h     
        self.vol4x, self.vol4y = self.mid_w -90, self.mid_h
        self.vol5x, self.vol5y = self.mid_w -30, self.mid_h
        self.vol6x, self.vol6y = self.mid_w +30, self.mid_h
        self.vol7x, self.vol7y = self.mid_w +90, self.mid_h
        self.vol8x, self.vol8y = self.mid_w +150, self.mid_h
        self.vol9x, self.vol9y = self.mid_w +210, self.mid_h
        self.vol10x, self.vol10y = self.mid_w +270, self.mid_h
        
        self.cursor_rect3.midtop = (self.vol5x + self.offsetx_vol, self.vol5y + self.offsety_vol) 

# Volume menu options
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()  
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Volume', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100)
            self.game.draw_text("1", 50, self.vol1x, self.vol1y)
            self.game.draw_text("2", 50, self.vol2x, self.vol2y)
            self.game.draw_text("3", 50, self.vol3x, self.vol3y)
            self.game.draw_text("4", 50, self.vol4x, self.vol4y)
            self.game.draw_text("5", 50, self.vol5x, self.vol5y)
            self.game.draw_text("6", 50, self.vol6x, self.vol6y)
            self.game.draw_text("7", 50, self.vol7x, self.vol7y)
            self.game.draw_text("8", 50, self.vol8x, self.vol8y)
            self.game.draw_text("9", 50, self.vol9x, self.vol9y)
            self.game.draw_text("10", 50, self.vol10x, self.vol10y)
            
            self.draw_cursor()
            self.blit_screen()
            
# Volume menu state + event
    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.settings
            self.run_display = False
            
        elif self.game.RIGHT_KEY:
            if self.state == '1':
                self.state = '2'
                self.cursor_rect3.midtop = (self.vol2x + self.offsetx_vol, self.vol2y + self.offsety_vol)
                menu_move_sound.play()
                pygame.mixer.music.set_volume(0.2)
                
            elif self.state == '2':
                self.state = '3'
                self.cursor_rect3.midtop = (self.vol3x + self.offsetx_vol, self.vol3y + self.offsety_vol)
                menu_move_sound.play()
                pygame.mixer.music.set_volume(0.3)
            
            elif self.state == '3':
                self.state = '4'
                self.cursor_rect3.midtop = (self.vol4x + self.offsetx_vol, self.vol4y + self.offsety_vol)
                menu_move_sound.play()
                pygame.mixer.music.set_volume(0.4)
                
            elif self.state == '4':
                self.state = '5'
                self.cursor_rect3.midtop = (self.vol5x + self.offsetx_vol, self.vol5y + self.offsety_vol)
                menu_move_sound.play()
                pygame.mixer.music.set_volume(0.5)
            
            elif self.state == '5':
                self.state = '6'
                self.cursor_rect3.midtop = (self.vol6x + self.offsetx_vol, self.vol6y + self.offsety_vol)
                menu_move_sound.play()
                pygame.mixer.music.set_volume(0.6)
                
            elif self.state == '6':
                self.state = '7'
                self.cursor_rect3.midtop = (self.vol7x + self.offsetx_vol, self.vol7y + self.offsety_vol)
                menu_move_sound.play()
                pygame.mixer.music.set_volume(0.7)
            
            elif self.state == '7':
                self.state = '8'
                self.cursor_rect3.midtop = (self.vol8x + self.offsetx_vol, self.vol8y + self.offsety_vol)
                menu_move_sound.play()
                pygame.mixer.music.set_volume(0.8)
                
            elif self.state == '8':
                self.state = '9'
                self.cursor_rect3.midtop = (self.vol9x + self.offsetx_vol, self.vol9y + self.offsety_vol)
                menu_move_sound.play()
                pygame.mixer.music.set_volume(0.9)
                
            elif self.state == '9':
                self.state = '10'
                self.cursor_rect3.midtop = (self.vol10x + self.offsetx_vol, self.vol10y + self.offsety_vol)
                menu_move_sound.play()
                pygame.mixer.music.set_volume(1)
                                                                  
        elif self.game.LEFT_KEY:
            if self.state == '10':
                self.state = '9'
                self.cursor_rect3.midtop = (self.vol9x + self.offsetx_vol, self.vol9y + self.offsety_vol)
                menu_move_sound.play()
                pygame.mixer.music.set_volume(0.9)
                
            elif self.state == '9':
                self.state = '8'
                self.cursor_rect3.midtop = (self.vol8x + self.offsetx_vol, self.vol8y + self.offsety_vol)
                menu_move_sound.play()
                pygame.mixer.music.set_volume(0.8)
            
            elif self.state == '8':
                self.state = '7'
                self.cursor_rect3.midtop = (self.vol7x + self.offsetx_vol, self.vol7y + self.offsety_vol)
                menu_move_sound.play()
                pygame.mixer.music.set_volume(0.7)
                
            elif self.state == '7':
                self.state = '6'
                self.cursor_rect3.midtop = (self.vol6x + self.offsetx_vol, self.vol6y + self.offsety_vol)
                menu_move_sound.play()
                pygame.mixer.music.set_volume(0.6)
            
            elif self.state == '6':
                self.state = '5'
                self.cursor_rect3.midtop = (self.vol5x + self.offsetx_vol, self.vol5y + self.offsety_vol)
                menu_move_sound.play()
                pygame.mixer.music.set_volume(0.5)
                
            elif self.state == '5':
                self.state = '4'
                self.cursor_rect3.midtop = (self.vol4x + self.offsetx_vol, self.vol4y + self.offsety_vol)
                menu_move_sound.play()
                pygame.mixer.music.set_volume(0.4)
            
            elif self.state == '4':
                self.state = '3'
                self.cursor_rect3.midtop = (self.vol3x + self.offsetx_vol, self.vol3y + self.offsety_vol)
                menu_move_sound.play()
                pygame.mixer.music.set_volume(0.3)
                
            elif self.state == '3':
                self.state = '2'
                self.cursor_rect3.midtop = (self.vol2x + self.offsetx_vol, self.vol2y + self.offsety_vol)
                menu_move_sound.play()
                pygame.mixer.music.set_volume(0.2)
                
            elif self.state == '2':
                self.state = '1'
                self.cursor_rect3.midtop = (self.vol1x + self.offsetx_vol, self.vol1y + self.offsety_vol)
                menu_move_sound.play()
                pygame.mixer.music.set_volume(0.1)
            self.run_display = False

# Quit menu
class QuitMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        
# Quit menu actions
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('See you next time', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2)
            self.blit_screen()
            mixer.music.fadeout(2000)
            sleep(2.5)
            pygame.quit()