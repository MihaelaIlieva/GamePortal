import pygame
import sys
import loginpage
import registerpage
import database.basicqueries as basicqueries
import tkinter
import statisticspage
from tkinter import *
import subprocess
import getrich

pygame.init()

WIDTH, HEIGHT = 1720, 980
FPS = 60
username = ""
password = ""

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BUTTON_COLOR = (255, 204, 235)
HOVER_COLOR = (254, 103, 194)

font = pygame.font.Font(None, 36)
subfont = pygame.font.Font(None, 24)

class Button:

    def __init__(self, text, subtext, x, y, width, height, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.subtext = subtext

    def draw(self, screen, hover):
        color = HOVER_COLOR if hover else BUTTON_COLOR
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        self.draw_text(screen, self.text, self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2)
        self.draw_subtext(screen,self.subtext, self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2)
    
    def draw_text(self, screen, text, x, y):
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

    def draw_subtext(self, screen, subtext, x, y):
        text_surface = subfont.render(subtext, True, WHITE)
        text_rect = text_surface.get_rect(center=(x, y - 35))
        screen.blit(text_surface, text_rect)


class ProfilePage:

    def __init__(self, username, password):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Game Portal - Profile Page")

        self.background = pygame.image.load("images/mainpagebackground.jpg")
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        self.get_rich_button = Button("Get rich","", WIDTH // 2 - 100, HEIGHT // 2 - 30, 150, 40)
        self.tictactoe_button = Button("TicTacToe","", WIDTH // 2 - 100, HEIGHT // 2 + 35, 150, 40)
        self.statistics_button = Button("Statistics","", WIDTH // 2 - 100, HEIGHT // 2 + 95, 150, 40)

        self.username = username
        self.password = password
        username = username
        password = password

        self.text = "Welcome {username}! What will it be today?".format(username=self.username)
        self.subtext = ""

        
        self.main_loop()

    def main_loop(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            hover_get_rich = self.get_rich_button.rect.collidepoint(pygame.mouse.get_pos())
            hover_tictactoe = self.tictactoe_button.rect.collidepoint(pygame.mouse.get_pos())
            hover_statistics = self.statistics_button.rect.collidepoint(pygame.mouse.get_pos())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if hover_get_rich:
                        running = False
                        self.open_get_rich_page()
                    elif hover_tictactoe:
                        running = False
                        self.open_tictactoe_page()
                    elif hover_statistics:
                        running = False
                        self.open_statistics_page()

            if running == False:
                break

            self.screen.blit(self.background, (0, 0))

            self.draw_text(self.text, WIDTH // 2, HEIGHT // 4)
            self.draw_subtext(self.subtext, WIDTH // 2, HEIGHT // 4 + 35)

            self.get_rich_button.draw(self.screen, hover_get_rich)
            self.tictactoe_button.draw(self.screen, hover_tictactoe)
            self.statistics_button.draw(self.screen, hover_statistics)

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()
        sys.exit()

    def draw_text(self, text, x, y):
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def draw_subtext(self, text, x, y):
        text_surface = subfont.render(text, True, WHITE)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def open_get_rich_page(self):
        #TODO: redirect to get rich game
        pygame.quit()
        getrich.GetRichGame(self.username, self.password)

    def open_tictactoe_page(self):
        #TODO: redirect to tictactoe
        pygame.quit()
        import tictactoepage
        # subprocess.Popen(["python", "tictactoepage.py"])
        # pygame.quit()

    def open_statistics_page(self):
        pygame.quit()
        root = Tk()
        statisticspage.StatisticsDisplay(root, self.username)
        root.mainloop()
        pass
