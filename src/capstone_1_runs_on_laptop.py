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


import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import time
import math as mt

def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()
    root.title('coal miner')
    delegate =Delegate()
    mqtt_client = com.MqttClient(delegate)
    mqtt_client.connect_to_ev3()


    while True:
        #setup_gui_difficult(root,mqtt_client)
        #setup_gui(root, mqtt_client)
        setup_gui_final(root,mqtt_client)
        root.mainloop()
        time.sleep(0.01)

    # --------------------------------------------------------------------------
    # TODO: 5. Add code above that constructs a   com.MqttClient   that will
    # TODO:    be used to send commands to the robot.  Connect it to this pc.
    # TODO:    Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------
class Delegate(object):
    def __init__(self):
        self.mqtt_client = None
        self.distance = 0
    @staticmethod
    def set_distance(distance):
        print(distance)
        if distance > 800:
            print('This mine is too far away from station')
        else:
            print('This mine is near to the station')
class Speed(object):
    def __init__(self):
        self.left = 50
        self.right = 50
def setup_gui_difficult(root_window,mqtt_client):
    frame = ttk.Frame(root_window, padding = 40)
    frame.grid()
    do_speak_button = ttk.Button(frame, text = "speak now")
    do_speak_button.grid()
    do_speak_button['command'] = (lambda : mqtt_client.send_message('beep_and_talk'))


def setup_gui_final(root, mqtt_client):
    frame = ttk.Frame(root, padding = 30)
    frame.grid()
    speed1 = Speed()

    button1 = ttk.Button(frame, text= 'up')
    button1.grid(row = 0, column =1)
    button2 = ttk.Button(frame, text = 'down')
    button2.grid(row = 1, column = 1)
    button3 = ttk.Button(frame, text = 'left')
    button3.grid(row = 1, column = 0)
    button4 = ttk.Button(frame, text = 'right')
    button4.grid(row = 1, column = 2)
    entry = ttk.Entry(frame, text = 'down')
    entry.grid(row = 2, column =1)
    button5 = ttk.Button(frame, text = 'send initial velocity to ev3')
    button5.grid(row =3, column = 1)
    button1['command'] = (lambda : adjust_speed_up(speed1,mqtt_client))
    button2['command'] = (lambda : adjust_speed_down(speed1,mqtt_client))
    button3['command'] = (lambda : adjust_speed_left(speed1,mqtt_client))
    button4['command'] = (lambda : adjust_speed_right(speed1,mqtt_client))
    button5['command'] = (lambda : set_speed(entry,speed1,mqtt_client))
    speak_string_box = ttk.Entry(frame)
    speak_button = ttk.Button(frame, text="set strings")
    volume_box = ttk.Entry(frame)
    volume_button = ttk.Button(frame, text="set volume")
    speak_string_box.grid(column = 1)
    speak_button.grid(column = 1)
    volume_box.grid(column = 1)
    volume_button.grid(column = 1)
    volume_button['command'] = (lambda : mqtt_client.send_message('set_volume',[int(volume_box.get())]))
    speak_button['command'] = (lambda : mqtt_client.send_message('set_words',[speak_string_box.get()]))


def adjust_speed_up(speed, mqtt_client):
    speed.left += 10
    speed.right += 10

    mqtt_client.send_message('final_go', [speed.left, speed.right])
def adjust_speed_down(speed, mqtt_client):
    speed.left = speed.left-10
    speed.right = speed.right-10
    mqtt_client.send_message('final_go', [speed.left, speed.right])
def adjust_speed_left(speed, mqtt_client):
    speed.left = speed.left-5
    speed.right = speed.right+5

    mqtt_client.send_message('final_go', [speed.left, speed.right])
def adjust_speed_right(speed, mqtt_client):
    speed.left = speed.left +5
    speed.right = speed.right -5
    mqtt_client.send_message('final_go', [speed.left,speed.right])
def set_speed(entry_box,speed,mqtt_client):
    inispeed = int(entry_box.get())
    speed.left = inispeed
    speed.right = inispeed
    mqtt_client.send_message('final_go', [speed.left, speed.right])


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

    speed = entry_box.get()
    print("Sending 'go_forward' to the robot, with a speed", speed)
    mqtt_client.send_message("go_forward",[speed])


main()
