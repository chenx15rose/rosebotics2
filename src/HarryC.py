"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
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
    test_go_straight_inches(30,-100)
    test_spin(360,-100)
    test_turn(180,-100)
    #test_camera_beep()
    #test_Brick_Button()
    #test()
    test_beacon()

def test_go_straight_inches(inch,speed):
    robot = rb.Snatch3rRobot()
    robot.drive_system.go_straight_inches(inch,duty_cycle_percent=speed)

def test_spin(degree,dutypercent):
    robot = rb.Snatch3rRobot()
    robot.drive_system.spin_in_place_degrees(degree,dutypercent)

def test_turn(degree,dutypercent):
    robot = rb.Snatch3rRobot()
    robot.drive_system.turn_degrees(degree,dutypercent)


def test_camera_beep():
    robot = rb.Snatch3rRobot()
    while True:
        if robot.camera.get_biggest_blob().get_area()<=1000 and robot.camera.get_biggest_blob().get_area()>0:
            ev3.Sound.beep()
            print(robot.camera.get_biggest_blob().get_area())
            time.sleep(0.01)

def pass_method_to_ev3():
    client = mqtt_remote_method_calls.MqttClient()
    client.connect_to_ev3()
    time.sleep(1)
    client.send_message("Brick_Button_method")

def test_Brick_Button():
    window = tkinter.Tk()
    frame = ttk.Frame(window,padding=200)
    frame.grid()
    button = ttk.Button(frame,text='Brick Button')
    button['command']=lambda: pass_method_to_ev3()
    button.grid()
    window.mainloop()

def test_beacon():
        robot = rb.Snatch3rRobot()
        while True:
            print(robot.beacon_sensor.get_heading_and_distance_to_beacon())
            time.sleep(0.5)



main()
