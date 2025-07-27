import pygame
import sys
from pygame.locals import *
import time
import datetime



def main():
    pygame.init()
    font = pygame.font.SysFont("Arial", 36)
    displaysurf = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Eh, it\'s about...')

    minute_color = (2, 38, 129) #my birthday :-)
    descriptor_color =  (9, 22, 119) #my wife's birthday :-)
    hour_color = (5, 20, 34) #our anniversary :-) :-)

    minute_modifier_list = ["just", "five", "ten", "quarter", "twenty", "twenty five", "half"]
    descriptor_modifier_list = ["about", "after", "past", "to"]
    while True:
        time_of_day = datetime.now()
        current_time = time_of_day.strftime("%H:%M:%S")
        current_hour = int(time_of_day.strftime("%H"))
        current_minute = int(time_of_day.strftime("%M"))
        match current_minute: #58, 59, 0, 1, 2
                                #3 - 27
                                #28 - 58
            case 58 | 59 | 0 | 1 | 2:
                print("something")
                descriptor_modifier = descriptor_modifier_list[0] #about
                minute_modifier = "something"
                #insert code as necessary to adjust the hour value
            case num if 3 <= num <= 27: 
                print("something")
                descriptor_modifier = descriptor_modifier_list[1] #after
                if 3 <= num <= 7:
                    minute_modifier = minute_modifier_list[1] #5
                elif 8 <= num <= 12:
                    minute_modifier = minute_modifier_list[2] #10
                elif 13 <= num <= 17:
                    minute_modifier = minute_modifier_list[3] #quarter
                elif 18 <= num <= 22:
                    minute_modifier = minute_modifier_list[4] #20
                else:
                    minute_modifier = minute_modifier_list[5] #25
                #insert code as necessary to adjust the hour value
            case num if 28 <= num < 58:
                print("something")
                descriptor_modifier = descriptor_modifier_list[3] #to
                if 28 <= num <= 32:
                    descriptor_modifier = descriptor_modifier_list[2] #past - this is the only case where past will be used
                    minute_modifier = minute_modifier_list[6] #half
                elif 33 <= num <= 37:
                    minute_modifier = minute_modifier_list[5] #25
                    if current_hour + 1 == 24:
                        current_hour = 0
                    else:
                        current_hour = current_hour + 1
                elif 38 <= num <= 42:
                    minute_modifier = minute_modifier_list[4] #20
                    if current_hour + 1 == 24:
                        current_hour = 0
                    else:
                        current_hour = current_hour + 1
                elif 43 <= num <= 47:
                    minute_modifier = minute_modifier_list[3] #15
                    if current_hour + 1 == 24:
                        current_hour = 0
                    else:
                        current_hour = current_hour + 1
                elif 48 <= num <= 52:
                    minute_modifier = minute_modifier_list[2] #10
                    if current_hour + 1 == 24:
                        current_hour = 0
                    else:
                        current_hour = current_hour + 1
                elif 53 <= num <= 57:
                    minute_modifier = minute_modifier_list[1] #5
                    if current_hour + 1 == 24:
                        current_hour = 0
                    else:
                        current_hour = current_hour + 1

        match current_hour:
            case 1 | 13:
                hour_text = "one"
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
            case 2 | 14:
                hour_text = "two"
                print("something else")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
            case 3 | 15:
                hour_text = "three"
                print("something else")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
            case 4 | 16:
                hour_text = "four"
                print("something else")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
            case 5 | 17:
                hour_text = "five"
                print("something else")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
            case 6 | 18:
                hour_text = "six"
                print("something else")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
            case 7 | 19:
                hour_text = "seven"
                print("something else")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
            case 8 | 20:
                hour_text = "eight"
                print("something else")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
            case 9 | 21:
                hour_text = "nine"
                print("something else")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
            case 10 | 22:
                hour_text = "ten"
                print("something else")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
            case 11 | 23:
                hour_text = "eleven"
                print("something else")
            case 12 | 0:
                if current_hour == 12:
                    hour_text = "noon"
                else:
                    hour_text = "midnight"
                print("something else")
                #insert code to correct for if it's pm or am, if it's close to the next hour, etc
                #insert code as necessary to adjust the hour value

        #put code here to draw the text to the screen
        #three calls to font.render, three calls to text.surface.get_rect
        #screen.fill
        #screen.blit (3x)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        time.sleep(60)



if __name__ == "__main__":
    main()
