import pygame
from random import randint, choice
import time


def g12():
    pygame.init()
    pygame.mixer.init()

    WIDTH = 1200
    HEIGHT = 1200

    font_object = pygame.font.SysFont("arial", 32)
    next_object = pygame.font.SysFont("arial", 24)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    sprites = pygame.sprite.Group()
    bad_end = pygame.sprite.Group()
    good_end = pygame.sprite.Group()
    initial = pygame.sprite.Group()
    grounds = pygame.sprite.Group()
    ending = pygame.sprite.Group()

    end = pygame.sprite.Sprite(ending)
    end.image = pygame.image.load("static/12/png/ground/end.png")
    end.rect = end.image.get_rect()
    end.rect.left = 0
    end.rect.top = 0

    start = pygame.sprite.Sprite(initial)
    start.image = pygame.image.load("static/12/png/ground/start.png")
    start.rect = start.image.get_rect()
    start.rect.left = 0
    start.rect.top = 0

    background_1 = pygame.image.load("static/12/png/ground/background 1.png")
    background_2 = pygame.image.load("static/12/png/ground/background 2.png")
    background_3 = pygame.image.load("static/12/png/ground/background 3.png")
    background_4 = pygame.image.load("static/12/png/ground/background 4.png")
    background = [background_1, background_2, background_3, background_4]

    sad_end = pygame.sprite.Sprite(bad_end)
    happy_end = pygame.sprite.Sprite(good_end)

    sad_end.image = pygame.image.load("static/12/png/ground/sad.png")
    happy_end.image = pygame.image.load("static/12/png/ground/happy.png")

    sad_end.rect = sad_end.image.get_rect()
    sad_end.rect.left = 0
    sad_end.rect.top = 0

    happy_end.rect = happy_end.image.get_rect()
    happy_end.rect.left = 0
    happy_end.rect.top = 0

    ground = pygame.sprite.Sprite(grounds)
    ground.image = choice(background)
    ground.rect = ground.image.get_rect()
    ground.rect.left = 0
    ground.rect.top = 0

    Inaction = pygame.image.load("static/12/png/unicorn/Inaction.png")
    A = pygame.image.load("static/12/png/unicorn/A.png")
    D = pygame.image.load("static/12/png/unicorn/D.png")
    Sa = pygame.image.load("static/12/png/unicorn/SA.png")
    Sd = pygame.image.load("static/12/png/unicorn/SD.png")
    Wa = pygame.image.load("static/12/png/unicorn/WA.png")
    Wd = pygame.image.load("static/12/png/unicorn/WD.png")

    player = pygame.sprite.Sprite(sprites)
    player.image = Inaction
    player.rect = player.image.get_rect()
    player.rect.centerx = WIDTH // 4
    player.rect.centery = (HEIGHT // 4) * 3

    meteor_1 = pygame.image.load("static/12/png/objects/meteor 1.png")
    meteor_2 = pygame.image.load("static/12/png/objects/meteor 2.png")
    meteor_3 = pygame.image.load("static/12/png/objects/meteor 3.png")
    meteor_4 = pygame.image.load("static/12/png/objects/meteor 4.png")

    meteors = [meteor_1, meteor_2, meteor_3, meteor_4]

    meteorite_1 = pygame.sprite.Sprite(sprites)
    meteorite_1.image = choice(meteors)
    meteorite_1.rect = meteorite_1.image.get_rect()
    meteorite_1.rect.centerx = WIDTH
    meteorite_1.rect.centery = randint(
        meteorite_1.rect.width, HEIGHT - meteorite_1.rect.width
    )

    meteorite_2 = pygame.sprite.Sprite(sprites)
    meteorite_2.image = choice(meteors)
    meteorite_2.rect = meteorite_2.image.get_rect()
    meteorite_2.rect.centerx = WIDTH - 800
    meteorite_2.rect.centery = randint(
        meteorite_2.rect.width, HEIGHT - meteorite_2.rect.width
    )

    meteorite_3 = pygame.sprite.Sprite(sprites)
    meteorite_3.image = choice(meteors)
    meteorite_3.rect = meteorite_3.image.get_rect()
    meteorite_3.rect.centerx = WIDTH - 400
    meteorite_3.rect.centery = randint(
        meteorite_3.rect.width, HEIGHT - meteorite_3.rect.width
    )

    cake_1 = pygame.image.load("static/12/png/objects/cake 1.png")
    cake_2 = pygame.image.load("static/12/png/objects/cake 2.png")
    cake_3 = pygame.image.load("static/12/png/objects/cake 3.png")
    cakes = [cake_1, cake_2, cake_3]

    biscuit_1 = pygame.sprite.Sprite(sprites)
    biscuit_1.image = choice(cakes)
    biscuit_1.rect = biscuit_1.image.get_rect()
    biscuit_1.rect.centerx = randint(
        biscuit_1.rect.width // 2, WIDTH - biscuit_1.rect.width // 2
    )
    biscuit_1.rect.centery = randint(
        biscuit_1.rect.height // 2, HEIGHT - biscuit_1.rect.height // 2
    )

    biscuit_2 = pygame.sprite.Sprite(sprites)
    biscuit_2.image = choice(cakes)
    biscuit_2.rect = biscuit_2.image.get_rect()
    biscuit_2.rect.centerx = randint(
        biscuit_2.rect.width // 2, WIDTH - biscuit_2.rect.width // 2
    )
    biscuit_2.rect.centery = randint(
        biscuit_2.rect.height // 2, HEIGHT - biscuit_2.rect.height // 2
    )

    clock = pygame.time.Clock()

    initial.draw(screen)
    pygame.display.update()

    cycle_1 = True
    ch = 0

    field = [[0 for i in range(5)] for i in range(3)]
    CELLx = WIDTH // 5
    CELLy = HEIGHT // 3

    space = "static/12/music/Space.mp3"
    pygame.mixer.music.load(space)
    pygame.mixer.music.play(-1)

    while cycle_1:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                i = x // CELLx
                j = y // CELLy

                if 0 < i and i < 4 and j == 1:
                    ch += 1

        if ch == 1:
            cycle_1 = False

    cat = "static/12/music/Nyan.mp3"
    pygame.mixer.music.load(cat)
    pygame.mixer.music.play(-1)

    pause_space = False
    speed = 1
    score = 0
    meteorite_delay = 0
    expectation_x = expectation_y = 0
    background_delay = 0
    condition = 2
    cake = 0
    meteorite = 0

    cycle_2 = True
    while cycle_2:

        if background_delay >= 150:
            ground.image = choice(background)
            background_delay -= 150
        if background_delay < 150:
            background_delay += 1

        expectation_x = player.rect.centerx
        expectation_y = player.rect.centery

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            pause_space = not pause_space
            time.sleep(0.2)

        if not pause_space:

            if keys[pygame.K_w] or keys[pygame.K_UP]:
                if player.image == A or player.image == Wa or player.image == Inaction:
                    player.image = Wa
                if player.image == D or player.image == Wd or player.image == Inaction:
                    player.image = Wd
                player.rect.top = max(player.rect.top - speed * 2, 0)

            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                if player.image == A or player.image == Sa or player.image == Inaction:
                    player.image = Sa
                if player.image == D or player.image == Sd or player.image == Inaction:
                    player.image = Sd
                player.rect.bottom = min(player.rect.bottom + speed * 2, HEIGHT)

            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                player.image = A
                player.rect.left = max(player.rect.left - speed * 2, 0)

            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                player.image = D
                player.rect.right = min(player.rect.right + speed * 2, WIDTH)

            if pygame.sprite.collide_mask(player, biscuit_1):
                y += 1
                score += 10
                cake += 1
                biscuit_1.rect.centerx = HEIGHT
                biscuit_1.rect.centery = randint(
                    biscuit_1.rect.height // 2, HEIGHT - biscuit_1.rect.height // 2
                )
                biscuit_1.image = choice(cakes)

            biscuit_1.rect.centerx -= speed
            if biscuit_1.rect.centerx <= 0:
                biscuit_1.rect.centerx = HEIGHT
                biscuit_1.rect.centery = randint(
                    biscuit_1.rect.height // 2, HEIGHT - biscuit_1.rect.height // 2
                )

            if pygame.sprite.collide_mask(player, biscuit_2):
                y += 1
                score += 10
                cake += 1
                biscuit_2.rect.centerx = HEIGHT
                biscuit_2.rect.centery = randint(
                    biscuit_2.rect.height // 2, HEIGHT - biscuit_2.rect.height // 2
                )
                biscuit_2.image = choice(cakes)

            biscuit_2.rect.centerx -= speed
            if biscuit_2.rect.centerx <= 0:
                biscuit_2.rect.centerx = HEIGHT
                biscuit_2.rect.centery = randint(
                    biscuit_2.rect.height // 2, HEIGHT - biscuit_2.rect.height // 2
                )

            meteorite_1.rect.centerx -= speed * 4
            if meteorite_1.rect.centerx <= 0:
                meteorite_1.rect.centerx = WIDTH
                meteorite_1.rect.centery = randint(
                    meteorite_1.rect.height, HEIGHT - meteorite_1.rect.height
                )

            if pygame.sprite.collide_mask(player, meteorite_1):
                speed -= 1
                meteorite += 1
                score -= 25
                meteorite_1.rect.centerx = WIDTH
                meteorite_1.rect.centery = randint(
                    meteorite_1.rect.height, HEIGHT - meteorite_1.rect.height
                )

            meteorite_2.rect.centerx -= speed * 4
            if meteorite_2.rect.centerx <= 0:
                meteorite_2.rect.centerx = WIDTH
                meteorite_2.rect.centery = randint(
                    meteorite_2.rect.height, HEIGHT - meteorite_2.rect.height
                )

            if pygame.sprite.collide_mask(player, meteorite_2):
                speed -= 1
                meteorite += 1
                score -= 25
                meteorite_2.rect.centerx = WIDTH
                meteorite_2.rect.centery = randint(
                    meteorite_2.rect.height, HEIGHT - meteorite_2.rect.height
                )

            meteorite_3.rect.centerx -= speed * 4
            if meteorite_3.rect.centerx <= 0:
                meteorite_3.rect.centerx = WIDTH
                meteorite_3.rect.centery = randint(
                    meteorite_3.rect.height, HEIGHT - meteorite_3.rect.height
                )

            if pygame.sprite.collide_mask(player, meteorite_3):
                speed -= 1
                meteorite += 1
                score -= 25
                meteorite_3.rect.centerx = WIDTH
                meteorite_3.rect.centery = randint(
                    meteorite_3.rect.height, HEIGHT - meteorite_3.rect.height
                )

            if meteorite_delay == 6:
                meteorite_1.image = choice(meteors)
                meteorite_2.image = choice(meteors)
                meteorite_3.image = choice(meteors)
                meteorite_delay -= 6
            if meteorite_delay < 6:
                meteorite_delay += 1

        if score <= -250:
            condition = 0
            break
        if score >= 100:
            condition = 1
            break

        if speed >= 6:
            speed = 6
        if speed <= 1:
            speed = 1

        if (
            expectation_x == player.rect.centerx
            and expectation_y == player.rect.centery
        ):
            player.image = Inaction

        grounds.draw(screen)
        sprites.draw(screen)

        counter = font_object.render(str(score), False, (255, 255, 255))
        screen.blit(counter, (10, 10))

        count_cake = font_object.render(str(cake), False, ("white"))
        screen.blit(count_cake, (WIDTH - 30, 10))

        clock.tick(120)
        pygame.display.update()

    screen.fill((20, 20, 20))

    if condition == 1:
        good_end.draw(screen)
    if condition == 0:
        bad_end.draw(screen)
    pygame.display.update()

    time.sleep(5)

    titles = [
        f"Ваш счёт составляет: {score}",
        "",
        f"Количество собранных тортиков: {cake}",
        "",
        f"Количество пойманных метеоритов: {meteorite}",
        "",
        "Главный геймплей-программист:",
        "- Дощинский Кирилл (Duo48)",
        "",
        "Главный геймдизайнер:",
        "- Дощинский Кирилл (Duo48)",
        "",
        "Главный 2D-художник и аниматор:",
        "- Дощинский Кирилл (Duo48)",
        "",
        "Главный звукорежиссёр:",
        "- Дощинский Кирилл (Duo48)",
        "",
        "Главный тестировщик:",
        "- Дощинский Кирилл (Duo48)",
        "",
        "Менеджер проекта:",
        "- Дощинский Кирилл (Duo48)",
        "",
        "Спасибо за прохождение!",
    ]

    ending.draw(screen)

    for line, titles_delay in zip(titles, range(400, 1100, 30)):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        title_output = next_object.render(line, False, (255, 255, 255))
        screen.blit(title_output, (400, titles_delay))
        clock.tick(2)
        pygame.display.update()

    time.sleep(3)
    pygame.quit()
    quit()
