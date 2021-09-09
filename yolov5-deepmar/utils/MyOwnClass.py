from time import monotonic


class Swimmer:
    def __init__(self): 
        self.av_speed = 0  #Средняя скорость
        self.prev_av_speed = 0 # Предыдущая средняя скорость
        self.mark1 = 0 # Временная метка 1
        self.mark2 = 0 # Временная метка 2
        self.check1 = False # Проверка на пересечении линии 1
        self.check2 = False # Проверка на пересечении линии 1



    def speed_measure(self,mark1,mark2):
        if self.prev_av_speed != 0:
            self.av_speed = ((25/(abs(mark1-mark2)))+ self.prev_av_speed)/2
            self.prev_av_speed = self.av_speed
            return self.av_speed
        else:
            self.av_speed = 25/(abs(mark1-mark2))    
            self.prev_av_speed = self.av_speed
            return self.av_speed



swimmer1 = Swimmer()
print(swimmer1.av_speed)