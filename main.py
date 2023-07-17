import time
import machine
from picounicorn import PicoUnicorn

MODE_SETTIME = 1
MODE_RUNCLOCK = 2

BUTTON_IDLE_TIME = 250

unicorn = PicoUnicorn() 
clock = machine.RTC()

handling_a_ts = time.ticks_ms()
handling_b_ts = time.ticks_ms()
handling_x_ts = time.ticks_ms()
handling_y_ts = time.ticks_ms()

mode = MODE_RUNCLOCK
hours_to_set = 0
minutes_to_set = 0

def clear_unicorn():
    for x in range(w):
        for y in range(w):
            unicorn.set_pixel(w, h, 0,0,0)

def draw_lamp(xs, ys, w, h, r, g, b):
    for x in range(xs, xs+w):
        for y in range(ys, ys+h):
            unicorn.set_pixel(x, y, r, g, b)

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
                draw_lamp(i,4,1,1,0,17,238)
            else:
                draw_lamp(i,4,1,1,58,75,126)                
        else:
            draw_lamp(i,4,1,1,20,20,20)
    
    # Bottom minute lamps
    for i in range(4):
        if i < minutes%5:
            draw_lamp(i*4,5,3,1,51,102,255)
        else:
            draw_lamp(i*4,5,3,1,20,20,20)
            
    # Seconds blinker
    for i in range(14):
        if seconds == 255: # Hack for settime
            draw_lamp(1+i,3,1,1,0,0,255)
        else:
            if seconds % 2:
                draw_lamp(1+i,3,1,1,204,102,153)
            else:
                draw_lamp(1+i,3,1,1,20,20,20)


def set_time(hours, minutes):
    clock.datetime(2023,7,15,hours, minutes, 0,0)

mode = MODE_RUNCLOCK

while True:
    current_tick = time.ticks_ms()
    handling_button_a = unicorn.is_pressed(unicorn.BUTTON_A) and not (current_tick - handling_a_ts) < BUTTON_IDLE_TIME 
    handling_button_b = unicorn.is_pressed(unicorn.BUTTON_B) and not (current_tick - handling_b_ts) < BUTTON_IDLE_TIME
    handling_button_x = unicorn.is_pressed(unicorn.BUTTON_X) and not (current_tick - handling_x_ts) < BUTTON_IDLE_TIME
    handling_button_y = unicorn.is_pressed(unicorn.BUTTON_Y) and not (current_tick - handling_y_ts) < BUTTON_IDLE_TIME
    
    if handling_button_x:
        if mode == MODE_SETTIME:
            clock.datetime((2023,7,15,0,hours_to_set, minutes_to_set,0,0))
            mode = MODE_RUNCLOCK
        else:
            hours_to_set = clock.datetime()[4]
            minutes_to_set = clock.datetime()[5]
            mode = MODE_SETTIME
        handling_x_ts = current_tick
        
    if handling_button_y:
        print("Nothing ever happens...")
        handling_y_ts = current_tick
              
    if mode == MODE_SETTIME:
                
        if handling_button_a:
            hours_to_set = (hours_to_set+1)%24
            handling_a_ts = current_tick 
            
        if handling_button_b:
            minutes_to_set = (minutes_to_set+1)%60
            handling_b_ts = current_tick
            
        render_time(hours_to_set, minutes_to_set, 255)
        
    else:
        current_time = clock.datetime()
        render_time(current_time[4], current_time[5], current_time[6])
