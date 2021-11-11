FROM voduytuan/docker-apache-php

#ty "apt-fast" is installed by default just to accelerate installl progress.
# All other dependencies are more or less needed by building phase of OpenCV.
# The last "apt-get clean" command is needed to reduce Docker image size.
#
RUN apt-get update && apt-get upgrade -y \
&& apt-get install software-properties-common -y && add-apt-repository ppa:saiarcot895/myppa && apt-get update && apt-get -y install apt-fast \
&& apt-fast install -y \
build-essential cmake git pkg-config \
libgtk2.0-dev libgtk-3-dev libavcodec-dev libavformat-dev libswscale-dev \
python-dev python2.7-dev python3.4-dev python-numpy python3-numpy \
libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev \
libdc1394-22-dev libv4l-0 libv4l-dev libgl1-mesa-dev libgles1-mesa-dev libgles2-mesa-dev \
libopenvg1-mesa-dev libglu1-mesa-dev \
libgtkglext1 libgtkglext1-dev \
openjdk-7-jdk ant \
vtk6 libvtk6-dev \
&& apt-get clean

# Add build opencv script
ADD	build_opencv.sh	/build_opencv.sh

# Running build opencv script for building OPENCV
RUN	/bin/sh /build_opencv.sh

RUN apt-get install -y autoconf automake libtool m4 php5-dev

# Export needed variable for php extension building
RUN export LIBS=/usr/lib/libopencv_*.so.*

# Download extension facedetect for manual building from source
RUN mkdir /opt/phpfacedetect \
    && cd /opt/phpfacedetect \
    && git clone https://github.com/infusion/PHP-Facedetect.git \
    && cd /opt/phpfacedetect/PHP-Facedetect

# Change current working directory to extension source code
WORKDIR /opt/phpfacedetect/PHP-Facedetect

# Build php facedetect extension for using function face_count() and face_detect()
RUN sudo phpize
RUN ./configure
RUN make && make install
RUN echo "extension=facedetect.so" >> /etc/php5/apache2/conf.d/facedetect.ini

# Add source code of default webservice for face detect
ADD www /var/www/site


