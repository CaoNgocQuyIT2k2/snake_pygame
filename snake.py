import pygame as pg
import random
pg.init()

# Cửa sổ game
Screen = pg.display.set_mode((400, 400))

# Đặt tiêu đề
pg.display.set_caption('Game bác sĩ săn covid')

# Khởi tạo biến mặc định
snake_part = 20  # thân rắn theo từng khúc
x = y = 200  # vị trí mặc định của rắn bằng 200px
x_change = y_change = 0  # vị trí thay đổi
body_snake = []  # để lưu thân rắn
length = 1  # thân rắn mặc định là 1
score = highScore = 0
is_eating_sound_playing = False


snake_img = pg.image.load('head.jpg')
snake_img = pg.transform.scale(snake_img, (snake_part, snake_part))
body_img = pg.image.load('body.jpg')
body_img = pg.transform.scale(body_img, (snake_part, snake_part))
food_img = pg.image.load('covid.png')
food_img = pg.transform.scale(food_img, (snake_part, snake_part))

eat_sound = pg.mixer.Sound('EatSound_CC0_by_EugeneLoza.ogg')

# Tạo điểm ăn cho rắn
food_x = random.randint(0, 19) * snake_part
food_y = random.randint(0, 19) * snake_part

# Tạo tốc độ cho rắn
clock = pg.time.Clock()
speed = 3

# Hàm kiểm tra va chạm
def check_col():
    if x < 0 or x > 400 or y < 0 or y > 400 or (x, y) in body_snake[:-1]:
        return False
    return True

# Hàm viết thông báo điểm, điểm cao nhất và chơi lại
def score_view():
    font = pg.font.Font(None, 36)
    if gamePlay:
        score_txt = font.render(f'Score: {score}', True, (255, 255, 255))
        Screen.blit(score_txt, (0, 0))
        hscore_txt = font.render(f'High Score: {highScore}', True, (255, 255, 255))
        Screen.blit(hscore_txt, (170, 0))
    else:
        note_txt = font.render(f'Press space to play again', True, (255, 255, 255))
        Screen.blit(note_txt, (0, 0))

# Phần xử lý game
gamePlay = True
while True:
    for event in pg.event.get():
        # Thoát game
        if event.type == pg.QUIT:
            pg.quit()
            quit
        # Di chuyển
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x_change -= snake_part
                y_change = 0
            elif event.key == pg.K_RIGHT:
                x_change = snake_part
                y_change = 0
            elif event.key == pg.K_UP:
                x_change = 0
                y_change -= snake_part
            elif event.key == pg.K_DOWN:
                x_change = 0
                y_change = snake_part
            elif event.key == pg.K_SPACE:
                gamePlay = True

    # Clear màn hình
    Screen.fill((0, 0, 0))
    # Sử dụng hình nền
    bg_img = pg.image.load('bg.png')
    bg_img = pg.transform.scale(bg_img, (400, 400))
    Screen.blit(bg_img, (0, 0))

    score_view()
    if gamePlay:
        # Cập nhật vị trí rắn
        x += x_change
        y += y_change

        # Thêm thân rắn mới vào mình con rắn
        body_snake.append((x, y))

        # Xóa thân rắn khi rắn di chuyển đi
        if len(body_snake) > length:
            del body_snake[0]

        # Kiểm tra xem rắn ăn mồi được không
        if x == food_x and y == food_y:
            length += 1
            score += 1
            if score > highScore: highScore = score
            # Random lại thức ăn
            food_x = random.randint(1, 19) * snake_part
            food_y = random.randint(1, 19) * snake_part

            eat_sound.play()
        # Vẽ thân rắn
        for bx, by in body_snake:
            Screen.blit(body_img, (bx, by))
        # Vẽ đầu rắn
        Screen.blit(snake_img, (x, y))
        # Vẽ thức ăn
        Screen.blit(food_img, (food_x, food_y))
        gamePlay = check_col()  # Kiểm tra va chạm

        # Cập nhật lại tốc độ
        clock.tick(speed)
    else:
        # Khởi tạo lại game
        x = y = 200
        x = y = 200  # Vị trí mặc định của rắn bằng 200px
        x_change = y_change = 0  # Vị trí thay đổi
        body_snake = []  # Để lưu thân rắn
        length = 1  # Thân rắn mặc định là 1

    # Cập nhật lại màn hình
    pg.display.update()
