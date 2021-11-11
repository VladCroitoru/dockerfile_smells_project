# This Docker file is used to encapsulate the Neato setup used in various
# Olin College courses
FROM ros:indigo-perception
MAINTAINER Paul Ruvolo Paul.Ruvolo@olin.edu

ENV DEBIAN_FRONTEND=noninteractive

# install ros packages
RUN apt-get update && apt-get install -y \
    ros-indigo-robot=1.1.4-0* \
    software-properties-common \
    wget \
    unzip \ 
    hping3 \
    x11vnc \
    xvfb \
    fvwm \
    tcpdump \
    python-pip \ 
    vim && \
    setcap cap_net_raw+ep /usr/sbin/hping3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN add-apt-repository -y ppa:ddalex/gstreamer
RUN apt-get update && apt-get install -y gstreamer1.0* ros-indigo-turtlebot ros-indigo-turtlebot-apps ros-indigo-turtlebot-interactions ros-indigo-turtlebot-simulator ros-indigo-kobuki-ftdi ros-indigo-rocon-remocon ros-indigo-rocon-qt-library ros-indigo-ar-track-alvar-msgs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Setup catkin workspace and ROS environment.
RUN /bin/bash -c "source /opt/ros/indigo/setup.bash && \
                  mkdir -p ~/catkin_ws/src && \
                  cd ~/catkin_ws/src && \
		  git clone https://github.com/paulruvolo/comprobo15.git && \
		  git clone https://github.com/ros-teleop/teleop_twist_keyboard.git && \
                  catkin_init_workspace && \
                  cd ~/catkin_ws/ && \
                  catkin_make && \
                  echo 'source ~/catkin_ws/devel/setup.bash' >> ~/.bashrc"

# build a custom version of opencv
RUN bin/bash -c "cd /tmp && \
    		 wget https://github.com/Itseez/opencv/archive/2.4.11.zip && \
    		 unzip 2.4.11.zip && \
		 cd opencv-2.4.11 && \
		 mkdir build && \
		 cd build && \
		 cmake .. -DCMAKE_BUILD_TYPE=RELEASE \
			-DBUILD_PYTHON_SUPPORT=ON \
			-DWITH_XINE=ON \
			-DWITH_OPENGL=ON \
			-DWITH_TBB=ON \
			-DBUILD_EXAMPLES=ON \
			-DBUILD_NEW_PYTHON_SUPPORT=ON \
			-DWITH_V4L=ON \
			-DOPENCV_EXTRA_MODULES_PATH=./modules && \
		make -j2 && \
		make install && \
		rm -rf /tmp/opencv-2.4.11 && \
		rm -f /tmp/2.4.11.zip"


COPY xsession /root/.xsession

# setup files required for x11vnc
# To start the x11vnc server use: docker exec container_name x11vnc -forever -usepw -create
RUN /bin/bash -c "mkdir ~/.vnc && \
		  mkdir ~/.rviz && \
		  x11vnc -storepasswd 1234 ~/.vnc/passwd && \
		  chmod u+x ~/.xsession"

COPY default.rviz /root/.rviz

CMD /bin/bash -c "source ~/catkin_ws/devel/setup.bash && roslaunch neato_node bringup.launch host:=$HOST"
