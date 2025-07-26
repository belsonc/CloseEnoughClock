import pygame
import sys
from pygame.locals import *
import time
import datetime
    

def main():
    pygame.init()
    displaysurf = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Eh, it\'s about...')
    minute_color = (2, 38, 129)
    range_color =  (9, 22, 119)
    hour_color = (5, 20, 34)
    while True:
        time_of_day = datetime.now()
        current_time = time_of_day.strftime("%H:%M:%S")
        current_hour = int(time_of_day.strftime("%H"))
        current_minute = int(time_of_day.strftime("%M"))
        match current_hour:
            case 1 | 13:
                print("something")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
            case 2 | 14:
                print("something else")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
            case 3 | 15:
                print("something else")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
            case 4 | 16:
                print("something else")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
            case 5 | 17:
                print("something else")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
            case 6 | 18:
                print("something else")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
            case 7 | 19:
                print("something else")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
            case 8 | 20:
                print("something else")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
            case 9 | 21:
                print("something else")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
            case 10 | 22:
                print("something else")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
            case 11 | 23:
                print("something else")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
        match current_minute:
            case 3 | 4 | 5 | 6:
                print("something")
                minute_modifier = "something"
                range_modifier = "something"
            case 3 | 4 | 5 | 6:
                print("something")
                minute_modifier = "something"
                range_modifier = "something"
            case 3 | 4 | 5 | 6:
                print("something")
                minute_modifier = "something"
                range_modifier = "something"
            case 3 | 4 | 5 | 6:
                print("something")
                minute_modifier = "something"
                range_modifier = "something"
            case 3 | 4 | 5 | 6:
                print("something")
                minute_modifier = "something"
                range_modifier = "something"
            case 3 | 4 | 5 | 6:
                print("something")
                minute_modifier = "something"
                range_modifier = "something"
            case 3 | 4 | 5 | 6:
                print("something")
                minute_modifier = "something"
                range_modifier = "something"
            case 3 | 4 | 5 | 6:
                print("something")
                minute_modifier = "something"
                range_modifier = "something"
            case 3 | 4 | 5 | 6:
                print("something")
                minute_modifier = "something"
                range_modifier = "something"
            case 3 | 4 | 5 | 6:
                print("something")
                minute_modifier = "something"
                range_modifier = "something"
            case 3 | 4 | 5 | 6:
                print("something")
                minute_modifier = "something"
                range_modifier = "something"
            case 3 | 4 | 5 | 6:
                print("something")
                minute_modifier = "something"
                range_modifier = "something"
            case 3 | 4 | 5 | 6:
                print("something")
                minute_modifier = "something"
                range_modifier = "something"
            case 3 | 4 | 5 | 6:
                print("something")
                minute_modifier = "something"
                range_modifier = "something"
        #put code here to draw the text to the screen

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        time.sleep(60)



if __name__ == "__main__":
    main()
