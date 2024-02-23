import machine
import utime
from App import App

MISC = machine.Pin(7, machine.Pin.IN)
OK = machine.Pin(8, machine.Pin.IN)
STOP = machine.Pin(9, machine.Pin.IN)

app = App()

# Initial loop to get past introduction screen
while True:
    if OK.value() == 1:
        break

# Loops The Entire Program
while True:
    # Select Time Split
    app.ask_time()
    utime.sleep(1)
    while True:
        if MISC.value() == 1:
            app.select_time("1")
            break
        elif OK.value() == 1:
            app.select_time("2")
            break
        elif STOP.value() == 1:
            app.select_time("3")
            break
        else:
            app.ask_time()

    # Main Loop
    for i in range(0,2):
        work = True
        break_time = True
        paused = False
        
        if not i:
            app.pre_countdown()
        else:
            app.cntdwn("w")
        while work:
            if STOP.value() == 1:
                app.pause("w")
                paused = True
            elif paused:
                if OK.value() == 1:
                    paused = False
                else:
                    app.pause('w')
            elif not paused:
                work = app.work()
        
        app.cntdwn("b")
        while break_time:
            if STOP.value() == 1:
                app.pause("b")
                paused = True
            elif paused:
                if OK.value() == 1:
                    paused = False
                else:
                    app.pause('b')
            elif not paused:
                break_time = app.brk()
                
        app.reset_times()
    
    app.end()
