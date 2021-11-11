# image from > https://github.com/lentychang/bringups/blob/melodic/kinect2/Docker/Dockerfile
#ARG DOCKER_BASE_IMAGE=lentychang/ros-base:melodic
#FROM DOCKER_BASE_IMAGE
FROM ubuntu:xenial
#ARG ROS_DISTRO=melodic
ARG ENABLE_NVIDIA=true

RUN apt-get update && apt-get install -y software-properties-common && \
    if [ "$ENABLE_NVIDIA" = "true" ] ; then add-apt-repository ppa:graphics-drivers ; fi && \
    if [ "$ENABLE_NVIDIA" = "true" ] ; then apt-get update ; fi && \
    if [ "$ENABLE_NVIDIA" = "true" ] ; then apt-get install -y nvidia-384 ; fi && \
    if [ "$ENABLE_NVIDIA" != "true" ] ; then echo nvidia Disabled; fi

RUN cd /root && \
    git clone https://github.com/OpenKinect/libfreenect2.git && \
    cd libfreenect2 && \
    apt-get update && \
    apt-get install -y build-essential software-properties-common cmake pkg-config \
      libusb-1.0-0-dev libturbojpeg libjpeg-turbo8-dev libturbojpeg0-dev \ 
      libglfw3-dev libopenni2-dev && \
    mkdir build && cd build && \
    cmake .. -DCMAKE_INSTALL_PREFIX=$HOME/freenect2 -Dfreenect2_DIR=$HOME/freenect2/lib/cmake/freenect2 -DENABLE_CXX11=ON && \
    make -j3 && \
    make install

RUN apt-get -y install openni2-utils && \
    cd /root/libfreenect2/build && \
    make install-openni2 

RUN add-apt-repository ppa:floe/beignet && apt-get update;exit 0 && \ 
RUN apt-get -y install beignet opencl-headers


RUN cd /root/catkin_ws/src/ && \
    git clone https://github.com/code-iai/iai_kinect2.git && \
    cd iai_kinect2 && \
    rosdep install -y -r --from-paths .
RUN cd /root/catkin_ws && \
    source devel/setup.bash && \
    catkin_make -DCMAKE_BUILD_TYPE="Release"

RUN echo "source /root/catkin_ws/devel/setup.bash" >> ~/.bashrc && \ 
    echo "export PS1='🐳 \e[1;32mkinect2\e[m\e[1;39m@\e[m\[\e[1;36m\]\h \[\e[1;34m\]\W\[\e[0;35m\] \[\e[1;36m\]# \[\e[0m\]'" >> ~/.bashrc && \
    cp ~/.bashrc ~/.bashrcLocal && \
    echo "export ROS_MASTER_URI='http://172.16.17.115:11311'" >> ~/.bashrc && \
    echo "export ROS_MASTER_URI='localhost:11311'" >> ~/.bashrcLocal