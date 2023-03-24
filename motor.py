class Motor:
    def __init__(self):
        self.speed= 0.5

    def set_speed(self,speed):
        speed = max(-1,speed) #helps reset the speed to -1
        speed = min(1, speed) #helps reset the speed to 1
        speed = speed^3 #making a deadzone
        self.speed = speed

    def speed_up(self,speed):
        self.speed= speed*2

    def slow_down(self,speed):
        self.speed= speed/2

if __name__=="__main__":
    x = Motor()
    x.set_speed(0.5)
