"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and BERT.
"""
# ------------------------------------------------------------------------------
# DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this TODO.
# ------------------------------------------------------------------------------



import rosebotics_even_newer as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3
import math
#import capstone_1_runs_on_laptop as laptop

def main():

    robot = rb.Snatch3rRobot()

    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()


    while True:
        if robot.color_sensor.get_color() == 6:
            robot.drive_system.stop_moving()
            ev3.Sound.set_volume(rc.volume)
            ev3.Sound.speak(rc.words).wait()
            time.sleep(1)
            while robot.beacon_sensor.get_heading_to_beacon() < 0:
                robot.drive_system.start_moving(-50, 50)
            while robot.beacon_sensor.get_heading_to_beacon() > 0:
                robot.drive_system.start_moving(50, -50)
            robot.drive_system.left_wheel.reset_degrees_spun()
            robot.drive_system.right_wheel.reset_degrees_spun()
            while robot.beacon_sensor.get_distance_to_beacon() > 1:
                robot.drive_system.start_moving(50, 50)
            a = robot.drive_system.left_wheel.get_degrees_spun()
            b = robot.drive_system.right_wheel.get_degrees_spun()
            distance = (a + b) / 2
            robot.drive_system.stop_moving()
            ev3.Sound.speak('I reach the station').wait()
            mqtt_client.send_message('set_distance',[distance])
            break

        else:
            rc.go_as_go()

        time.sleep(0.01)  # For the delegate to do its work
class RemoteControlEtc(object):
    def __init__(self, robot):
        """
        Stores a robot.
            :type robot: rb.Snatch3rRobot
        """

        self.robot = robot
        self.mqtt_client = com.MqttClient()
        self.left_speed = 0
        self.right_speed = 0
        self.volume = 100
        self.words = ''
    def beep_and_talk(self):
            while True:
                if self.robot.beacon_button_sensor.is_bottom_blue_button_pressed() is True:
                    break
                if self.robot.beacon_button_sensor.is_top_red_button_pressed() is True:
                    ev3.Sound.beep(0.5)
                if self.robot.beacon_button_sensor.is_top_blue_button_pressed() is True:
                    ev3.Sound.speak('Hello. How are you?')

    def go_forward(self,speed_string):
        speed = int(speed_string)
        print('Robot should start moving',speed)
        self.robot.drive_system.start_moving(speed,speed)
    def Infrared_beacon(self):
        while True:
            if self.robot.beacon_button_sensor.is_top_blue_button_pressed() is True:
                self.robot.drive_system.go_straight_inches(5,-30)
            if self.robot.beacon_button_sensor.is_top_red_button_pressed() is True:
                self.robot.drive_system.go_straight_inches(5,30)
    def final_go(self,left_speed,right_speed):
       self.left_speed = left_speed
       self.right_speed = right_speed
    def go_as_go(self):
        self.robot.drive_system.start_moving(self.left_speed,self.right_speed)
    def set_volume(self,volume):
        self.volume = volume
    def set_words(self,words):
        self.words = words






main()