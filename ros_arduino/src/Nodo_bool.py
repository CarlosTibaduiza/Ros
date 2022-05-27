#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool
from std_msgs.msg import String

clase = False

def callback_C(dato):

    global clase
    clase=dato.data

def Nodo_Bool():

    rospy.init_node('Nodo_Bool', anonymous=False)

    rospy.Subscriber("chatter3",Bool, callback_C)

    pub = rospy.Publisher('chatter6', String, queue_size=10)

    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():

        if clase == True:
            salida = "Activo"
        else:
            salida = "Inactivo"

        hello_str = salida
        rospy.loginfo("Entrada: [" + str(clase) + "] = Salida: [" + salida + "]")
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':

    try:
        Nodo_Bool()
    except rospy.ROSInterruptException:
        pass
