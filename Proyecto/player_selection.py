import pygame
from menu import *
from player import Player
class PlayerSelection():
    number_of_players= [1, 2]
    players = []
    
    def __init__(self,game):
        self.game=game
        self.display = self.game.display
        self.window = self.game.window
        self.run_display = True
        self.mid_w, self.mid_h = self.game.DISPLAY_W , self.game.DISPLAY_H - 200
        #self.number_of_players= [1, 2]  
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()
        
class Selection(PlayerSelection):
    def __init__(self, game):
        PlayerSelection.__init__(self, game)
        self.state = "2"
        self.number2x, self.number2y = self.game.DISPLAY_W/2 - 200, self.game.DISPLAY_H / 2,
        self.number3x, self.number3y = self.game.DISPLAY_W/2 - 50, self.game.DISPLAY_H / 2,
        self.number4x, self.number4y = self.game.DISPLAY_W/2 + 100, self.game.DISPLAY_H / 2,
        

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            
            self.game.render("Select", 0, 0)
            #movement= pygame.mouse.get_pos()
            #print(movement)
            self.game.draw_text('Numero de jugadores : ', 45, self.game.DISPLAY_W / 2 + 20, self.game.DISPLAY_H / 3, self.game.BLACK)
            self.game.draw_button('2',40, self.number2x, self.number2y, 100,100, self.game.BLACK, self.game.ORANGE)
            self.boton1 = pygame.Rect(self.number2x,self.number2y, 100, 100)
            self.game.draw_button('3',40, self.number3x, self.number3y, 100,100, self.game.BLACK, self.game.ORANGE)
            self.boton2 = pygame.Rect(self.number3x,self.number3y, 100, 100)
            self.game.draw_button('4',40, self.number4x, self.number4y, 100,100, self.game.BLACK, self.game.ORANGE)
            self.boton3 = pygame.Rect(self.number4x,self.number4y, 100, 100)
            self.game.window.blit(self.game.display, (0, 0))
            pygame.display.update()
            self.check_input()
            self.game.reset_keys()
    #Ubicar el puntero 
    #def move_cursor(self):
    #Para saber que hace click en el boton y se active
    def check_input (self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                #depende el numero los mando a elegir el monstruo
                if self.boton1.collidepoint(mouse_pos):
                    print("HOLAA") 
                    print(self.number_of_players)
                    self.game.curr_menu = self.game.create_players
                if self.boton2.collidepoint(mouse_pos):
                    print("boton 2")
                    self.number_of_players.append(3)
                    self.run_display = False
                    self.game.curr_menu = self.game.create_player
                    self.game.curr_menu.display_menu()        
                if self.boton3.collidepoint(mouse_pos):
                    print("boton 3")
                    self.number_of_players.append(3)
                    self.number_of_players.append(4)
                    print(self.number_of_players)
            if event.type == pygame.QUIT:
                self.game.running, self.game.playing = False, False
                self.game.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.running, self.game.playing = False, False
                    self.game.curr_menu.run_display = False
                if event.key == pygame.K_BACKSPACE:
                    self.game.curr_menu = self.game.main_menu
                    self.game.curr_menu.display_menu()
                    self.game.playing=False
                    self.game.reset_keys()
                    self.run_display = False
                    self.reset_players()
    def reset_players(self):
        self.number_of_players = 0
class CreatePlayers(PlayerSelection):
    def __init__(self, game):
        PlayerSelection.__init__(self, game)
        
    def display_menu(self):
            self.run_display = True
            while self.run_display:
                self.game.reset_keys()
                self.game.render("Select", 0, 0)
                self.game.draw_text('Numero de jugadores : ', 45, self.game.DISPLAY_W / 2 + 20, self.game.DISPLAY_H / 3, self.game.BLACK)
                for x in self.number_of_players:
                    print(self.number_of_players)
                    name = print(f"Nombre del jugador {x}: ")
                    name =input()
                    monster =  print(f"Nombre del Monstruo {x}:")
                    monster =input()
                    player= Player(x,name,self.number_of_players[x-1], monster)
                    self.players.append(player) 
                print("Su nombre es : ",self.players[1].name)   
                return self.players
            
                           
    def check_input(self):
        self.game.check_events()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.select_character
            self.run_display = False
                   
                    

  
        

               
   
