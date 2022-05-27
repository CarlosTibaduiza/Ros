#!/usr/bin/env python

import rospy
from std_msgs.msg import String

clase4 = " "
clase5 = " "
clase6 = " "

def callback_4(dato):

    global clase4
    clase4=dato.data

def callback_5(dato):

    global clase5
    clase5=dato.data

def callback_6(dato):

    global clase6
    clase6=dato.data

def Nodo_final_s():

    rospy.init_node('Nodo_final_s', anonymous=False)

    rospy.Subscriber("int_string",String, callback_4)

    rospy.Subscriber("float_string",String, callback_5)

    rospy.Subscriber("bool_string",String, callback_6)

    pub = rospy.Publisher('mensaje_final',String, queue_size=10)

    rate = rospy.Rate(0.5) #0.5Hertz

    while not rospy.is_shutdown():

        hello_str = "\n Entero: %s " % clase4 + "\n Decimal: %s " % clase5 + "\n Booleano: %s " % clase6 + "\n -------------------------"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':

    try:
        Nodo_final_s()
    except rospy.ROSInterruptException:
        pass
