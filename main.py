import pygame
import time
import random

# Initialize the pygame.
pygame.init()

# Create the screen.
W = 800
H = 600
SCREEN = pygame.display.set_mode((W, H))

BACKGROUND = pygame.image.load("background.png")

# lists of images for northern lights movement
PINK1 = [
    pygame.image.load("Pink11.png"),
    pygame.image.load("Pink11.png"),
    pygame.image.load("Pink11.png"),
    pygame.image.load("Pink11.png"),
    pygame.image.load("Pink12.png"),
    pygame.image.load("Pink12.png"),
    pygame.image.load("Pink12.png"),
    pygame.image.load("Pink12.png"),
    pygame.image.load("Pink13.png"),
    pygame.image.load("Pink13.png"),
    pygame.image.load("Pink13.png"),
    pygame.image.load("Pink13.png"),
    pygame.image.load("Pink14.png"),
    pygame.image.load("Pink14.png"),
    pygame.image.load("Pink14.png"),
    pygame.image.load("Pink14.png"),
    pygame.image.load("Pink15.png"),
    pygame.image.load("Pink15.png"),
    pygame.image.load("Pink15.png"),
    pygame.image.load("Pink15.png"),
    pygame.image.load("Pink16.png"),
    pygame.image.load("Pink16.png"),
    pygame.image.load("Pink16.png"),
    pygame.image.load("Pink16.png"),
]

GREEN1 = [
    pygame.image.load("Green11.png"),
    pygame.image.load("Green11.png"),
    pygame.image.load("Green11.png"),
    pygame.image.load("Green11.png"),
    pygame.image.load("Green12.png"),
    pygame.image.load("Green12.png"),
    pygame.image.load("Green12.png"),
    pygame.image.load("Green12.png"),
    pygame.image.load("Green13.png"),
    pygame.image.load("Green13.png"),
    pygame.image.load("Green13.png"),
    pygame.image.load("Green13.png"),
    pygame.image.load("Green14.png"),
    pygame.image.load("Green14.png"),
    pygame.image.load("Green14.png"),
    pygame.image.load("Green14.png"),
    pygame.image.load("Green15.png"),
    pygame.image.load("Green15.png"),
    pygame.image.load("Green15.png"),
    pygame.image.load("Green15.png"),
    pygame.image.load("Green16.png"),
    pygame.image.load("Green16.png"),
    pygame.image.load("Green16.png"),
    pygame.image.load("Green16.png"),
]

PINK2 = [
    pygame.image.load("Pink21.png"),
    pygame.image.load("Pink21.png"),
    pygame.image.load("Pink21.png"),
    pygame.image.load("Pink21.png"),
    pygame.image.load("Pink22.png"),
    pygame.image.load("Pink22.png"),
    pygame.image.load("Pink22.png"),
    pygame.image.load("Pink22.png"),
    pygame.image.load("Pink23.png"),
    pygame.image.load("Pink23.png"),
    pygame.image.load("Pink23.png"),
    pygame.image.load("Pink23.png"),
    pygame.image.load("Pink24.png"),
    pygame.image.load("Pink24.png"),
    pygame.image.load("Pink24.png"),
    pygame.image.load("Pink24.png"),
    pygame.image.load("Pink25.png"),
    pygame.image.load("Pink25.png"),
    pygame.image.load("Pink25.png"),
    pygame.image.load("Pink25.png"),
    pygame.image.load("Pink26.png"),
    pygame.image.load("Pink26.png"),
    pygame.image.load("Pink26.png"),
    pygame.image.load("Pink26.png"),
]

GREEN2 = [
    pygame.image.load("Green21.png"),
    pygame.image.load("Green21.png"),
    pygame.image.load("Green21.png"),
    pygame.image.load("Green21.png"),
    pygame.image.load("Green22.png"),
    pygame.image.load("Green22.png"),
    pygame.image.load("Green22.png"),
    pygame.image.load("Green22.png"),
    pygame.image.load("Green23.png"),
    pygame.image.load("Green23.png"),
    pygame.image.load("Green23.png"),
    pygame.image.load("Green23.png"),
    pygame.image.load("Green24.png"),
    pygame.image.load("Green24.png"),
    pygame.image.load("Green24.png"),
    pygame.image.load("Green24.png"),
    pygame.image.load("Green25.png"),
    pygame.image.load("Green25.png"),
    pygame.image.load("Green25.png"),
    pygame.image.load("Green25.png"),
    pygame.image.load("Green26.png"),
    pygame.image.load("Green26.png"),
    pygame.image.load("Green26.png"),
    pygame.image.load("Green26.png"),
]

# lists of images for player movement
FRONT = pygame.image.load("front.png")
LEFT = [
    pygame.image.load("left1.png"),
    pygame.image.load("left2.png"),
    pygame.image.load("left3.png"),
    pygame.image.load("left4.png"),
    pygame.image.load("left5.png"),
    pygame.image.load("left6.png"),
    pygame.image.load("left7.png"),
]
RIGHT = [
    pygame.image.load("right1.png"),
    pygame.image.load("right2.png"),
    pygame.image.load("right3.png"),
    pygame.image.load("right4.png"),
    pygame.image.load("right5.png"),
    pygame.image.load("right6.png"),
    pygame.image.load("right7.png"),
]

GEYSER = pygame.image.load("geyser_water.png")
LAVA = pygame.image.load("geyser_lava.png")

health_font = pygame.font.Font('freesansbold.ttf', 16)
you_won_font = pygame.font.Font('freesansbold.ttf', 64)
game_over_font = pygame.font.Font('freesansbold.ttf', 64)


class Light:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.bling = False
        self.pink1 = False
        self.green1 = False
        self.pink2 = False
        self.green2 = False
        self.light_count = 3

    def draw(self):
        if self.bling:
            if self.pink1:
                self.image = PINK1
                SCREEN.blit(PINK1[(self.light_count // 3) - 1], (self.x, self.y))
            elif self.green1:
                self.image = GREEN1
                SCREEN.blit(GREEN1[(self.light_count // 3) - 1], (self.x, self.y))
            elif self.pink2:
                self.image = PINK2
                SCREEN.blit(PINK2[(self.light_count // 3) - 1], (self.x, self.y))
            elif self.green2:
                self.image = GREEN2
                SCREEN.blit(GREEN2[(self.light_count // 3) - 1], (self.x, self.y))


class Player:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.y_change = -5
        self.x_change = 5
        self.jumping = False
        self.jump_count = 7
        self.health = 100
        self.mask = pygame.mask.from_surface(self.image)
        self.left = False
        self.right = False
        self.steps = 0

    def draw(self):
        if self.left:
            self.image = LEFT
            SCREEN.blit(LEFT[(self.steps // 3)-1], (self.x, self.y))
        elif self.right:
            self.image = RIGHT
            SCREEN.blit(RIGHT[(self.steps // 3)-1], (self.x, self.y))
        else:
            self.image = FRONT
            SCREEN.blit(FRONT, (self.x, self.y))

    def health_score(self):
        health_text = health_font.render("health: " + str(self.health), True, (255, 255, 255))
        SCREEN.blit(health_text, (W - 100, H - 550))


class Geyser:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.y_change = 0
        self.erupting = False
        self.medium = False
        self.small = False
        self.erupt_count_medium = 20
        self.erupt_count_small = 15
        self.lava = False
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self):
        if self.lava:
            self.image = LAVA
            SCREEN.blit(self.image, (self.x, self.y))
        else:
            self.image = GEYSER
            SCREEN.blit(self.image, (self.x, self.y))


# Function to check collision between two objects.
def collision(item1, item2):
    offset_x = int(item2.x - item1.x)
    offset_y = int(item2.y - item1.y)
    return item1.mask.overlap(item2.mask, (offset_x, offset_y)) is not None


# Function to run main game loop
def run_game():
    run = True
    # fps = frames per second
    fps = 60

    # create clock
    clock = pygame.time.Clock()

    you_won = False
    you_won_text = you_won_font.render("You won!!", True, (255, 255, 255))
    game_over = False
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    countdown = 0

    # create instances of classes
    player = Player(FRONT, 384, 568)

    light1 = Light(GREEN1, 70, 60)
    light2 = Light(GREEN1, 500, 150)
    light3 = Light(GREEN1, 170, 160)
    light4 = Light(GREEN1, 380, 40)
    light5 = Light(GREEN1, 620, 170)
    lights = [light1, light2, light3, light4, light5]

    geyser1 = Geyser(GEYSER, int(W / 8 - 20), 600)
    geyser2 = Geyser(GEYSER, int(W / 8 * 2 - 20), 600)
    geyser3 = Geyser(GEYSER, int(W / 8 * 3 - 20), 600)
    geyser4 = Geyser(GEYSER, int(W / 8 * 4 - 20), 600)
    geyser5 = Geyser(GEYSER, int(W / 8 * 5 - 20), 600)
    geyser6 = Geyser(GEYSER, int(W / 8 * 6 - 20), 600)
    geyser7 = Geyser(GEYSER, int(W / 8 * 7 - 20), 600)
    geysers = [geyser1,
               geyser2,
               geyser3,
               geyser4,
               geyser5,
               geyser6,
               geyser7]

    def redraw_window():
        SCREEN.blit(BACKGROUND, (0, 0))
        for geyser in geysers:
            geyser.draw()
        for light in lights:
            light.draw()
        player.draw()
        player.health_score()
        if you_won:
            SCREEN.blit(you_won_text,
                        (int(W / 2 - you_won_text.get_width() / 2), int(H / 2 - you_won_text.get_height() / 2)))
        if game_over:
            SCREEN.blit(game_over_text,
                        (int(W / 2 - game_over_text.get_width() / 2), int(H / 2 - game_over_text.get_height() / 2)))
        pygame.display.update()

    while run:
        clock.tick(fps)
        redraw_window()
        # show Game Over or You Won text for 3 seconds then return to menu
        if game_over or you_won:
            countdown += 1
            if countdown > fps * 3:
                run = False
            else:
                continue

        # End game if user clicks cross.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        # let the northern lights turn on at random intervals
        for light in lights:
            if not light.bling:
                if random.randrange(0, 1500) == 100:
                    light.bling = True
                    light.pink1 = True
                    light.pink2 = False
                    light.green1 = False
                    light.green2 = False
                if random.randrange(0, 300) == 101:
                    light.bling = True
                    light.pink1 = False
                    light.pink2 = False
                    light.green1 = True
                    light.green2 = False
                if random.randrange(0, 1500) == 102:
                    light.bling = True
                    light.pink1 = False
                    light.pink2 = True
                    light.green1 = False
                    light.green2 = False
                if random.randrange(0, 300) == 103:
                    light.bling = True
                    light.pink1 = False
                    light.pink2 = False
                    light.green1 = False
                    light.green2 = True
            if light.bling:
                if light.light_count > 73:
                    light.light_count = 3
                    light.bling = False
                else:
                    light.light_count += 1

        # Make geysers erupt at random intervals
        for geyser in geysers:
            if not geyser.erupting:
                if 1 < random.randrange(0, 300) < 6:
                    geyser.erupting = True
                    geyser.medium = True
                    geyser.small = False
                    geyser.lava = False
                elif random.randrange(0, 300) == 6:
                    geyser.erupting = True
                    geyser.medium = True
                    geyser.small = False
                    geyser.lava = True
                elif 6 < random.randrange(0, 300) < 11:
                    geyser.erupting = True
                    geyser.medium = False
                    geyser.small = True
                    geyser.lava = False
                elif random.randrange(0, 300) == 11:
                    geyser.erupting = True
                    geyser.medium = False
                    geyser.small = True
                    geyser.lava = True

        # Geyser movement
        for geyser in geysers:
            if geyser.erupting:
                if geyser.medium:
                    if geyser.erupt_count_medium >= -20:
                        if geyser.erupt_count_medium < 0:
                            num = -1
                        else:
                            num = 1
                        geyser.y_change = (geyser.erupt_count_medium ** 2) * 0.05 * num
                        geyser.y -= geyser.y_change
                        geyser.erupt_count_medium -= 0.5
                    else:
                        geyser.erupting = False
                        geyser.lava = False
                        geyser.medium = False
                        geyser.erupt_count_medium = 20
                elif geyser.small:
                    if geyser.erupt_count_small >= -15:
                        if geyser.erupt_count_small < 0:
                            num = -1
                        else:
                            num = 1
                        geyser.y_change = (geyser.erupt_count_small ** 2) * 0.05 * num
                        geyser.y -= geyser.y_change
                        geyser.erupt_count_small -= 0.5
                    else:
                        geyser.erupting = False
                        geyser.lava = False
                        geyser.small = False
                        geyser.erupt_count_small = 15

        # check for collision player with lava
        for geyser in geysers:
            if collision(player, geyser):
                if geyser.lava:
                    player.health -= 1
                    if player.health < 0:
                        game_over = True

        # check for collision player with northern lights
        for light in lights:
            if light.bling:
                if light.x < player.x < light.x + 120:
                    if light.y < player.y < light.y + 60:
                        if light.green1 or light.green2:
                            player.health += 1
                        elif light.pink1 or light.pink2:
                            you_won = True

        # Player movement
        player.y -= player.y_change  # default value -5, because of gravity.
        # Define boundaries in which player can move
        if player.y - player.y_change <= 0:
            player.y = 0
        if player.y - player.y_change >= 568:
            player.y = 568

        # When player goes to top of geyser, she moves up with it.
        for geyser in geysers:
            if geyser.erupting:
                if geyser.x - 10 <= player.x <= geyser.x + 18:
                    if geyser.y - 35 <= player.y <= geyser.y + 35:
                        player.y = geyser.y - 32
                        player.y -= geyser.y_change

        # Player moves left
        if keys[pygame.K_LEFT] and player.x - player.x_change > 0:
            player.left = True
            player.right = False
            if player.steps > 21:
                player.left = False
                player.steps = 0
            else:
                player.x -= player.x_change
                player.steps += 1

        # Player moves right
        if keys[pygame.K_RIGHT] and player.x + 32 + player.x_change < W:
            player.right = True
            player.left = False
            if player.steps > 21:
                player.right = False
                player.steps = 0
            else:
                player.x += player.x_change
                player.steps += 1

        # Backspace makes player jump, if she is not already jumping.
        if keys[pygame.K_SPACE] and not player.jumping:
            player.jumping = True

        # Movement of player while jumping.
        # To get a natural 'jumping look' player moves faster at begin and end of jump.
        if player.jumping:
            if player.jump_count >= -7:
                if player.jump_count < 0:
                    num = -1
                else:
                    num = 1
                player.y_change = (player.jump_count ** 2) * 0.5 * num
                player.y -= player.y_change
                player.jump_count -= 1
            else:
                player.jumping = False
                player.jump_count = 7

    menu()


# Main menu of the game
def menu():
    title_font = pygame.font.Font('freesansbold.ttf', 32)
    title_text = title_font.render("Tinna the Icelandic Troll", True, (255, 255, 255))
    expl_font = pygame.font.Font('freesansbold.ttf', 20)
    text1 = "Tinna the Troll misses her loved one, who has turned into a northern light."
    text2 = "Help Tinna get her lover back!"
    text3 = "Press the spacebar to start the game."
    expl_text1 = expl_font.render(text1, True, (255, 0, 0))
    expl_text2 = expl_font.render(text2, True, (255, 0, 0))
    expl_text3 = expl_font.render(text3, True, (255, 255, 255))

    run_menu = True
    while run_menu:
        SCREEN.fill((0, 0, 0))
        SCREEN.blit(title_text, ((int(W / 2)-int(title_text.get_width() / 2)), 100))
        SCREEN.blit(expl_text1, ((int(W / 2)-int(expl_text1.get_width() / 2)), 250))
        SCREEN.blit(expl_text2, ((int(W / 2)-int(expl_text2.get_width() / 2)), 300))
        SCREEN.blit(expl_text3, ((int(W / 2)-int(expl_text3.get_width() / 2)), 390))
        SCREEN.blit(FRONT, (int(W / 2 - 16), 450))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run_game()
    pygame.quit()
    exit()


menu()
