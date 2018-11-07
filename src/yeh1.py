"""
  Capstone Project.  Code written by Hengqi Ye(Luis).
  Fall term, 2018-2019.
"""

import rosebotics_even_newer as rb
import time
from ev3dev import ev3
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls

def main():
    """ Runs YOUR specific part of the project """
    #test_wait_until_pressed()
    #test_wait_until_released()
    #test_color_stop_by(5)
    test_infrared_beacon()
    # test_beacon1()


def test_wait_until_pressed():
    robot = rb.Snatch3rRobot()
    while True:
        robot.drive_system.start_moving(50, 50)
        robot.touch_sensor.wait_until_pressed()
        robot.drive_system.stop_moving()
        robot.touch_sensor.wait_until_released()

def test_wait_until_released():
    robot = rb.Snatch3rRobot()
    robot.touch_sensor.wait_until_pressed()
    robot.touch_sensor.wait_until_released()
    robot.drive_system.start_moving(50, 50)
def test_color_stop_by(color_number):
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(50, 50)
    robot.color_sensor.wait_until_color_is(color_number)
    robot.drive_system.stop_moving()
    print(robot.color_sensor.get_color())

#def test_beacon1():
    #robot = rb.Snatch3rRobot
    #print("Beacon sensor:",
    #    robot.beacon_button_sensor.is_beacon_button_pressed())
    #if robot.beacon_button_sensor.is_beacon_button_pressed() == True:
    #    robot.drive_system.spin_in_place_degrees(180, -100)
    #   robot.drive_system.go_straight_inches(30, 100)

def test_beacon():
    robot = rb.Snatch3rRobot()
    robot.drive_system.spin_in_place_degrees(180, -100)
    robot.drive_system.go_straight_inches(30, 100)



def test_infrared_beacon():
    window = tkinter.Tk()

    frame = ttk.Frame(window, padding=50)
    frame.grid()

    client = mqtt_remote_method_calls.MqttClient()
    client.connect_to_ev3()

    button = ttk.Button(frame, text='Infrared Beacon')
    button['command'] = lambda: test_beacon()
    button.grid()

    window.mainloop()













main()
