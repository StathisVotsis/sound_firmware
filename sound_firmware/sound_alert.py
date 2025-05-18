#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from pygame import mixer

class SoundAlert(Node):
    def __init__(self):
        super().__init__("sound_alert")
        self.sub_ = self.create_subscription(String, "sound_alert", self.msgCallback, 10)#siren is the topic
        self.sub_
        mixer.init()

    def msgCallback(self, msg):
        file = '/home/pi/robot_ws/src/sound_firmware/sound_firmware/police_siren.mp3'
        mixer.music.load(file)
        self.get_logger().info("New message received on sound alert")
        self.x = int(msg.data.encode("utf-8"))
        if self.x == 1:
           mixer.music.play()
           self.get_logger().info("Playing siren")
           #playsound(file, True)
        elif self.x == 0:
           mixer.music.stop() 
        else:
           mixer.music.stop() 
           self.get_logger().info("else")
          
        


def main():
    rclpy.init()

    sound_alert = SoundAlert()
    rclpy.spin(sound_alert)
    
    sound_alert.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

     
    