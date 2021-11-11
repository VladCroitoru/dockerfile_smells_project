FROM nvidia/cuda:8.0-cudnn7-devel-ubuntu16.04

# Set default shell to bash
SHELL ["/bin/bash", "-c"]

ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

WORKDIR ${HOME}

RUN echo "Preparing system environment..."

RUN mv /root/.bashrc /root/bashrc.bak && \
    touch /root/.bashrc

RUN apt-get update -qq > /dev/null && apt-get install -y -qq sudo wget lsb-release iputils-ping > /dev/null && \
    apt-get install -y -qq build-essential libopencv-dev python-opencv cmake libeigen3-dev vim htop sshfs nfs-common python-dev git python-pip python-all-dev libatlas-base-dev gfortran > /dev/null && \
    apt-get install -y -qq libopenblas-dev mpg123 > /dev/null && \
    rm -rf /var/lib/apt/lists/*

RUN wget -q https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    export PATH=/usr/local/bin:$PATH && \
    rm get-pip.py
    
RUN git clone https://github.com/voutcn/g2o.git && cd g2o && sh init.sh

RUN pip install -q -U bitarray pyzmq ujson requests gunicorn pymysql numpy pandas scipy scikit-learn gTTs awscli numba chardet > /dev/null

RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' && \
    apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116 && \
    apt-get update -qq && \
    apt-get install -y -qq ros-kinetic-desktop-full && \
    rosdep init && \
    rosdep update && \
    echo "source /opt/ros/kinetic/setup.bash" >> /root/.bashrc && \
    source /root/.bashrc

RUN apt-get install -y -qq \
    python-rosinstall \
    pulseaudio socat alsa-utils ffmpeg gstreamer1.0* \
    ros-kinetic-gazebo-ros-control \
    ros-kinetic-controller-manager \
    ros-kinetic-position-controllers \
    ros-kinetic-transmission-interface \
    v4l-utils \
    ros-kinetic-velocity-controllers \
    ros-kinetic-can-msgs \
    ros-kinetic-control-toolbox  \
    ros-kinetic-controller-interface \
    ros-kinetic-controller-manager  \
    ros-kinetic-controller-manager-msgs \
    ros-kinetic-hardware-interface  \
    ros-kinetic-joint-limits-interface \
    ros-kinetic-realtime-tools  \
    ros-kinetic-transmission-interface \
    ros-kinetic-laser-proc ros-kinetic-urg-c \
    bluez \
    evemu-tools \
    evtest \
    inputattach \
    joystick \
    libbluetooth3 \
    libcwiid1 \
    libevemu3 \
    libspnav-dev \
    libusb-dev \
    python-bluez \
    python-cwiid \
    ros-kinetic-combined-robot-hw \
    ros-kinetic-combined-robot-hw-tests \
    ros-kinetic-controller-manager-tests \
    ros-kinetic-diff-drive-controller \
    ros-kinetic-effort-controllers \
    ros-kinetic-force-torque-sensor-controller \
    ros-kinetic-gripper-action-controller \
    ros-kinetic-imu-sensor-controller \
    ros-kinetic-joint-state-controller \
    ros-kinetic-joint-trajectory-controller \
    ros-kinetic-ps3joy \
    ros-kinetic-rqt-joint-trajectory-controller \
    ros-kinetic-spacenav-node \
    ros-kinetic-wiimote \
    spacenavd \
    ros-kinetic-grid-map-core \
    ros-kinetic-grid-map-cv \
    ros-kinetic-grid-map-msgs \
    ros-kinetic-grid-map-ros \
    curl \
    ros-kinetic-joy \
    ros-kinetic-joystick-drivers \
    ros-kinetic-ros-control \
    ros-kinetic-ros-controllers \
    python-dev \
    python3-dev \
    libboost-all-dev \
    cmake \
    compiz-plugins \
    compizconfig-settings-manager \
    libpcap-dev \
    libglew-dev \
    mpg123 \
    sysstat \
    ntpdate \
    ifstat \
    libopencv-dev \
    ros-kinetic-sound-play \
    ros-kinetic-jsk-recognition-msgs \
    ros-kinetic-grid-map-ros \
    ros-kinetic-nmea-msgs \
    ros-kinetic-nmea-navsat-driver \
    ros-kinetic-jsk-visualization \
    ros-kinetic-slam-gmapping ros-kinetic-geodesy \
    ros-kinetic-audio-capture

RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
RUN apt-get install -y nodejs
RUN rm -rf /var/lib/apt/lists/*

RUN rosdep fix-permissions

RUN echo "US/Pacific" > /etc/timezone && \
    unlink /etc/localtime && \
    sudo ln -s /usr/share/zoneinfo/US/Pacific /etc/localtime

# Define default command.
CMD ["/bin/bash"]
