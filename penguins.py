# -*- coding: utf-8 -*-
import pygame as pg
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.sounds = False
        self.music = False
        self.english = False
        self.level = 1
        self.center = (WIDTH / 2, 5)

        # game parameters
        self.penguin_number = 10
        self.bomb_number = 5
        self.umbrella_number = 5
        self.stop_number = 5
        self.needed = 5
        self.game_over = False
        self.next_level = False

        # penguins information
        self.current_penguin_number = 0
        self.penguin_home_number = 0
        self.last_penguin = 0
        self.home_penguins = 0
        self.killed = 0

        # buttons
        self.stop_button = False
        self.umbrella_button = False
        self.bomb_button = False
        self.any_powerup_button = False
        self.bum_button = False

    def background(self):
        # clouds
        p = Platform(self, clouds[0].convert(), 160, 60)
        self.all_sprites.add(p)
        self.clouds.add(p)

        p = Platform(self, clouds[1].convert(), 360, 25)
        self.all_sprites.add(p)
        self.clouds.add(p)

        p = Platform(self, clouds[2].convert(), 660, 40)
        self.all_sprites.add(p)
        self.clouds.add(p)

        p = Platform(self, clouds[1].convert(), 950, 65)
        self.all_sprites.add(p)
        self.clouds.add(p)

        # floor
        for i in range(0, WIDTH, 70 // 2):
            p = Platform(self, s.convert(), i, HEIGHT - 100)
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(0, WIDTH, 70):
            p = Platform(self, sc.convert(), i, HEIGHT - 70)
            self.all_sprites.add(p)
            self.platforms.add(p)

        # wall
        for i in range(0, HEIGHT, 70):
            w = Platform(self, c.convert(), 0, i)
            self.all_sprites.add(w)
            self.walls.add(w)
            w = Platform(self, c.convert(), 20, i)
            self.all_sprites.add(w)
            self.walls.add(w)

        # door
        d = Platform(self, image_door, self.center[0] - 35, self.center[1])
        self.all_sprites.add(d)

        # buttons
        umbrella_button = Umbrella_button(self, 17, 5)
        self.all_sprites.add(umbrella_button)
        self.buttons.add(umbrella_button)

        stop_button = Stop_button(self, 17, 290 // 5 + 30)
        self.all_sprites.add(stop_button)
        self.buttons.add(stop_button)

        bomb_button = Bomb_button(self, 17, 2 * (290 // 5 + 30))
        self.all_sprites.add(bomb_button)
        self.buttons.add(bomb_button)

        bum_button = Bum_button(self, 17, 4 * (290 // 5 + 40))
        self.all_sprites.add(bum_button)
        self.buttons.add(bum_button)

        self.penguins = []
        p = Penguin(self)
        self.current_penguin_number += 1
        self.penguins.append(p)
        self.last_penguin = pg.time.get_ticks()
        self.all_sprites.add(p)
        self.all_penguins.add(p)

    def new(self):
        if self.music: pg.mixer.music.play(loops=-1)
        self.all_sprites = pg.sprite.Group()
        self.all_penguins = pg.sprite.Group()
        self.stop_penguins = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.buttons = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.fridge = pg.sprite.Group()
        self.bum = pg.sprite.Group()
        self.clouds = pg.sprite.Group()
        self.dead = pg.sprite.Group()

        if self.level == 1:
            self.umbrella_number = 5
            self.stop_number = 5
            self.bomb_number = 5

            self.background()

            f = Fridge(self, 70, 409)
            self.all_sprites.add(f)
            self.fridge.add(f)

            for i in range(90, WIDTH, 70//2):
                p = Platform(self, s.convert(), i, 200)
                self.all_sprites.add(p)
                self.platforms.add(p)

            for i in range(WIDTH//3, WIDTH, 70//2):
                p = Platform(self, s.convert(), i, 300)
                self.all_sprites.add(p)
                self.platforms.add(p)

            for i in range((2 * WIDTH)//3, WIDTH, 70//2):
                p = Platform(self, s.convert(), i, 400)
                self.all_sprites.add(p)
                self.platforms.add(p)

        elif self.level == 2:
            self.umbrella_number = 4
            self.stop_number = 2
            self.bomb_number = 3

            self.center = (500, 7)
            self.background()

            f = Fridge(self, 150, 409)
            self.all_sprites.add(f)
            self.fridge.add(f)

            for i in range(400, WIDTH, 70 // 2):
                p = Platform(self, s.convert(), i, 200)
                self.all_sprites.add(p)
                self.platforms.add(p)

            for i in range(90, 300, 70 // 2):
                p = Platform(self, s.convert(), i, 200)
                self.all_sprites.add(p)
                self.platforms.add(p)

            for i in range(700, WIDTH, 70):
                p = Platform(self, sp.convert(), i, 168)
                self.all_sprites.add(p)
                self.dead.add(p)

            for i in range(90, 700, 70 // 2):
                p = Platform(self, s.convert(), i, 300)
                self.all_sprites.add(p)
                self.platforms.add(p)

            for i in range(800, WIDTH, 70 // 2):
                p = Platform(self, s.convert(), i, 300)
                self.all_sprites.add(p)
                self.platforms.add(p)

            for i in range(90, 200, 70):
                p = Platform(self, sp.convert(), i, 268)
                self.all_sprites.add(p)
                self.dead.add(p)

            for i in range(500, WIDTH, 70 // 2):
                p = Platform(self, s.convert(), i, 400)
                self.all_sprites.add(p)
                self.platforms.add(p)

            for i in range(900, WIDTH, 70):
                p = Platform(self, sp.convert(), i, 368)
                self.all_sprites.add(p)
                self.dead.add(p)

        elif self.level == 3:
            self.umbrella_number = 5
            self.stop_number = 5
            self.bomb_number = 5

            self.center = (400, 7)
            self.background()

            f = Fridge(self, 150, 409)
            self.all_sprites.add(f)
            self.fridge.add(f)

            for i in range(90, WIDTH, 70 // 2):
                p = Platform(self, s.convert(), i, 200)
                self.all_sprites.add(p)
                self.platforms.add(p)

            for i in range(800 + 90, WIDTH, 70):
                p = Platform(self, sp.convert(), i, 168)
                self.all_sprites.add(p)
                self.dead.add(p)

            for i in range(90, 300, 70):
                p = Platform(self, sp.convert(), i, 168)
                self.all_sprites.add(p)
                self.dead.add(p)

            for i in range(90, WIDTH, 70 // 2):
                p = Platform(self, s.convert(), i, 300)
                self.all_sprites.add(p)
                self.platforms.add(p)

            for i in range(700 + 90, WIDTH, 70):
                p = Platform(self, sp.convert(), i, 268)
                self.all_sprites.add(p)
                self.dead.add(p)

            for i in range(90, 350, 70):
                p = Platform(self, sp.convert(), i, 268)
                self.all_sprites.add(p)
                self.dead.add(p)

            for i in range(600 + 90, WIDTH, 70):
                p = Platform(self, sp.convert(), i, 468)
                self.all_sprites.add(p)
                self.dead.add(p)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        if self.penguin_number == self.home_penguins:
            self.playing = False
        if self.current_penguin_number == self.penguin_number and self.killed == self.penguin_number:
            self.playing = False
        if self.killed + self.home_penguins >= self.penguin_number:
            self.playing = False

        if self.any_powerup_button:
            pg.mouse.set_cursor(*pg.cursors.broken_x)
        else:
            pg.mouse.set_cursor(*pg.cursors.arrow)

        if self.current_penguin_number < self.penguin_number:
            if pg.time.get_ticks() - self.last_penguin > 3000:
                p = Penguin(self)
                self.current_penguin_number += 1
                self.penguins.append(p)
                self.last_penguin = pg.time.get_ticks()
                self.all_sprites.add(p)
                self.all_penguins.add(p)
        if self.bum_button:
            if self.sounds: explosion_snd.play()
            for p in self.penguins:
                p.kill()
                self.killed += 1
        self.all_sprites.update()

    def events(self):
        for event in pg.event.get():
            for button in self.buttons:
                button.handle_event(event)

            for penguin in self.all_penguins:
                penguin_was_stopped = penguin.stop
                penguin_was_bombed = penguin.bomb

                penguin.handle_event(event)

                penguin_is_stopped = penguin.stop
                penguin_is_bombed = penguin.bomb

                if penguin_is_stopped and not penguin_was_stopped: break
                if penguin_is_bombed and not penguin_was_bombed: break

            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        draw_text(self.screen, str(self.umbrella_number), 24, 300//pb - 15 , 284//pb + 3, 0)
        draw_text(self.screen, str(self.stop_number), 24, 300 // pb - 15, 2 * (284 // pb + 3) + 26, 0)
        draw_text(self.screen, str(self.bomb_number), 24, 300 // pb - 15, 3 * (284 // pb + 3) + 2 * 27, 0)

        draw_text(self.screen, 'OUT', 20, 300 // pb - 15, 3 * (284 // pb + 3) + 2 * 27 + 40, 1)
        draw_text(self.screen, str(self.current_penguin_number) + '/' + str(self.penguin_number), 20, 300 // pb - 15, 3 * (284 // pb + 3) + 2 * 27 + 60, 1)
        draw_text(self.screen, 'HOME', 20, 300 // pb - 15, 3 * (284 // pb + 3) + 2 * 27 + 100, 1)
        draw_text(self.screen, str(self.home_penguins) + '/' + str(self.needed), 20, 300 // pb - 15, 3 * (284 // pb + 3) + 2 * 27 + 120, 1)

        pg.display.flip()

    def show_start_screen(self):
        file = open("settings.txt", 'r').readlines()
        if file[0].find('1') > -1: self.sounds = True
        if file[1].find('1') > -1: self.music = True
        if file[2].find('1') > -1: self.english = True

        screen = pg.display.set_mode((WIDTH, HEIGHT))
        screen.blit(start_background, [0, 0])
        draw_text(self.screen, TITLE, 48, WIDTH / 2, HEIGHT / 4, 0)

        if not self.english: draw_text(self.screen,"Naciśnij ENTER by zacząć", 25, WIDTH / 2, HEIGHT  / 2, 0)
        else: draw_text(self.screen,"Press ENTER to play", 25, WIDTH / 2, HEIGHT  / 2 , 0)

        if not self.english: draw_text(self.screen,"Naciśnij SPACJĘ by zmienić ustawienia", 25, WIDTH / 2, HEIGHT / 2 + 50, 0)
        else: draw_text(self.screen,"Press SPACE to change settings", 25, WIDTH / 2, HEIGHT  / 2 + 50, 0)

        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP and event.key == pg.K_RETURN:
                    waiting = False
                elif event.type == pg.KEYUP and event.key == pg.K_SPACE:
                    self.show_settings_screen()
                    waiting = True
                    while waiting:
                        self.clock.tick(FPS)
                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                waiting = False
                                self.running = False
                            elif event.type == pg.KEYUP and event.key == pg.K_s:
                                self.sounds = not self.sounds
                                self.show_settings_screen()
                            elif event.type == pg.KEYUP and event.key == pg.K_m:
                                self.music = not self.music
                                self.show_settings_screen()
                            elif event.type == pg.KEYUP and event.key == pg.K_RETURN:
                                waiting = False

    def show_settings_screen(self):
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        screen.blit(start_background, [0, 0])
        draw_text(self.screen, TITLE, 48, WIDTH / 2, HEIGHT / 4, 0)

        if not self.english:
            draw_text(self.screen, "S - dźwięki", 25, WIDTH / 2 - 45, HEIGHT / 2, 0)
            draw_text(self.screen, str(self.sounds), 25, WIDTH / 2 + 100 - 45, HEIGHT / 2, 0)
        else:
            draw_text(self.screen, "S - sounds", 25, WIDTH / 2 - 45, HEIGHT / 2, 0)
            draw_text(self.screen, str(self.sounds), 25, WIDTH / 2 + 100 - 45, HEIGHT / 2, 0)

        if not self.english:
            draw_text(self.screen, "M - muzyka", 25, WIDTH / 2 - 45, HEIGHT / 2 + 50, 0)
            draw_text(self.screen, str(self.music), 25, WIDTH / 2 + 100 - 45, HEIGHT / 2 + 50, 0)
        else:
            draw_text(self.screen, "M - music", 25, WIDTH / 2 - 45, HEIGHT / 2 + 50, 0)
            draw_text(self.screen, str(self.music), 25, WIDTH / 2 + 100 - 45, HEIGHT / 2 + 50, 0)

        if self.english: draw_text(self.screen, "Press ENTER to start", 25, WIDTH / 2, HEIGHT / 2 + 100, 0)
        else: draw_text(self.screen, "Naciśnij ENTER żeby rozpocząć", 25, WIDTH / 2, HEIGHT / 2 + 100, 0)

        pg.display.flip()

    def show_level_screen(self):
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        screen.blit(start_background, [0, 0])

        if not self.english: draw_text(self.screen, 'WYBIERZ POZIOM', 48, WIDTH / 2, HEIGHT / 4, 0)
        else: draw_text(self.screen, 'CHOOSE LEVEL', 48, WIDTH / 2, HEIGHT / 4, 0)

        if not self.english: draw_text(self.screen, '1 - łatwy', 30, WIDTH / 2, HEIGHT / 4 + 100, 0)
        else: draw_text(self.screen, '1 - easy', 30, WIDTH / 2, HEIGHT / 4 + 100, 0)

        if not self.english: draw_text(self.screen, '2 - średni', 30, WIDTH / 2, HEIGHT / 4 + 200, 0)
        else: draw_text(self.screen, '2 - medium', 30, WIDTH / 2, HEIGHT / 4 + 200, 0)

        if not self.english: draw_text(self.screen, '3 - trudny', 30, WIDTH / 2, HEIGHT / 4 + 300, 0)
        else: draw_text(self.screen, '3 - hard', 30, WIDTH / 2, HEIGHT / 4 + 300, 0)

        pg.display.flip()
        self.wait_for_level_key()

    def wait_for_level_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                elif event.type == pg.KEYUP and event.key == pg.K_1:
                    self.level = 1
                    waiting = False
                elif event.type == pg.KEYUP and event.key == pg.K_2:
                    self.level = 2
                    waiting = False
                elif event.type == pg.KEYUP and event.key == pg.K_3:
                    self.level = 3
                    waiting = False

    def show_go_screen(self):
        if not self.running:
            return
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        screen.blit(start_background, [0, 0])

        if self.english:
            if self.home_penguins / self.penguin_number > 0.4:
                draw_text(self.screen, "YOU WON!", 48, WIDTH / 2, HEIGHT / 4, 0)
                if self.level < 3: draw_text(self.screen, "Try your luck at a higher level :)", 25, WIDTH / 2, HEIGHT / 4 + 60, 0)
            else: draw_text(self.screen, "GAME OVER", 48, WIDTH / 2, HEIGHT / 4, 0)
            draw_text(self.screen, "Score: " + str(int(100 * self.home_penguins / self.penguin_number)) + '%', 22, WIDTH / 2, HEIGHT / 2, 0)
            draw_text(self.screen, "Needed: " + '50%', 22, WIDTH / 2, HEIGHT / 2 + 100, 0)
        else:
            if self.home_penguins / self.penguin_number > 0.4:
                draw_text(self.screen, "ZWYCIĘSTWO!", 48, WIDTH / 2, HEIGHT / 4, 0)
                if self.level < 3: draw_text(self.screen, "Spróbuj szczęścia na wyższym poziomie :)", 25, WIDTH / 2, HEIGHT / 4 + 60, 0)
            else: draw_text(self.screen, "GRA SKOŃCZONA", 48, WIDTH / 2, HEIGHT / 4, 0)
            draw_text(self.screen, "Wynik: " + str(int(100 * self.home_penguins / self.penguin_number)) + '%', 22, WIDTH / 2, HEIGHT / 2, 0)
            draw_text(self.screen, "Wymagany wynik: " + '50%', 22, WIDTH / 2, HEIGHT / 2 + 100, 0)

        pg.display.flip()

        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False

if __name__ == "__main__":
    g = Game()
    g.show_start_screen()
    while g.running:
        g.show_level_screen()
        if g.running:
            g.new()
            g.show_go_screen()
    pg.quit()

