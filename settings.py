import pygame as pg

pg.init()
pg.mixer.init()

TITLE = "Penguins!"
WIDTH = 1100
HEIGHT = 600
FPS = 50

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (173, 224, 255)
BGCOLOR = LIGHTBLUE
GREY = (44, 50, 61)

# images
#penguins
p = 12
image_u = pg.image.load('penguin_jump2.png')
image_u = pg.transform.scale(image_u, (641//p, 780//p))

image_j = pg.image.load('penguin_jump.png')
image_j = pg.transform.scale(image_j, (512//p, 576//p))

image_p_w1_r = pg.image.load('penguin_walk_1.png')
image_p_w1_r = pg.transform.scale(image_p_w1_r, (512//p, 576//p))
image_p_w1_l = pg.transform.flip(image_p_w1_r, True, False)

image_p_w2_r = pg.image.load('penguin_walk_2.png')
image_p_w2_r = pg.transform.scale(image_p_w2_r, (512//p, 576//p))
image_p_w2_l = pg.transform.flip(image_p_w2_r, True, False)

image_p_stop = pg.image.load('stop.png')
image_p_stop = pg.transform.scale(image_p_stop, (640//p, 576//p))

# buttons
pb = 5
image_b_u = pg.image.load('umbrella_button.png')
image_b_u = pg.transform.scale(image_b_u, (300//pb, 284//pb))
image_b_u_p = pg.image.load('umbrella_button_pushed.png')
image_b_u_p = pg.transform.scale(image_b_u_p, (300//pb, 284//pb))
umbrella_images = [image_b_u, image_b_u_p]

image_b_s = pg.image.load('stop_button.png')
image_b_s = pg.transform.scale(image_b_s, (300//pb, 284//pb))
image_b_s_p = pg.image.load('stop_button_pushed.png')
image_b_s_p = pg.transform.scale(image_b_s_p, (300//pb, 284//pb))
stop_images = [image_b_s, image_b_s_p]

image_b_b = pg.image.load('bomb_button.png')
image_b_b = pg.transform.scale(image_b_b, (300//pb, 284//pb))
image_b_b_p = pg.image.load('bomb_button_pushed.png')
image_b_b_p = pg.transform.scale(image_b_b_p, (300//pb, 284//pb))
bomb_images = [image_b_b, image_b_b_p]

image_b = pg.image.load('bum_button.png')
image_b = pg.transform.scale(image_b, (300//pb, 284//pb))
image_b_p = pg.image.load('bum_button_pushed.png')
image_b_p = pg.transform.scale(image_b_p, (300//pb, 284//pb))
bum_images = [image_b, image_b_p]

# other
s = pg.image.load('s.png')
s = pg.transform.scale(s, (70//2, 40))
s.set_colorkey(WHITE)
sc = pg.image.load('sc.png')
sc.set_colorkey(WHITE)
sl = pg.image.load('sl.png')
sl.set_colorkey(WHITE)
sr = pg.image.load('s.png')
sr.set_colorkey(WHITE)
c = pg.image.load('cc.png')
c.set_colorkey(WHITE)
sp = pg.image.load('spikes.png')
sp.set_colorkey(BLACK)

image_door = pg.image.load('door.png')
image_door = pg.transform.scale(image_door, (300//4, 300//4))

image_fridge = pg.image.load('fridge.png')
image_fridge = pg.transform.scale(image_fridge, (800//6, 800//8))

image_explosion = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pg.image.load(filename)
    img = pg.transform.scale(img, (152//2, 150//2))
    img.set_colorkey(BLACK)
    image_explosion.append(img)

image_cloud_1 = pg.image.load('cloud1.png')
image_cloud_1 = pg.transform.scale(image_cloud_1, ((2 * 128)//3, (2 * 71)//3))
image_cloud_1.set_colorkey(BLACK)

image_cloud_2 = pg.image.load('cloud2.png')
image_cloud_2 = pg.transform.scale(image_cloud_2, ((2 * 128)//3, (2 * 71)//3))
image_cloud_2.set_colorkey(BLACK)

image_cloud_3 = pg.image.load('cloud3.png')
image_cloud_3 = pg.transform.scale(image_cloud_3, ((2 * 128)//3, (2 * 71)//3))
image_cloud_3.set_colorkey(BLACK)
clouds = [image_cloud_1, image_cloud_2, image_cloud_3]

start_background = pg.image.load('tlo.png')

# sound
button_snd = pg.mixer.Sound('button.wav')
click_snd = pg.mixer.Sound('click.wav')
explosion_snd = pg.mixer.Sound('explosion.wav')
back_snd = pg.mixer.music.load('background.wav')
pg.mixer.music.set_volume(0.3)