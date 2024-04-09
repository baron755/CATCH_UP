from pygame import *
FPS = 60
#створи вікно гри
window = display.set_mode((700, 500))
display.set_caption("Догонялки")
clock = time.Clock()
FPS = 60
#задай фон сцени
background = transform.scale(image.load("background.png"), (700, 500))
#створи 2 спрайти та розмісти їх на сцені
window.blit(background, (0, 0))
#оброби подію «клік за кнопкою "Закрити вікно"»

game = True

sprite1 = transform.scale(image.load("sprite1.png"), (100, 100))
sprite2 = transform.scale(image.load("sprite2.png"), (100, 100))

x1 = 500
y1 = 200
x2 = 100
y2 = 200
speed = 5

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    
    keys_pressed = key.get_pressed()
    
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += speed
        
    
    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed
    if keys_pressed[K_d] and x2 < 595:
        x2 += speed
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 395:
        y2 += speed
    
    display.update()
    clock.tick(FPS)
    
    