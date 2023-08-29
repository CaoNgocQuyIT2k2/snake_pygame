import pygame as pg
import random
pg.init()

#cửa sổ game
Screen =pg.display.set_mode((400,400))

#đặt tiêu đề 
pg.display.set_caption('Snake Game')

# Khởi tạo biến mặc định
snake_part = 20 #thân rắn theo từng khúc 
x=y=200 #vị trí mặc định của rắn bằng 200px
x_change = y_change = 0 #vị trí thay đổi
body_snake = [] # để lưu thân rắn
length = 1 #thân rắn mặc định là 1
score = highScore = 0


# tạo điểm ăn cho rắn
food_x= random.randint(0,19)*snake_part
food_y= random.randint(0,19)*snake_part

#tạo tốc độ cho rắn
clock = pg.time.Clock()
speed = 3

#def Function
def check_col(): #kiểm tra va chạm
    if x<0 or  x > 400 or y<0 or y > 400 or (x,y) in body_snake[:-1]:
        return False
    return True

#hàm viết thông báo điểm, điểm cao nhất và chơi lại
def score_view():
    font = pg.font.Font(None,36)
    if gamePlay:
        score_txt = font.render(f'Score: {score}', True,(255,255,255))
        Screen.blit(score_txt,(0,0))
        hscore_txt = font.render(f'High Score: {highScore}', True,(255,255,255))
        Screen.blit(hscore_txt,(170,0))
    else:
        note_txt = font.render(f'Press space to play again', True,(255,255,255))
        Screen.blit(note_txt,(0,0))

#Phần xử lý game
gamePlay = True
while True:
    for event in pg.event.get():
        #thoát game
        if event.type ==pg.QUIT:
            pg.quit()
            quit
        #di chuyển
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
                gamePlay=True
    #Clear màn hình
    Screen.fill((0,0,0))
    score_view()
    if gamePlay:
        #cập nhật vị trí rắn
        x+= x_change
        y+= y_change

        #thêm thân rắn mới vào mình con rắn
        body_snake.append((x,y))

        #xóa thân rắn khi rắn di chuyển đi
        if len(body_snake) > length:
            del body_snake[0]

        #kiểm tra xem rắn ăn mồi được không
        if x==food_x and y == food_y:
            length+=1
            score +=1
            if score > highScore : highScore = score
            #random lại thức ăn
            food_x= random.randint(0,19)*snake_part
            food_y= random.randint(0,19)*snake_part
        
        #vẽ thân rắn
        for x,y in body_snake:
            pg.draw.rect(Screen,(255,255,255),(x,y,snake_part,snake_part))
        #vẽ thức ăn
        pg.draw.rect(Screen,(220,20,60),(food_x,food_y,snake_part,snake_part))
        gamePlay=check_col() #kiểm tra va chạm
        
        #cập nhật lại tốc độ
        clock.tick(speed)
    else:
        #khởi tạo lại game
        x=y=200
        x=y=200 #vị trí mặc định của rắn bằng 200px
        x_change = y_change = 0 #vị trí thay đổi
        body_snake = [] # để lưu thân rắn
        length = 1 #thân rắn mặc định là 1

    #cập nhật lại màn hình
    pg.display.update()
