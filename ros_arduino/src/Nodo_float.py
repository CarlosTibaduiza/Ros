#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64

clase = 0.0

def callback_B(dato):

    global clase
    clase=dato.data

def Nodo_float():

    rospy.init_node('Nodo_float', anonymous=False)

    rospy.Subscriber("chatter2",Float64, callback_B)

    pub = rospy.Publisher('chatter5', String, queue_size=10)

    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():

        if clase < 250:
            salida = "frio"
        elif clase < 550:
            salida = "tibio"
        else:
            salida = "caliente"

        hello_str = salida
        rospy.loginfo("Entrada: [" + str(clase) + "] = Salida: [" + salida + "]")
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':

    try:
        Nodo_float()
    except rospy.ROSInterruptException:
        pass
