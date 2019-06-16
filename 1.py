import pygame
from pygame.mixer_music import set_volume

pygame.init()
gray = (119, 118, 110)
black = (0, 0, 0)
red = (240, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
bright_red = (255, 10, 10)
bright_green = (0, 220, 0)
bright_blue = (0, 0, 254)
display_width = 800
display_height = 600
import time
import random

pygame.mixer.music.load('intro.mp3')
pygame.mixer.music.play(-1)

gamedisplays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Gra")
clock = pygame.time.Clock()
character = pygame.image.load("chodzenie/7.png")
character = pygame.transform.scale(character, (80, 80))
backgroundpic = pygame.image.load("zz.png")
yellow_strip = pygame.image.load("yellow strip.jpg")
strip = pygame.image.load("strip.jpg")
intro_background = pygame.image.load("background.jpg")
instruction_background = pygame.image.load("background2.jpg")
car_width = 82
collect_width=15
pause = False


def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gamedisplays.blit(intro_background, (0, 0))
        button("START", 150, 520, 100, 50, green, bright_green, "play")
        button("WYJDŹ", 550, 520, 100, 50, red, bright_red, "quit")
        pygame.display.update()
        clock.tick(50)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gamedisplays, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                countdown()
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "pause":
                paused()
            elif action == "unpause":
                unpaused()


    else:
        pygame.draw.rect(gamedisplays, ic, (x, y, w, h))
    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    textsurf, textrect = text_objects(msg, smalltext)
    textrect.center = ((x + (w / 2)), (y + (h / 2)))
    gamedisplays.blit(textsurf, textrect)


def paused():
    global pause

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gamedisplays.blit(instruction_background, (0, 0))
        button("KONTYNUUJ", 150, 520, 150, 50, green, bright_green, "unpause")
        button("RESTART", 350, 520, 150, 50, blue, bright_blue, "play")
        button("WYJDŹ", 550, 520, 150, 50, red, bright_red, "quit")
        pygame.display.update()
        clock.tick(30)


def unpaused():
    global pause
    pause = False


def countdown_background():
    font = pygame.font.SysFont(None, 35)
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    gamedisplays.blit(backgroundpic, (0, 0))
    gamedisplays.blit(backgroundpic, (0, 200))
    gamedisplays.blit(backgroundpic, (0, 400))
    gamedisplays.blit(backgroundpic, (700, 0))
    gamedisplays.blit(backgroundpic, (700, 200))
    gamedisplays.blit(backgroundpic, (700, 400))
    gamedisplays.blit(yellow_strip, (400, 100))
    gamedisplays.blit(yellow_strip, (400, 200))
    gamedisplays.blit(yellow_strip, (400, 300))
    gamedisplays.blit(yellow_strip, (400, 400))
    gamedisplays.blit(yellow_strip, (400, 100))
    gamedisplays.blit(yellow_strip, (400, 500))
    gamedisplays.blit(yellow_strip, (400, 0))
    gamedisplays.blit(yellow_strip, (400, 600))
    gamedisplays.blit(strip, (120, 200))
    gamedisplays.blit(strip, (120, 0))
    gamedisplays.blit(strip, (120, 100))
    gamedisplays.blit(strip, (680, 100))
    gamedisplays.blit(strip, (680, 0))
    gamedisplays.blit(strip, (680, 200))
    gamedisplays.blit(character, (x, y))
    score = font.render("WYNIK: 0", True, red)
    gamedisplays.blit(score, (0, 30))
    button("PAUZA", 700, 0, 100, 50, green, bright_green, "pause")


def countdown():
    countdown = True
    while countdown:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gamedisplays.fill(gray)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("3", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gamedisplays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        gamedisplays.fill(gray)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("2", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gamedisplays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        gamedisplays.fill(gray)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("1", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gamedisplays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        gamedisplays.fill(gray)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("START!", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gamedisplays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        game_loop()


def obstacle(obs_startx, obs_starty, obs):
    if obs == 0:
        obs_pic = pygame.image.load("car9.png")
    elif obs == 1:
        obs_pic = pygame.image.load("car99.png")
    gamedisplays.blit(obs_pic, (obs_startx, obs_starty))


def obstacleCollect(obs_startx, obs_starty, obs):
    if obs == 0:
        obs_pic = pygame.image.load("qqq.png")
    elif obs == 1:
        obs_pic = pygame.image.load("www.png")
    gamedisplays.blit(obs_pic, (obs_startx, obs_starty))


def score_system(passed, score):
    font = pygame.font.SysFont(None, 35)
    score = font.render("WYNIK: " + str(score), True, red)
    gamedisplays.blit(score, (0, 30))


def text_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((display_width / 2), (display_height / 2))
    gamedisplays.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash():
    message_display("ZŁAPANY")


def background():
    gamedisplays.blit(backgroundpic, (0, 0))
    gamedisplays.blit(backgroundpic, (0, 200))
    gamedisplays.blit(backgroundpic, (0, 400))
    gamedisplays.blit(backgroundpic, (700, 0))
    gamedisplays.blit(backgroundpic, (700, 200))
    gamedisplays.blit(backgroundpic, (700, 400))
    gamedisplays.blit(yellow_strip, (400, 0))
    gamedisplays.blit(yellow_strip, (400, 100))
    gamedisplays.blit(yellow_strip, (400, 200))
    gamedisplays.blit(yellow_strip, (400, 300))
    gamedisplays.blit(yellow_strip, (400, 400))
    gamedisplays.blit(yellow_strip, (400, 500))
    gamedisplays.blit(strip, (120, 0))
    gamedisplays.blit(strip, (120, 100))
    gamedisplays.blit(strip, (120, 200))
    gamedisplays.blit(strip, (680, 0))
    gamedisplays.blit(strip, (680, 100))
    gamedisplays.blit(strip, (680, 200))


def car(x, y):
    gamedisplays.blit(character, (x, y))


def game_loop():
    pygame.mixer.music.load('muzyka.mp3')
    pygame.mixer.music.play(-1)
    global pause
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    obstacle_speed = 9
    obs = 0
    y_change = 0
    obs_startx = random.randrange(200, (display_width - 200))
    obs_starty = -750
    obs_width = 56
    obs_height = 165
    passed = 0
    level = 0
    score = 0
    y2 = 7
    fps = 120

    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -6
                elif event.key == pygame.K_RIGHT:
                    x_change = 6
                elif event.key == pygame.K_a:
                    obstacle_speed += 2
                elif event.key == pygame.K_b:
                    obstacle_speed -= 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        pause = True
        gamedisplays.fill(gray)

        rel_y = y2 % backgroundpic.get_rect().width
        gamedisplays.blit(backgroundpic, (0, rel_y - backgroundpic.get_rect().width))
        gamedisplays.blit(backgroundpic, (700, rel_y - backgroundpic.get_rect().width))
        if rel_y < 800:
            gamedisplays.blit(backgroundpic, (0, rel_y))
            gamedisplays.blit(backgroundpic, (700, rel_y))
            gamedisplays.blit(yellow_strip, (400, rel_y))
            gamedisplays.blit(yellow_strip, (400, rel_y + 100))
            gamedisplays.blit(yellow_strip, (400, rel_y + 200))
            gamedisplays.blit(yellow_strip, (400, rel_y + 300))
            gamedisplays.blit(yellow_strip, (400, rel_y + 400))
            gamedisplays.blit(yellow_strip, (400, rel_y + 500))
            gamedisplays.blit(yellow_strip, (400, rel_y - 100))
            gamedisplays.blit(strip, (120, rel_y - 200))
            gamedisplays.blit(strip, (120, rel_y + 20))
            gamedisplays.blit(strip, (120, rel_y + 30))
            gamedisplays.blit(strip, (680, rel_y - 100))
            gamedisplays.blit(strip, (680, rel_y + 20))
            gamedisplays.blit(strip, (680, rel_y + 30))

        y2 += obstacle_speed

        obs_starty -= (obstacle_speed / 6)
        obstacle(obs_startx, obs_starty, obs)
        #obstacleCollect(obs_startx,obs_starty,obs)
        obs_starty += obstacle_speed
        car(x, y)
        score_system(passed, score)
        if x > 690 - car_width or x < 110:
            pygame.mixer.music.load('policja.mp3')
            pygame.mixer.music.play(1)
            crash()

        if x > display_width - (car_width + 110) or x < 110:
            pygame.mixer.music.load('policja.mp3')
            pygame.mixer.music.play(1)
            crash()

        if obs_starty > display_height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(170, (display_width - 170))
            obs = random.randrange(0, 2)
            passed = passed + 1
            score = passed * 10
            if int(passed) % 10 == 0:
                level = level + 1
                obstacle_speed + 2
                largetext = pygame.font.Font("freesansbold.ttf", 90)
                textsurf, textrect = text_objects("POZIOM " + str(level), largetext)
                obstacle_speed=obstacle_speed+2
                textrect.center = ((display_width / 2), (display_height / 2))
                gamedisplays.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)

        if y < obs_starty + obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x + car_width > obs_startx and x + car_width < obs_startx + obs_width:
                pygame.mixer.music.load('policja.mp3')
                pygame.mixer.music.play(1)
                crash()
        button("PAUZA", 700, 0, 100, 50, green, bright_green, "pause")
        pygame.display.update()
        clock.tick(120)


intro_loop()
game_loop()
pygame.quit()
quit()
