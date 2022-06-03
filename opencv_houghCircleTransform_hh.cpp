
// Includes
#include <ros/ros.h>						// Inlcuir libreria para uso de ros
#include <stdio.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include "std_msgs/Int16.h" //Libreria para el manejo de datos del tipo std_msgs en formato Int16

/*#include <iostream>
#include "std_msgs/String.h"
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv/cv.h>
#include <opencv/highgui.h>
#include <cv_bridge/cv_bridge.h>
#include <cvaux.h>
#include <math.h>
#include <cxcore.h>
#include <highgui.h>*/

// Defines - General
#define    NODE_NAME       	"opencv_houghCircleTransform_hh"
#define    OPENCV_WINDOW1       "Original Image"
#define    OPENCV_WINDOW2       "Image Filtered"

// Defines - Topics
#define    TOPIC1_SUB__IMAGE_INPUT      "/usb_cam/image_raw" 		// Imagen obtenida de la camara
#define    TOPIC1_PUB__IMAGE_OUTPUT     "/image_converter/output_video" // Imagen procesada

class ImageConverter
{
    private:
    	ros::NodeHandle nh_;						// Iniciación del nodo


    	image_transport::ImageTransport it_;
    	image_transport::Subscriber topic1_sub__image_input;
    	image_transport::Publisher topic1_pub__image_output;
      ros::Publisher chatter_pub = nh_.advertise<std_msgs::Int16>("ValueX", 100); //el publicador de la coordenada x
      ros::Publisher chatter_pub2 = nh_.advertise<std_msgs::Int16>("ValueY", 100); //el publicador de la coordenada y
    public:

  	ImageConverter() : it_(nh_)
  	{
       	topic1_sub__image_input = it_.subscribe(TOPIC1_SUB__IMAGE_INPUT, 1, &ImageConverter::imageCb, this);
   	    topic1_pub__image_output = it_.advertise(TOPIC1_PUB__IMAGE_OUTPUT, 1);



     cv::namedWindow(OPENCV_WINDOW1);				// Crear GUI para mostrar imagen
	    cv::namedWindow(OPENCV_WINDOW2);
  	}

  	~ImageConverter()
  	{
    	cv::destroyWindow(OPENCV_WINDOW1);				// cerrar ventadas para mostar imagen
	    cv::destroyWindow(OPENCV_WINDOW2);
  	}

	void imageCb(const sensor_msgs::ImageConstPtr& msg)
  	{

    	    cv_bridge::CvImagePtr cv_OriginalImage_ptr;
    	    try
    	    {
      		cv_OriginalImage_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
    	    }
	    catch (cv_bridge::Exception& e)
    	    {
      		ROS_ERROR("cv_bridge exception: %s", e.what());
      		return;
    	    }

    	// Convertir información a cv::Mat class
	    cv::Mat cvMat_Image = cv_OriginalImage_ptr->image;

	    // Convertir imagen a formato "gray".
	    cv::Mat cvMat_GrayImage;
	    cv::cvtColor(cvMat_Image, cvMat_GrayImage, CV_BGR2GRAY);

	    // Aplicación de filtro gaussiano
	    cv::Mat cvMat_GrayImage_filtered;
	    cv::GaussianBlur(cvMat_GrayImage, cvMat_GrayImage_filtered, cv::Size(9, 9), 2, 2);


	    std::vector<cv::Vec3f> circles;
	    cv::HoughCircles(cvMat_GrayImage_filtered, circles, CV_HOUGH_GRADIENT, 2, 20, 100, 155, 0, 0 );

	    // procesamiento de circulos
	    for(size_t i = 0; i < circles.size(); i++)
	    {
		// dibujar un circulos
		cv::Point center(cvRound(circles[i][0]), cvRound(circles[i][1]));
 		int radius = cvRound(circles[i][2]);				// Establecer tamaño del circulo
   		circle(cvMat_Image, center, 3, cv::Scalar(0,255,0), -1, 8, 0 ); // circulo verde de radio 3 indicando el centro
   		circle(cvMat_Image, center, radius, cv::Scalar(0,0,255), 3, 8, 0 ); // circulo blanco indicando el tamaño del circulo encontrado



		ROS_INFO("Circle detected #%d / %d: ", int(i)+1, (int)circles.size());
		// Imprimir X e Y en el terminal
		ROS_INFO("    x=%d, y=%d, r=%d: ", cvRound(circles[i][0]), cvRound(circles[i][1]), cvRound(circles[i][2]));


    //Envio cordenadas
    std_msgs::Int16 msg;
    msg.data = (int)cvRound(circles[i][0]);
    chatter_pub.publish(msg);
    msg.data = (int)cvRound(circles[i][1]);
    chatter_pub2.publish(msg);
      	    }

    	    // Actualizar GUI
   	    cv::imshow(OPENCV_WINDOW1, cvMat_Image);
    	  cv::waitKey(3);

	    // Actualizar GUI
   	  cv::imshow(OPENCV_WINDOW2, cvMat_GrayImage_filtered);
	    cv::waitKey(3);
	}
};

//***Main***
int main(int argc, char** argv)
{
    // Init ROS
    ros::init(argc, argv, NODE_NAME);						// Inicializar ROS
    ImageConverter ic;								// Inicializar objetos de la clase ImageConverter
    ros::spin();
    return 0;
}
