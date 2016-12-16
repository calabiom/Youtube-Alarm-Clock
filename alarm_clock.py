# Alarm Clock

## This is a simple program that takes input in the form of
##  "(hr) (min) (/AM/PM)" (i.e. "8 20 PM")
## When the desired time rings, the program reads from a textfile full of random YT videos and opens them up in the user's browser.

import time
import datetime
import webbrowser
import random

file_to_open = "alarm_clock_vid_test.txt"

class AlarmClockError(Exception):
    pass

def error_check_inputs(input_time: str):
    ## error-checking here
    error_check_time_str = input_time.split()
    
    if len(error_check_time_str) != 3:
        raise AlarmClockError("The input for the desired wake-up time must be \
                       in the format of '(hr) (min) (AM/PM)'. For example, \
                       the user-input, '8 51 AM' (meaning 8:51 AM), is acceptable")
    else:
        if (int(error_check_time_str[0]) < 0) or (int(error_check_time_str[0]) > 12):
            raise AlarmClockError("The input for the hours must be a positive integer \
                                 between 0 and 12 hours")
        
        if (int(error_check_time_str[1]) < 0) or (int(error_check_time_str[1]) > 59):
            raise AlarmClockError("The input for the minutes must be a positive integer \
                                 between 0 and 59 minutes")
            
        if (len(error_check_time_str[1]) == 1):
            raise AlarmClockError("The input for a single-digit minute should have a zero (0) \
                                   in front of it (i.e. 8:08 AM --> 8 08 AM)")
        
        if error_check_time_str[2] not in ["AM", "PM"]:
            raise AlarmClockError("The input for the Ante/Post Meridiem must be \
                           either 'AM' or 'PM' (must be capitalized)")
    return
            
def set_alarm() -> str:
    '''Gathers inputs in the form of "<hr> <min> <AM/PM>"'''
    time_str = input("What time would like to wake up? ")

    error_check_inputs(time_str)
    
    return time_str

def open_file_if_alarm_rings():
    '''When the desired time for the alarm occurs, this function
       opens a text file and plays the video on the browser'''
    open_file = open(file_to_open, "r")
    
    try:
        num_of_lines = sum(1 for line in open_file)
        line_num = random.randrange(num_of_lines)
        
        open_file.seek(0)
        total_lines = [line.strip() for line in open_file]
        selected_video_link = total_lines[line_num]

        webbrowser.open_new_tab(selected_video_link)
    except:
        pass

    finally:
        open_file.close()

if __name__ == "__main__":
    desired_wake_time = set_alarm().split()
    
    while desired_wake_time != time.strftime("%I:%M:%p").split(':'):
        print("The time is currently: {}".format(time.strftime("%I:%M:%S:%p")))
        time.sleep(1)
        
        if desired_wake_time == time.strftime("%I:%M:%p").split(':'):
            print("WAKE UP! The time is {}.".format(time.strftime("%I:%M:%p")))
            open_file_if_alarm_rings()
            break
        
    print("Goodbye :)")

