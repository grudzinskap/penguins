import pygame as pg
from settings import *

font_name = [pg.font.match_font('arial'), pg.font.match_font('arial', bold = True)]
def draw_text(surf, text, size, x, y, bold):
    font = pg.font.Font(font_name[bold], size)
    text_surface = font.render(text, True, GREY)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class Umbrella_button(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.button_images = umbrella_images
        self.image = self.button_images[0]
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pressed = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if not self.game.any_powerup_button:
                button_snd.play()
                self.game.umbrella_button = not self.game.umbrella_button
                self.game.any_powerup_button = not self.game.any_powerup_button
                self.pressed = not self.pressed
                self.image = self.button_images[self.pressed]
            elif self.game.any_powerup_button and self.pressed:
                button_snd.play()
                self.pressed = not self.pressed
                self.image = self.button_images[self.pressed]
                self.game.any_powerup_button = not self.game.any_powerup_button
                self.game.umbrella_button = not self.game.umbrella_button



class Stop_button(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.button_images = stop_images
        self.image = self.button_images[0]
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pressed = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if not self.game.any_powerup_button:
                button_snd.play()
                self.game.stop_button = not self.game.stop_button
                self.game.any_powerup_button = not self.game.any_powerup_button
                self.pressed = not self.pressed
                self.image = self.button_images[self.pressed]
            elif self.game.any_powerup_button and self.pressed:
                button_snd.play()
                self.pressed = not self.pressed
                self.image = self.button_images[self.pressed]
                self.game.any_powerup_button = not self.game.any_powerup_button
                self.game.stop_button = not self.game.stop_button


class Bomb_button(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.button_images = bomb_images
        self.image = self.button_images[0]
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pressed = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if not self.game.any_powerup_button:
                button_snd.play()
                self.game.bomb_button = not self.game.bomb_button
                self.game.any_powerup_button = not self.game.any_powerup_button
                self.pressed = not self.pressed
                self.image = self.button_images[self.pressed]
            elif self.game.any_powerup_button and self.pressed:
                button_snd.play()
                self.pressed = not self.pressed
                self.image = self.button_images[self.pressed]
                self.game.any_powerup_button = not self.game.any_powerup_button
                self.game.bomb_button = not self.game.bomb_button

class Bum_button(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.button_images = bum_images
        self.image = self.button_images[0]
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pressed = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos) and self.game.current_penguin_number == self.game.penguin_number:
            button_snd.play()
            self.pressed = True
            self.image = self.button_images[self.pressed]
            self.game.bum_button = True



class Penguin(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = image_j
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.game.center[0], self.game.center[1] + 50)
        self.umbrella = False
        self.stop = False
        self.walk = False
        self.load_images()
        self.last_update = 0
        self.current_frame = 0
        self.vx = 0
        self.vy = 2
        self.umbrella = False
        self.bomb = False
        self.radius = int(self.rect.width * .85) //2
        self.last_stop_penguin_hit = 0
        self.g = 0.5
        self.dropping = True
        self.right = True
        self.fly = False
        self.last_h = HEIGHT
        #pg.draw.circle(self.image, RED, (self.rect.width//2 + 5, self.rect.height//2), self.radius)




    def update(self):
        if self.dropping:
            if self.fly: self.flying()

            self.vx = 0
            self.vy = 1
            self.rect.y += self.vy

            ground_hit = pg.sprite.spritecollide(self, self.game.platforms, False)
            if ground_hit:
                if self.rect.bottom - self.last_h > 150 and not self.fly:
                    exp = Explosion(self.game, self, self.rect.center)
                    exp.suicide = True
                    self.game.all_sprites.add(exp)
                    self.game.bum.add(exp)
                    self.bomb = True
                    self.game.killed += 1
                    self.kill()
                else: self.last_h = self.rect.bottom

                self.walk = True
                self.dropping = False
                self.vy = 0
                if self.right:
                    self.vx = 1
                else: self.vx = -1
                #self.rect.bottom = ground_hit[0].rect.top

        elif self.walk:
            if self.rect.left < 0 or self.rect.right > WIDTH:
                self.vx = -self.vx
                self.right = not self.right

            self.rect.x += self.vx
            self.animate()

            stop_penguin_hit = pg.sprite.spritecollide(self, self.game.stop_penguins, False, pg.sprite.collide_circle)
            if stop_penguin_hit:
                if self.vx > 0:
                    self.rect.right = stop_penguin_hit[0].rect.x
                else:
                    self.rect.x = stop_penguin_hit[0].rect.right
                self.vx = -self.vx
                self.right = not self.right

            wall_hit = pg.sprite.spritecollide(self, self.game.walls, False, pg.sprite.collide_circle)
            if wall_hit:
                self.vx = -self.vx
                self.right = not self.right

            fridge_hit = pg.sprite.spritecollide(self, self.game.fridge, False, pg.sprite.collide_circle)
            if fridge_hit:
                self.game.home_penguins += 1
                self.game.penguin_home_number += 1
                self.kill()

            ground_hit = pg.sprite.spritecollide(self, self.game.platforms, False)
            if not ground_hit:
                self.last_h = self.rect.bottom
                self.dropping = True
                self.walk = False

            dead_hit = pg.sprite.spritecollide(self, self.game.dead, False)
            if dead_hit:
                exp = Explosion(self.game, self, self.rect.center)
                exp.suicide = True
                self.game.all_sprites.add(exp)
                self.game.bum.add(exp)
                self.bomb = True
                self.game.killed += 1
                self.kill()



    def stopping(self):
        #self.radius = int(self.rect.width) // 2
        self.walk = False
        self.stop = True
        self.vx = 0
        self.vy = 0
        self.image = image_p_stop
        self.image.set_colorkey(WHITE)
        self.game.stop_penguins.add(self)

    def flying(self):
        #self.radius = int(self.rect.width) // 2
        x, y = self.rect.x, self.rect.y
        self.image = image_u
        self.image.set_colorkey(WHITE)
        #self.rect = self.image.get_rect()
        #self.rect.x, self.rect.y = x, y


    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and self.game.stop_button == True and self.vy == 0 and not self.stop and self.game.stop_number > 0:
                if self.game.sounds: click_snd.play()
                self.game.stop_number -= 1
                self.stopping()
            if self.rect.collidepoint(event.pos) and self.game.umbrella_button == True and self.vy == 0 and not self.fly and self.game.umbrella_number > 0:
                if self.game.sounds: click_snd.play()
                self.game.umbrella_number -= 1
                self.fly = True
            if self.rect.collidepoint(event.pos) and self.game.bomb_button == True and self.vy == 0 and not self.bomb and self.game.bomb_number > 0:
                self.game.bomb_number -= 1
                exp = Explosion(self.game, self, self.rect.center)
                self.game.all_sprites.add(exp)
                self.game.bum.add(exp)
                self.bomb = True
                self.game.killed += 1
                self.kill()
        # if self.game.any_powerup_button:
        #     if event.type == pg.MOUSEMOTION:
        #         if self.rect.collidepoint(event.pos):
        #             pg.mouse.set_cursor(*pg.cursors.broken_x)
        #         else:
        #             pg.mouse.set_cursor(*pg.cursors.arrow)


    def load_images(self):
        self.walk_frames_r = [image_p_w1_r, image_p_w2_r]
        self.walk_frames_l = [image_p_w1_l, image_p_w2_l]

        for frame in self.walk_frames_r:
            frame.set_colorkey(BLACK)
        for frame in self.walk_frames_l:
            frame.set_colorkey(BLACK)

    def animate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 150:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % 2
        x, y = self.rect.x, self.rect.y
        if self.vx > 0:
            self.image = self.walk_frames_r[self.current_frame]
            #self.rect = self.image.get_rect()
            #self.rect.x, self.rect.y = x, y
        elif self.vx < 0:
            self.image = self.walk_frames_l[self.current_frame]
            #self.rect = self.image.get_rect()
            #self.rect.x, self.rect.y = x, y



class Platform(pg.sprite.Sprite):
    def __init__(self, game, image, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = image
        #self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Explosion(pg.sprite.Sprite):
    def __init__(self, game, penguin, center):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = image_explosion[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 150
        self.radius = self.rect.width//3
        self.suicide = False

    def update(self):
        pg.draw.circle(self.image, RED, (self.rect.width // 2, self.rect.height // 2), self.radius)
        now = pg.time.get_ticks()
        if self.frame == 1 and self.game.sounds: explosion_snd.play()
        if now - self.last_update > self.frame_rate:
            self.frame += 1
            if self.frame == len(image_explosion):
                if not self.suicide: pg.sprite.spritecollide(self, self.game.platforms, True, pg.sprite.collide_circle)
                self.kill()
            else:
                center = self.rect.center
                self.image = image_explosion[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


class Fridge(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = image_fridge
        #self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.radius = int(.8 *self.rect.width) // 3
        #pg.draw.rect(self.image, BLUE, (self.rect.x, self.rect.y, self.rect.width, self.rect.height))
        #pg.draw.circle(self.image, RED, (self.rect.width // 2, self.rect.height // 2), self.radius)