from lcd1602 import LCD
import machine
import utime

class App:
    lcd = LCD()
    work_time = 0
    break_time = 0
    
    uc_work = 0
    uc_break = 0


    def __init__(self):
        self.lcd.clear()
        self.lcd.message("Pomodoro Timer\nPress OK")
        
    
    def ask_time(self):
        self.lcd.clear()
        self.lcd.message("Select Desired\nTime Interval")
        utime.sleep(2)
        self.lcd.clear()
        self.lcd.message("MISC button:\n1min / 1min")
        utime.sleep(2.5)
        self.lcd.clear()
        self.lcd.message("OK button:\n35min / 10min")
        utime.sleep(2.5)
        self.lcd.clear()
        self.lcd.message("STOP button:\n45min / 15min")
        utime.sleep(2.5)
        self.lcd.clear()
        self.lcd.message("WAIT for Option\nRefresh. Or")
        utime.sleep(2.5)
        self.lcd.clear()
        self.lcd.message("HOLD Selection\nButton Now")
        utime.sleep(2)
        

        
        
    def select_time(self, selection):
        if selection == "1":
            self.work_time = 1 * 60
            self.break_time = 1 * 60
        elif selection == "2":
            self.work_time = 35 * 60
            self.break_time = 10 * 60
        elif selection == "3":
            self.work_time = 45 * 60
            self.break_time = 15 * 60
        self.uc_work = self.work_time
        self.uc_break = self.break_time
            
            
    def pre_countdown(self):
        for i in range(5,0,-1):
            self.lcd.clear()
            self.lcd.message(f"Beginning in...\n{i} ...")
            utime.sleep(1)
        self.lcd.clear()
        
        
    def cntdwn(self, wb = "Next Session"):
        if wb == 'w':
            wb = "Work Starts"
        elif wb == 'b':
            wb = "Break Time"
        for i in range(5,0,-1):
            self.lcd.clear()
            self.lcd.message(f"{wb} in...\n{i} ...")
            utime.sleep(1)
        self.lcd.clear()
            
            
    def work(self):
        mins, seconds = divmod(self.work_time, 60)
        self.lcd.clear()
        self.lcd.message('WORK:\n{:02d}:{:02d}'.format(int(mins),int(seconds)))
        utime.sleep(1)
        self.work_time -= 1
        if self.work_time <= 0:
            return False
        return True
        
    def brk(self):
        mins, seconds = divmod(self.break_time, 60)
        self.lcd.clear()
        self.lcd.message('BREAK:\n{:02d}:{:02d}'.format(int(mins),int(seconds)))
        utime.sleep(1)
        self.break_time -= 1
        if self.break_time <= 0:
            return False
        return True
        
        
    def reset_times(self):
        self.work_time = self.uc_work
        self.break_time = self.uc_break
        
        
    def pause(self, state):
        self.lcd.clear()
        if state == "w":
            mins, seconds = divmod(self.work_time, 60)
            self.lcd.message('Paused at\nWORK: {:02d}:{:02d}'.format(int(mins),int(seconds)))
            utime.sleep(1)
        elif state == "b":
            mins, seconds = divmod(self.break_time, 60)
            self.lcd.message('Paused at\nBREAK: {:02d}:{:02d}'.format(int(mins),int(seconds)))
            utime.sleep(1)
            
    
    def end(self):
        self.lcd.clear()
        self.lcd.message("Session Done!\nRestarting")
        utime.sleep(4)
        self.lcd.clear()
            
        