import pygame
import random

pygame.init()

#alap beállítások
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
running = True
clock = pygame.time.Clock()
BG_COLOR = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

# ütők
rocket_x = WIDTH-740 #800-740 = 60. Bal oldal 60px padding
rocket_y = HEIGHT/2-50
rocket_width = 10
rocket_height = 100

# ellenfél
op_rocket_x = WIDTH-rocket_width-60 #800-width-60 = 740. Jobb oldal 60px padding
op_rocket_y = HEIGHT/2-50
op_rocket_width = 10
op_rocket_height = 100

# labda
ball_x = WIDTH/2
ball_y = HEIGHT/2
ball_r = 7
le = True
fel = False
jobb = True
bal = False

#scores
player = 0
op = 0

# Font inicializálás
FONT = pygame.font.Font(None, 36)
while running:
  
  if player == 11:
    screen.fill(BG_COLOR)
    kiiras = FONT.render("Nyertél", True, WHITE)
    screen.blit(kiiras, (WIDTH/2-50, HEIGHT/2))
    pygame.time.delay(2000)
    pygame.display.flip()
    running = False
  if op == 11:
    screen.fill(BG_COLOR)
    kiiras = FONT.render("Vesztettél", True, WHITE)
    screen.blit(kiiras, (WIDTH/2-50, HEIGHT/2))
    pygame.display.flip()
    pygame.time.delay(2000)
    running = False

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(BG_COLOR)
  rocket = pygame.draw.rect(screen, WHITE, (rocket_x, rocket_y, rocket_width, rocket_height))
  op_rocket = pygame.draw.rect(screen, WHITE, (op_rocket_x, op_rocket_y, op_rocket_width, op_rocket_height))
  ball = pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_r)

# labda mozgása
  sebesseg = 6
  #terulet = pygame.draw.rect(screen, RED, (op_rocket_x-ball_r*2, rocket_y, ball_r*2, rocket_height))
  if ((ball_x >= 70) and (ball_x < 70+ball_r*2)) and ((ball_y >= rocket_y) and (ball_y <= rocket_y+rocket_height)):
    sebesseg += 20
    bal = False
    jobb = True
    choice = random.randint(0,2)
    if choice == 0:
      le = True
      fel = False
    elif choice == 1:
      fel = True
      le = False
    elif choice == 2:
      fel = True
      le = True
  if ((ball_x > 720) and (ball_x > WIDTH-op_rocket_x-ball_r)) and ((ball_y >= op_rocket_y) and (ball_y <= op_rocket_y+op_rocket_height)):
    sebesseg += 20
    jobb = False
    bal = True
    choice = random.randint(0,2)
    if choice == 0:
      le = True
      fel = False
    elif choice == 1:
      fel = True
      le = False
    elif choice == 2:
      fel = True
      le = True
# y tengelyen levő irány haladás megkötése
  if le:
    ball_y += sebesseg
    if (ball_y == HEIGHT-ball_r) or (ball_y > HEIGHT-ball_r):
      le = False
      fel = True
  if fel:
    ball_y -= sebesseg
    if (ball_y == 0) or (ball_y < 0):
      fel = False
      le = True
# x tengelyen levő irány haladás megkötése. Legyen random, melyik irányba halad.
  if jobb:
    ball_x += sebesseg
    if (ball_x == WIDTH-ball_r) or (ball_x > WIDTH-ball_r):
      player += 1
      jobb = False
      bal = True
      ball_x = WIDTH/2
      ball_y = HEIGHT/2
      choice = random.randint(0,2)
      if choice == 0:
        le = True
        fel = False
      elif choice == 1:
        fel = True
        le = False
      elif choice == 2:
        fel = True
        le = True
  if bal:
    ball_x -= sebesseg
    if (ball_x == 0) or (ball_x < 0):
      op += 1
      bal = False
      jobb = True
      ball_x = WIDTH/2
      ball_y = HEIGHT/2
      choice = random.randint(0,2)
      if choice == 0:
        le = True
        fel = False
      elif choice == 1:
        fel = True
        le = False
      elif choice == 2:
        fel = True
        le = True
# ütők mozgása
  r_sebesseg = 6.69
  lenyomott_gombok = pygame.key.get_pressed()
  if lenyomott_gombok[pygame.K_UP]:
    rocket_y -= r_sebesseg
    if (rocket_y == 0) or (rocket_y < 0):
      rocket_y = 1

  if lenyomott_gombok[pygame.K_DOWN]:
    rocket_y += r_sebesseg
    if (rocket_y == HEIGHT-rocket_height) or (rocket_y > HEIGHT-rocket_height):
      rocket_y = HEIGHT-rocket_height
  
  if (op_rocket_y == 0) or (op_rocket_y < 0):
    op_rocket_y = 1
  if (op_rocket_y == HEIGHT-op_rocket_height) or (op_rocket_y > HEIGHT-op_rocket_height):
    op_rocket_y = HEIGHT-op_rocket_height
  
  if op_rocket_y < ball_y:
    op_rocket_y += r_sebesseg-2
  if op_rocket_y > ball_y:
    op_rocket_y -= r_sebesseg-2

#score megjelenítés
  player_score = FONT.render(str(player), True, WHITE)
  op_score = FONT.render(str(op), True, WHITE)
  screen.blit(player_score, (WIDTH // 2 - 50, 50))  # Player pontszám (kicsit balra a középtől)
  screen.blit(op_score, (WIDTH // 2 + 50, 50))

  pygame.display.update()
  clock.tick(60)

pygame.quit()