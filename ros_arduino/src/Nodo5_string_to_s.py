#!/usr/bin/env python

import rospy
from std_msgs.msg import String

clase = " "

def callback_5(dato):

    global clase
    clase=dato.data

def Nodo5_string():

    rospy.init_node('Nodo5_string', anonymous=False)

    rospy.Subscriber("chatter5",String, callback_5)

    pub = rospy.Publisher('float_string', String, queue_size=10)

    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():

        if clase == "frio":
            salida = "cold"
        elif clase == "tibio":
            salida = "warn"
        else:
            salida = "hot"

        hello_str = salida
        rospy.loginfo("Entrada: [" + clase + "] = Salida: [" + salida + "]")
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':

    try:
        Nodo5_string()
    except rospy.ROSInterruptException:
        pass
