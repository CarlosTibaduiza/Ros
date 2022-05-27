#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32

clase = 0

def callback_B(dato):

    global clase
    clase=dato.data

def Nodo_int():

    rospy.init_node('Nodo_int', anonymous=False)

    rospy.Subscriber("chatter",Int32, callback_B)

    pub = rospy.Publisher('chatter4', String, queue_size=10)

    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():

        if clase < 350:
            salida = "despacio"
        elif clase < 650:
            salida = "normal"
        else:
            salida = "rapido"

        hello_str = salida
        rospy.loginfo("Entrada: [" + str(clase) + "] = Salida: [" + salida + "]")
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':

    try:
        Nodo_int()
    except rospy.ROSInterruptException:
        pass
