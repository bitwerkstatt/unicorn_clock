import time
import machine
from picounicorn import PicoUnicorn

MODE_SETTIME = 1
MODE_RUNCLOCK = 2

display = PicoUnicorn()
clock = machine.RTC()

w = display.get_width()
h = display.get_height()

mode = MODE_RUNCLOCK

def clear_display():
    for x in range(w):
        for y in range(w):
            display.set_pixel(w, h, 0,0,0)

def draw_lamp(xs, ys, w, h, r, g, b):
    for x in range(xs, xs+w):
        for y in range(ys, ys+h):
            display.set_pixel(x, y, r, g, b)

def render_time(hours, minutes, seconds):
    # Top hour lamps
    for i in range(4):
        if i < hours//5:
            draw_lamp(i*4,1,3,1,255,153,0)
        else:
            draw_lamp(i*4,1,3,1,20,20,20)
    
    # Bottom hour lamps
    for i in range(4):
        if i < hours%5:
            draw_lamp(i*4,2,3,1,255,153,102)
        else:
            draw_lamp(i*4,2,3,1,20,20,20)
    
    
    # Top minute lamps
    for i in range(11):
        if i < minutes//5:
            if i>0 and (i+1)%3 == 0:
                draw_lamp(i,4,1,1,153,153,255)
            else:
                draw_lamp(i,4,1,1,58,75,126)                
        else:
            draw_lamp(i,4,1,1,20,20,20)
    
    # Bottom minute lamps
    # Bottom hour lamps
    for i in range(4):
        if i < hours%5:
            draw_lamp(i*4,5,3,1,0,0,255)
        else:
            draw_lamp(i*4,5,3,1,20,20,20)
            
    # Seconds blinker
    for i in range(14):
        if seconds % 2:
            draw_lamp(1+i,3,1,1,136,34,17)
        else:
            draw_lamp(1+i,3,1,1,20,20,0)


def set_time(hours, minutes):
    clock.datetime(2023,7,15,hours, minutes, 0,0)

while True:
    if mode == MODE_SETTIME:
        print(clock.datetime(), w, h)
    else:
        current_time = clock.datetime()
        render_time(current_time[4], current_time[5], current_time[6])
