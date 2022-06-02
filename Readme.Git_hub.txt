*** Archivo README ROS***


En el actual archivo se explica generalmente el que y el como utilizar los paquetes o ejercicios realizados durante el primer semestre del 2022 en la materia de ROS, mayormente se utilizo el lenguaje de programacion de python, y en algunas ocasiones se probaron los códigos en c++, pero eso fue a desicion de cada grupo. Tambien se tuvo en cuenta la pagina oficial de ROS, para guiarse en cada uno de los ejercicios. Se recomienda utilizar el ROS NOETIC(UBUNTU 20.04), para evitar daños en maquina virtual o algunos otros problemas de actualizaciones. Se explicará segun la información que se pudo subir a Github debido a que se perdieron muchos datos por daños en maquinas virtuales.


**Primer Corte**

-Ros-tutorials-noetic-devel: En este paquete esta basicamente todo lo relacionado con la instalacion de ros, se siguio el paso a paso de la pagina oficial de Ros, en este caso en el grupo se probo tanto el ros kinetic, como el noetic, al final cada integrante se quedo con el que le parecio mas adecuado y tambien teniendo en cuenta la version de Ubuntu. Tambien todo lo relacionado con herramientas, y paquetes necesarios para utilizar todo en Ros. Se verifica tambien el uso de rostopic, rosinfo, etc... El topic de turtlesim fue el ejemplo y se verificaba mediante el movimiento de la tortuga en una terminal con las flechas.


**Segundo Corte**


-Begginer Tutorials: En esta carpeta se encuentran los ejercicios que inicialmente fueron de prueba cuando se comenzó a ver nodos, topics, donde simplemente hay un nodo Publisher y un nodo Suscriber, en este caso esta en python. El nodo publisher, básicamente publica un dato o una cadena de dato en cualquier tipo, en este caso se envia un entero, mediante un topic y lo recibe cualquier otro nodo con el mismo topico. El nodo Suscriber recibe informacion mediante un topico de un publisher, guarda esa informacion en una funcion y la muestra si lo desea el usuario.

-Ros Arduino: Basado en la carpeta anterior, este paquete contiene todos los nodos que se utilizaron para el parcial del segundo corte. Inicialmente se recibe informacion de 3 tipos de datos(Int,float,bool) en nodos que son publisher y Subscriber a la vez, seguidamente los nodos 4,5,6 reciben esa informacion, y segun la clasificacion de los datos que se manejaron, por ejemplo en el dato del Int(despacio, normal o rapido) y segun que tipo de dato es en los rangos que se manejaron, sale un dato String, finalmente esos 3 nodos(nodos 4,5 y 6) se reciben en un nodo Final, que recibe tambien 3 datos String, se intercambian las variables segun el nombre del dato que se ingreso y se publica en una minitabla las 3 variables finales. Cabe resaltar que se hizo uso del paquete Rosserial y arduino para la comunacion de Ros y arduino.


-Rosserial: Se descargo este paquete para poder usar ROS directamente con el IDE de Arduino. Rosserial nos proporciona  basicamente un protocolo de comunicación ROS que funciona sobre el UART de Arduino. Permite que nuestro arduino sea un nodo ROS completo que puede publicar y suscribirse directamente a mensajes ROS, publicar transformaciones TF y obtener la hora del sistema R, entre otras multiples herramientas que se pueden utilizar en este paquete. Nuestro uso fue principalmente para la comunicacion entre Ros y arduino, y para el parcial del tercer corte de Opencv.


**Tercer Corte**

-Conexion Remoto Remmina&SSH: Basicamente se implemento una conexion remoto entre dos maquinas virtuales de Ubuntu, se habilitaron puertos para poder realizar la conexion, en el caso de de SSH se habilito el puerto 22, y la conexion fue simplemente de un terminal a otro y con respecto a VSH se habilito el puerto 3389 y en esta parte si se podia interactuar con toda la interfaz obteniendo asi un control remoto completo literalmente. Cabe aclarar que se hizo instalacion de aplicaciones y tambien algo muy importante la configuracion de red, en nuestro caso fue bajo la misma red y con conexion "adaptador puente" 

-OpenCV: 