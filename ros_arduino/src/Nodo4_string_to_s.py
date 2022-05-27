#!/usr/bin/env python

import rospy
from std_msgs.msg import String

clase = " "

def callback_4(dato):

    global clase
    clase=dato.data

def Nodo4_string():

    rospy.init_node('Nodo4_string', anonymous=False)

    rospy.Subscriber("chatter4",String, callback_4)

    pub = rospy.Publisher('int_string', String, queue_size=10)

    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():

        if clase == "despacio":
            salida = "slow"
        elif clase == "normal":
            salida = "normally"
        else:
            salida = "fast"

        hello_str = salida
        rospy.loginfo("Entrada: [" + clase + "] = Salida: [" + salida + "]")
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':

    try:
        Nodo4_string()
    except rospy.ROSInterruptException:
        pass
