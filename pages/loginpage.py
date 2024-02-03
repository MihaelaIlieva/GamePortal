import pygame
import sys
# from ..database import basicqueries
import database.basicqueries as basicqueries
import mainpage

pygame.init()

WIDTH, HEIGHT = 1720, 980
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHTGRAY = (235, 235, 235)
BUTTON_COLOR = (255, 204, 235)
HOVER_COLOR = (254, 103, 194)
BORDER_COLOR = (55, 55, 55)

font = pygame.font.Font(None, 36)

class InputBox:

    def __init__(self, x, y, width, height, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = GRAY
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = LIGHTGRAY if not self.active else GRAY
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                print(self.text)
                #TODO think if should do something when pressed enter
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.txt_surface = font.render(self.text, True, BLACK)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, BORDER_COLOR, self.rect, 3)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

    def get_text(self):
        return self.text


class LoginPage:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Game Portal - Login Page")

        self.background = pygame.image.load("images/mainpagebackground.jpg")
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        self.username_input = InputBox(WIDTH//2 - 100, HEIGHT//2 - 65, 200, 40, '')
        self.password_input = InputBox(WIDTH//2 - 100, HEIGHT//2, 200, 40, '')
        self.login_button = Button("Login", WIDTH // 2 - 75, HEIGHT // 2 + 55, 150, 40, self.login)
        self.text = "Please put in your credentials"
        self.error_message = None
        self.main_loop()

    def main_loop(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.username_input.handle_event(event)
                self.password_input.handle_event(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.login_button.rect.collidepoint(event.pos):
                        #TODO write the method
                        self.login()

            self.username_input.update()
            self.password_input.update()

            self.screen.blit(self.background, (0, 0))

            self.draw_text(self.text, WIDTH // 2, HEIGHT // 4)
            self.draw_text("Username", WIDTH//2, HEIGHT//2 -85)
            self.draw_text("Password", WIDTH//2, HEIGHT//2 - 15)

            self.username_input.draw(self.screen)
            self.password_input.draw(self.screen)

            hover_login = self.login_button.rect.collidepoint(pygame.mouse.get_pos())
            self.login_button.draw(self.screen, hover_login)

            if self.error_message:
                self.draw_text(self.error_message, WIDTH // 2, HEIGHT // 2 + 105)

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()
        sys.exit()

    def login(self):
        username = self.username_input.get_text()
        password = self.password_input.get_text()

        # if there's no such username in the database
        if len(basicqueries.check_for_same_username(username)) == 0:
            self.error_message = "No such user!"
            print("No such user!")
        else:
            user_id = basicqueries.check_for_same_username(username)[0][0]
            result = basicqueries.get_user_credentials(user_id)
            # if both username and password match
            if result[0] == (username, password):
                self.error_message = "Successfull login!"
                self.update_screen()
                pygame.time.delay(1000)
                #TODO add real refernce here
                mainpage.MainPage()
                print("Successfull login!")
            else:
                self.error_message = "Wrong password!"
                print("Wrong password!")

    def draw_text(self, text, x, y):
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    # for when the error message changes
    def update_screen(self):
        self.screen.blit(self.background, (0, 0))

        self.draw_text(self.text, WIDTH // 2, HEIGHT // 4)
        self.draw_text("Username", WIDTH//2, HEIGHT//2 - 85)
        self.draw_text("Password", WIDTH//2, HEIGHT//2 - 15)

        self.username_input.draw(self.screen)
        self.password_input.draw(self.screen)

        hover_login = self.login_button.rect.collidepoint(pygame.mouse.get_pos())
        self.login_button.draw(self.screen, hover_login)

        if self.error_message:
            self.draw_text(self.error_message, WIDTH // 2, HEIGHT // 2 + 105)

        pygame.display.flip()

class Button:

    def __init__(self, text, x, y, width, height, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action

    def draw(self, screen, hover):
        color = HOVER_COLOR if hover else BUTTON_COLOR
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        self.draw_text(screen, self.text, self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2)

    def draw_text(self, screen, text, x, y):
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

if __name__ == "__main__":
    login_page = LoginPage()
