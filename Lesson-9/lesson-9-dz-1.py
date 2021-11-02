import time

class TrafficLights:
    __color = ''
        
    def running(self):
        color_text = ['red', 'yellow', 'green']
        color_value = [31, 33, 32]
        red_time = 7
        yellow_time = 2
        green_time = 5
        
        while (True):
            color_regime = [red_time, yellow_time, green_time]
            for index in range(0,3):
                self.__color = color_text[index]
                _text ="\033[{}m{}".format(color_value[index], self.__color)
                #print(f'\033[31m\033[43m{self.__color}')
                print(_text)
                time.sleep(color_regime[index])
                
                
tr_lights = TrafficLights()
tr_lights.running()