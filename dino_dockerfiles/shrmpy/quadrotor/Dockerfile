FROM osrf/ros:kinetic-desktop-full-xenial

ARG VNC_PASSWORD=secret
ENV VNC_PASSWORD=${VNC_PASSWORD} \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update; apt-get install -y \
            dbus-x11 x11-utils x11vnc xvfb supervisor \
            dwm suckless-tools stterm; \
    mkdir -p /etc/supervisor/conf.d; \
    x11vnc -storepasswd $VNC_PASSWORD /etc/vncsecret; \
    chmod 444 /etc/vncsecret; \
    adduser --system --home /home/gopher --shell /bin/bash --group --disabled-password gopher; \
    usermod -a -G www-data gopher; 

#    apt-get autoclean; \
#    apt-get autoremove; \
#    rm -rf /var/lib/apt/lists/*; 

COPY supervisord.conf /etc/supervisor/conf.d
EXPOSE 5900
ENTRYPOINT ["/usr/bin/env"]
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]

# Download quadrotor sim plugin
RUN mkdir -p /root/catkin_ws/src; cd /root/catkin_ws; . /opt/ros/kinetic/setup.sh; catkin_make; . /root/catkin_ws/devel/setup.sh; \
    apt-get install -y python-wstool ros-kinetic-joystick-drivers ros-kinetic-teleop-twist-keyboard ros-kinetic-geographic-msgs; \
    wstool init src https://raw.githubusercontent.com/AS4SR/hector_quadrotor/kinetic-devel/tutorials.rosinstall; \
    rosdep install --from-path src --ignore-src --rosdistro kinetic --default-yes; \
    catkin_make;

####    . /root/catkin_ws/devel/setup.sh; roslaunch hector_quadrotor_demo indoor_slam_gazebo.launch;


