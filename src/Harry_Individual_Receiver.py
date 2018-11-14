import rosebotics_even_newer as rb
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3
import time
import math
import random



def main():
    my_delegate = MyDelegate()
    mqtt_client = com.MqttClient(my_delegate)
    my_delegate.mqtt_client = mqtt_client
    mqtt_client.connect_to_pc()
    while True:
        time.sleep(0.01)


class MyDelegate(object):

    def __init__(self):
        self.robot= rb.Snatch3rRobot()
        self.mqtt_client = None

    def Arrogant_Talk(self):
        heading = 3 * (self.robot.beacon_sensor.get_heading_to_beacon())
        distance = 20+(7/10)*(0.5)*self.robot.beacon_sensor.get_distance_to_beacon()
        print(heading)
        if heading <0:
            self.robot.drive_system.spin_in_place_degrees(math.fabs(heading),-100)
        else:
            self.robot.drive_system.spin_in_place_degrees(heading)

        self.robot.drive_system.go_straight_inches(distance)
        ev3.Sound.speak('You are the one')
        time.sleep(1.5)
        ev3.Sound.speak('who wants to talk to me')
        time.sleep(1.5)
        ev3.Sound.speak('keep it short, do not waste my time')

        self.mqtt_client.send_message("arrogant_talk_popup")

    def Bad_Tempered(self):
        self.robot.drive_system.spin_in_place_degrees(360)
        ev3.Sound.speak('Do you know who are you talking to')
        print((7/10)*(0.5)*self.robot.beacon_sensor.get_distance_to_beacon())

        while (7/10)*(0.5)*self.robot.beacon_sensor.get_distance_to_beacon()>10:
            heading = 2.3 * (self.robot.beacon_sensor.get_heading_to_beacon())
            if heading < 0:
                self.robot.drive_system.spin_in_place_degrees(math.fabs(heading), -100)
            else:
                self.robot.drive_system.spin_in_place_degrees(heading)
            self.robot.drive_system.go_straight_inches(10,100)

        self.robot.arm.calibrate()
        ev3.Sound.speak('Watch your language')

    def Arrogant_Color(self):
        self.robot.drive_system.start_moving(80,80)
        self.robot.color_sensor.wait_until_color_is(5)
        self.robot.drive_system.stop_moving()
        ev3.Sound.set_volume(100)
        ev3.Sound.speak('red')


    def Cold_Talk(self):
        heading = 3 * (self.robot.beacon_sensor.get_heading_to_beacon())
        distance = 20 + (7 / 10) * (0.5) * self.robot.beacon_sensor.get_distance_to_beacon()
        print(heading)
        if heading < 0:
            self.robot.drive_system.spin_in_place_degrees(math.fabs(heading), -100)
        else:
            self.robot.drive_system.spin_in_place_degrees(heading)

        self.robot.drive_system.go_straight_inches(distance,50)
        ev3.Sound.speak('Do not take me more than one minute')
        self.mqtt_client.send_message("cold_talk_popup")

    def Cold(self):
        while self.robot.touch_sensor.is_pressed()==False:
            if self.robot.camera.get_biggest_blob().get_area()<25:
                self.robot.drive_system.spin_in_place_degrees(random.randrange(90,270),50)
                self.robot.drive_system.go_straight_inches(10,50)
                ev3.Sound.speak('I am not interested in you')
                time.sleep(1)
                ev3.Sound.speak('do not bother me')
            else:
                time.sleep(0.001)


    def Cold_Color(self):
        self.robot.drive_system.start_moving(50,50)
        self.robot.color_sensor.wait_until_color_is(2)
        self.robot.drive_system.stop_moving()
        ev3.Sound.set_volume(100)
        ev3.Sound.speak('blue')

    def Check_Greeting(self):
        while True:
            self.robot.drive_system.spin_in_place_degrees(90, 100)
            time.sleep(0.5)
            num = self.robot.camera.get_biggest_blob().get_area()
            if num ==0:
                time.sleep(0.1)
                self.robot.drive_system.spin_in_place_degrees(80, -100)
                self.robot.drive_system.go_straight_inches(10, 100)
            else:
                break
        ev3.Sound.speak('Hello how are you')

    def Goodbye(self):
        heading = 3 * (self.robot.beacon_sensor.get_heading_to_beacon())
        distance = 20 + (7 / 10) * (0.5) * self.robot.beacon_sensor.get_distance_to_beacon()
        print(heading)
        if heading < 0:
            self.robot.drive_system.spin_in_place_degrees(math.fabs(heading), -100)
        else:
            self.robot.drive_system.spin_in_place_degrees(heading)

        self.robot.drive_system.go_straight_inches(distance, 50)
        ev3.Sound.speak('goodbye my friend')




main()