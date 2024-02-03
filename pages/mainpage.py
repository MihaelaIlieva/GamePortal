import pygame
import sys
import loginpage
import registerpage
import database.basicqueries as basicqueries

pygame.init()

WIDTH, HEIGHT = 1720, 980
FPS = 60

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


class MainPage:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Game Portal - Main Page")

        self.background = pygame.image.load("images/mainpagebackground.jpg")
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        self.login_button = Button("Login","Already have an account?", WIDTH // 2 - 100, HEIGHT // 2 - 30, 150, 40, self.open_login_page)
        self.register_button = Button("Register","New to the game portal?", WIDTH // 2 - 100, HEIGHT // 2 + 65, 150, 40, self.open_register_page)

        self.text = "Welcome to Mihaela's Game Portal"
        self.subtext = "A place where you can train your brain"
        self.main_loop()

    def main_loop(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            hover_login = self.login_button.rect.collidepoint(pygame.mouse.get_pos())
            hover_register = self.register_button.rect.collidepoint(pygame.mouse.get_pos())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if hover_login:
                        self.open_login_page()
                    elif hover_register:
                        self.open_register_page()

            self.screen.blit(self.background, (0, 0))

            self.draw_text(self.text, WIDTH // 2, HEIGHT // 4)
            self.draw_subtext(self.subtext, WIDTH // 2, HEIGHT // 4 + 35)

            self.login_button.draw(self.screen, hover_login)
            self.register_button.draw(self.screen, hover_register)

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

    def open_login_page(self):
        loginpage.LoginPage()

    def open_register_page(self):
        registerpage.RegisterPage()

if __name__ == "__main__":
    main_page = MainPage()