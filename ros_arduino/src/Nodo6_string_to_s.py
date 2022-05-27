#!/usr/bin/env python

import rospy
from std_msgs.msg import String

clase = " "

def callback_6(dato):

    global clase
    clase=dato.data

def Nodo6_string():

    rospy.init_node('Nodo6_string', anonymous=False)

    rospy.Subscriber("chatter6",String, callback_6)

    pub = rospy.Publisher('bool_string', String, queue_size=10)

    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():

        if clase == "Activo":
            salida = "bueno"
        else:
            salida = "malo"

        hello_str = salida
        rospy.loginfo("Entrada: [" + clase + "] = Salida: [" + salida + "]")
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':

    try:
        Nodo6_string()
    except rospy.ROSInterruptException:
        pass
