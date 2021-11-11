FROM arm32v7/ros:kinetic-ros-base-xenial

MAINTAINER Breandan Considine breandan.considine@nutonomy.com

# Switch on systemd init system in container and set various other variables
ENV QEMU_EXECVE 1 \
    INITSYSTEM="on" \
    TERM="xterm" \
    ROS_DISTRO="kinetic"

COPY . /usr/bin

RUN [ "cross-build-start" ]

RUN echo "deb http://packages.ros.org/ros/ubuntu xenial main" > /etc/apt/sources.list.d/ros-latest.list \
    && apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net --recv-key 0xB01FA116

RUN apt-get clean && apt-get update && apt-get upgrade -y

RUN apt-get install -yq --no-install-recommends --fix-missing \
    ros-kinetic-robot=1.3.2-0* ros-kinetic-perception=1.3.2-0* \
    ros-kinetic-navigation ros-kinetic-robot-localization

# System dependencies
RUN apt-get install -yq --no-install-recommends --fix-missing \
    sudo locales locales-all build-essential \
    etckeeper emacs vim byobu zsh git git-extras htop atop nethogs iftop apt-file ntpdate gfortran \
    libxslt-dev libxml2-dev \
    libblas-dev liblapack-dev libatlas-base-dev libyaml-cpp-dev libpcl-dev libvtk6-dev libboost-all-dev

# Python Dependencies
RUN apt-get install -yq --no-install-recommends --fix-missing \
    python-dev python-pip ipython python-sklearn python-smbus python-termcolor \
    python-tables i2c-tools python-lxml python-bs4 python-openssl python-service-identity \
    python-rosdep python-catkin-tools

# ROS Dependencies
RUN apt-get install -yq --no-install-recommends --fix-missing \
    ros-kinetic-roslint ros-kinetic-hector-trajectory-server \
    ros-kinetic-ros-tutorials ros-kinetic-common-tutorials

# Cleanup packages list
RUN apt-get clean && rm -rf /var/lib/apt/lists
    
# http://rettgergalactic.com/blog/2016/01/fixing-no-rule-to-make-target-usrlibliblog4cxx-so-in-ros/
RUN ln -s /usr/lib/arm-linux-gnueabihf/liblog4cxx.so /usr/lib/

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

RUN pip install --upgrade --user \
    setuptools platformio wheel \
    PyContracts==1.7.15 \
    DecentLogs==1.1.2\
    QuickApp==1.3.8 \
    conftools==1.9.1 \
    comptests==1.4.10 \
    procgraph==1.10.6 \
    pymongo==3.5.1 \
    ruamel.yaml==0.15.34

RUN rosdep init && rosdep update; exit 0

RUN git clone https://github.com/duckietown/software /home/

COPY ./ros_entrypoint.sh .

RUN /bin/bash -c "source /opt/ros/kinetic/setup.bash && catkin_make -C /home/software/catkin_ws/"; exit 0

RUN echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc

RUN [ "cross-build-end" ]

ENTRYPOINT ["bash", "ros_entrypoint.sh"]

CMD ["bash"]
