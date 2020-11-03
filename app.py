import pygame
import random
import math

# initilize the pygame and create window
pygame.init()
window = pygame.display.set_mode((800, 800))

# logo and title
pygame.display.set_caption(" Space Invaders")
pygame.display.set_icon(pygame.image.load("images/rocket-ship.png"))

# importing images
spaceImg = pygame.image.load("images/space.png")
spaceshipImg = pygame.image.load("images/rocket.png")
enemy1Img = pygame.image.load("images/ufo1.png")
enemy2Img = pygame.image.load("images/ufo2.png")
enemy3Img = pygame.image.load("images/ufo3.png")
bulletImg = pygame.image.load("images/bullet.png")

# player
playerX = 350
playerY = 700
playerXChange = 0
playerYChange = 0

# enemy1
enemyX1 = random.randint(0, 736)
enemyY1 = random.randint(0, 100)
enemyX1Change = 0.5
enemyY1Change = 50

# enemy2
enemyX2 = random.randint(0, 736)
enemyY2 = random.randint(0, 100)
enemyX2Change = 0.8
enemyY2Change = 20

# enemy3
enemyX3 = random.randint(0, 736)
enemyY3 = random.randint(0, 100)
enemyX3Change = 1
enemyY3Change = 20

# bullet
showBullet = False
bulletX = playerX + 20
bulletY = playerY
bulletXChange = 0
bulletYChange = -1.5

# score
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
scoreX = 10
scoreY = 10

def showScore(x, y):
    scoreToShow = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(scoreToShow, (x, y))

def player(x, y):
    # top screen drawing
    window.blit(spaceshipImg, (x, y))


def enemy(img, x, y):
    # top screen drawing
    window.blit(img, (x, y))


def bullet(x, y):
    # top screen drawing
    window.blit(bulletImg, (x, y))


# find distance between bullet and enemy
def distance(x1, x2, y1, y2):
    return int(math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1))))


# running the game
running = True
while running:
    # background of game
    window.fill((0, 0, 0))
    window.blit(spaceImg, (0, 0))

    # checks if the program has exited
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False

        # check if keyboard is pressed
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT:
                playerXChange -= 1.2
            if events.key == pygame.K_RIGHT:
                playerXChange += 1.2
            # checks if bullet is fired
            if events.key == pygame.K_SPACE and showBullet == False:
                showBullet = True
                bulletX = playerX + 20
                bulletY = playerY

        if events.type == pygame.KEYUP:
            if events.key == pygame.K_RIGHT or events.key == pygame.K_LEFT:
                playerXChange = 0


    # checks if bullet hit enemy
    if distance(int(bulletX) + 16, int(enemyX1) + 32, int(bulletY) + 16, int(enemyY1) + 32) <= 32:
        score += 1
        enemyX1 = random.randint(0, 736)
        enemyY1 = random.randint(0, 100)
        bulletY = 1000
        showBullet = False

    if distance(int(bulletX) + 16, int(enemyX2) + 32, int(bulletY) + 16, int(enemyY2) + 32) <= 32:
        score += 1
        enemyX2 = random.randint(0, 736)
        enemyY2 = random.randint(0, 100)
        bulletY = 1000
        showBullet = False

    if distance(int(bulletX) + 16, int(enemyX3) + 32, int(bulletY) + 16, int(enemyY3) + 32) <= 40:
        score += 1
        enemyX3 = random.randint(0, 736)
        enemyY3 = random.randint(0, 100)
        bulletY = 1000
        showBullet = False


    # change the value of x
    playerX += playerXChange
    enemyX1 += enemyX1Change
    enemyX2 += enemyX2Change
    enemyX3 += enemyX3Change

    # checks if player is in window
    if playerX >= 736:
        playerX = 736
    if playerX <= 0:
        playerX = 0

    # enemy1 movement
    if enemyX1 >= 736:
        enemyX1 = 736
        enemyX1Change = -0.5
        enemyY1 += enemyY1Change
    if enemyX1 <= 0:
        enemyX1 = 0
        enemyX1Change = 0.5
        enemyY1 += enemyY1Change
    # enemy2 movement
    if enemyX2 >= 736:
        enemyX2 = 736
        enemyX2Change = -0.8
        enemyY2 += enemyY1Change
    if enemyX2 <= 0:
        enemyX2 = 0
        enemyX2Change = 0.8
        enemyY2 += enemyY1Change
    # enemy2 movement
    if enemyX3 >= 736:
        enemyX3 = 736
        enemyX3Change = -1
        enemyY3 += enemyY1Change
    if enemyX3 <= 0:
        enemyX3 = 0
        enemyX3Change = 1
        enemyY3 += enemyY1Change

    # bullet movement
    if bulletY <= 0:
        bulletY = 1000
        showBullet = False

    # calling player function
    player(playerX, playerY)

    # calling enemy functions
    enemy(enemy1Img, enemyX1, enemyY1)
    enemy(enemy2Img, enemyX2, enemyY2)
    enemy(enemy3Img, enemyX3, enemyY3)

    # calling bullet function
    if showBullet:
        bullet(bulletX, bulletY)
        bulletY += bulletYChange

    showScore(scoreX, scoreY)

    pygame.display.update()
