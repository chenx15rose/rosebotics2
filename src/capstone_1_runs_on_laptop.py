"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and BERT.
"""
# ------------------------------------------------------------------------------
# DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this TODO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 2. With your instructor, discuss the "big picture" of laptop-robot
# TODO:    communication:
# TODO:      - One program runs on your LAPTOP.  It displays a GUI.  When the
# TODO:        user presses a button intended to make something happen on the
# TODO:        ROBOT, the LAPTOP program sends a message to its MQTT client
# TODO:        indicating what it wants the ROBOT to do, and the MQTT client
# TODO:        SENDS that message TO a program running on the ROBOT.
# TODO:
# TODO:      - Another program runs on the ROBOT. It stays in a loop, responding
# TODO:        to events on the ROBOT (like pressing buttons on the IR Beacon).
# TODO:        It also, in the background, listens for messages TO the ROBOT
# TODO:        FROM the program running on the LAPTOP.  When it hears such a
# TODO:        message, it calls the method in the DELAGATE object's class
# TODO:        that the message indicates, sending arguments per the message.
# TODO:
# TODO:  Once you understand the "big picture", delete this TODO (if you wish).
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 3. One team member: change the following in mqtt_remote_method_calls.py:
#                LEGO_NUMBER = 99
# TODO:    to use YOUR robot's number instead of 99.
# TODO:    Commit and push the change, then other team members Update Project.
# TODO:    Then delete this TODO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 4. Run this module.
# TODO:    Study its code until you understand how the GUI is set up.
# TODO:    Then delete this TODO.
# ------------------------------------------------------------------------------

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import time

def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()
    point = Point()
    #mqtt_client.send_message('beep_and_talk',['Hello.How are you?',200])

    while True:
        #setup_gui_difficult(root,mqtt_client)
        #setup_gui(root, mqtt_client)
        setup_gui_final(root,mqtt_client,point)
        root.mainloop()
        time.sleep(0.01)

    # --------------------------------------------------------------------------
    # TODO: 5. Add code above that constructs a   com.MqttClient   that will
    # TODO:    be used to send commands to the robot.  Connect it to this pc.
    # TODO:    Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------
def setup_gui_difficult(root_window,mqtt_client):
    defaults_speak_words = speak_words()
    frame = ttk.Frame(root_window, padding = 40)
    frame.grid()
    speak_string_box = ttk.Entry(frame)
    speak_button = ttk.Button(frame, text = "set strings")
    volume_box = ttk.Entry(frame)
    volume_button = ttk.Button(frame, text = "set volume")
    speak_string_box.grid()
    speak_button.grid()
    volume_box.grid()
    volume_button.grid()
    do_speak_button = ttk.Button(frame, text = "speak now")
    do_speak_button.grid()
    speak_button['command'] = (lambda : adjust_words(defaults_speak_words, speak_string_box.get()))
    volume_button['command'] = (lambda : adjust_volume(defaults_speak_words, int(volume_box.get())))
    do_speak_button['command'] = (lambda : mqtt_client.send_message('beep_and_talk',[defaults_speak_words.words,defaults_speak_words.volume]))
def adjust_words(speak_object,new_words):
    speak_object.words = new_words
def adjust_volume(speak_object,new_volume):
    speak_object.volume = new_volume
class speak_words(object):
    def __init__(self,volume = 100, words=''):
        self.volume = volume
        self.words = words
def setup_gui_final(root, mqtt_client,point):
    frame = ttk.Frame(root, padding = 30)
    frame.grid()

    canvas = tkinter.Canvas(frame,background = 'lightgray',height = 2000,width = 1000)
    canvas.grid()
    canvas.bind('<Button-1>', lambda event: left_mouse_click(event,point))

def left_mouse_click(event,point):
    if point.x == 0 and point.y == 0:
        pass
    else:
        canvas = event.widget
        canvas.create_line(event.x, event.y,point.x,point.y)
    point.x = event.x
    point.y = event.y

class Point(object):
    def __init__(self):
        self.x = 0
        self.y = 0

def setup_gui(root_window, mqtt_client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=10)
    frame.grid()

    speed_entry_box = ttk.Entry(frame)
    go_forward_button = ttk.Button(frame, text="Go forward")

    speed_entry_box.grid()
    go_forward_button.grid()

    go_forward_button['command'] = \
        lambda: handle_go_forward(speed_entry_box, mqtt_client)


def handle_go_forward(entry_box, mqtt_client):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
    # --------------------------------------------------------------------------
    # TODO: 6. This function needs the entry box in which the user enters
    # TODO:    the speed at which the robot should move.  Make the 2 changes
    # TODO:    necessary for the entry_box constructed in  setup_gui
    # TODO:    to make its way to this function.  When done, delete this TODO.
    # --------------------------------------------------------------------------
    speed = entry_box.get()
    print("Sending 'go_forward' to the robot, with a speed", speed)
    mqtt_client.send_message("go_forward",[speed])

    # --------------------------------------------------------------------------
    # TODO: 7. For this function to tell the robot what to do, it needs
    # TODO:    the MQTT client constructed in main.  Make the 4 changes
    # TODO:    necessary for that object to make its way to this function.
    # TODO:    When done, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 8. Add the single line of code needed to get the string that is
    # TODO:    currently in the entry box.
    # TODO:
    # TODO:    Then add the single line of code needed to "call" a method on the
    # TODO:    LISTENER that runs on the ROBOT, where that LISTENER is the
    # TODO:    "delegate" object that is constructed when the ROBOT's code
    # TODO:    runs on the ROBOT.  Send to the delegate the speed to use
    # TODO:    plus a method name that you will implement in the DELEGATE's
    # TODO:    class in the module that runs on the ROBOT.
    # TODO:
    # TODO:    Test by using a PRINT statement.  When done, delete this TODO.
    # --------------------------------------------------------------------------


main()
