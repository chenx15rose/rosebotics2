"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Harry Chen.
"""

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

import rosebotics_even_newer as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    robot = rb.Snatch3rRobot()
    my_delegate = My_Delegate(robot)
    client = com.MqttClient(my_delegate)
    client.connect_to_pc()
    while True:
        my_delegate.beacon_button()
        time.sleep(0.01)

class My_Delegate(object):
    def __init__(self,robot):
        """
        Stores a robot.
          :type robot: rb.Snatch3rRobot
        """
        self.robot = robot

    def go_forward(self,speed_string):
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed,speed)

    def beacon_button(self):
        while True:
            if self.robot.beacon_button_sensor.is_top_red_button_pressed() is True:
                ev3.Sound.beep()
            if self.robot.beacon_button_sensor.is_top_blue_button_pressed() is True:
                ev3.Sound.speak('Hello. How are you?')

    # --------------------------------------------------------------------------
        # ----------------------------------------------------------------------
        # ----------------------------------------------------------------------


main()