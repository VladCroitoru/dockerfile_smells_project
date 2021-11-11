FROM ubuntu:xenial

ARG VNC_PASSWORD=secret
ENV VNC_PASSWORD=${VNC_PASSWORD} \
    WSPC=/home/gopher/catkin_ws \
    DEBIAN_FRONTEND=noninteractive

# Allow universe and multiverse repos
RUN apt-get update; apt-get install -y software-properties-common wget; \
    apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116; \
    echo "deb http://packages.ros.org/ros/ubuntu xenial main" >/etc/apt/sources.list.d/ros-latest.list; \
    wget http://packages.osrfoundation.org/gazebo.key -O - | apt-key add -; \
    echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable xenial main" >/etc/apt/sources.list.d/gazebo-stable.list; \
    add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ xenial restricted universe multiverse"; \
    add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ xenial-updates restricted universe multiverse";

# Install dependencies
RUN apt-get update; apt-get install -y sudo \
    dbus-x11 x11vnc xvfb supervisor \
    dwm suckless-tools stterm \
    ros-lunar-desktop \
    gazebo9 libgazebo9-dev \
    ros-lunar-gazebo9-* \
    ros-lunar-joystick-drivers ros-lunar-geographic-msgs \
    python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential; \ 
    adduser --system --home /home/gopher --shell /bin/bash --group --disabled-password gopher; \
    usermod -a -G www-data,sudo gopher; \
    echo ' gopher ALL=(ALL)  NOPASSWD: ALL' >> /etc/sudoers; \
    mkdir -p /etc/supervisor/conf.d; \
    x11vnc -storepasswd $VNC_PASSWORD /etc/vncsecret; \
    chmod 444 /etc/vncsecret; \
    apt-get autoclean; \
    apt-get autoremove; \
    rm -rf /var/lib/apt/lists/*; 

COPY supervisord.conf /etc/supervisor/conf.d
EXPOSE 5900
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]

WORKDIR /home/gopher
USER gopher
# Prepare workspace
RUN mkdir -p ${WSPC}/src; \
    . /opt/ros/lunar/setup.sh; . /usr/share/gazebo-9/setup.sh; \
    cd ${WSPC}/src; catkin_init_workspace; \
    cd ${WSPC}; catkin_make; . ${WSPC}/devel/setup.sh; \
    sudo rosdep init; rosdep update; \
    echo "source /usr/share/gazebo-9/setup.sh" >> /home/gopher/.bashrc; \
    echo "source /opt/ros/lunar/setup.bash" >> /home/gopher/.bashrc; \
    echo "source ${WSPC}/devel/setup.bash" >> /home/gopher/.bashrc; 

