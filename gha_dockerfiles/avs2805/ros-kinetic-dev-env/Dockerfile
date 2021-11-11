FROM ros:kinetic
SHELL ["/bin/bash","-c"] 

ENV ROS_DISTRO kinetic
ENV LIBMODBUS libmodbus_3.1.6-1_amd64.deb
ENV CATKIN_WS=/root/catkin_ws

# Setup Locales
RUN apt-get update && apt-get install -y locales
ENV LANG="en_US.UTF-8" LC_ALL="en_US.UTF-8" LANGUAGE="en_US.UTF-8"


RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen --purge $LANG && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=$LANG LC_ALL=$LC_ALL LANGUAGE=$LANGUAGE

# Set up timezone
ENV TZ 'America/Los_Angeles'
RUN echo $TZ > /etc/timezone && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# Install basic dev and utility tools
RUN apt-get update && apt-get install -y \
    stow \
    nano \
    unzip \
    apt-utils \
    software-properties-common \
    apt-transport-https \
    ca-certificates \
    git \
    lsb-release \
    wget 

# Update to GCC 9
RUN add-apt-repository ppa:ubuntu-toolchain-r/test \
    && apt-get update \
    && apt-get install -y gcc-9 g++-9

RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 90 --slave /usr/bin/g++ g++ /usr/bin/g++-9 && \
    sudo update-alternatives --config gcc

# Obtain a copy of our signing key:
RUN wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null \
    | gpg --dearmor - | sudo tee /etc/apt/trusted.gpg.d/kitware.gpg >/dev/null

# Update CMake version
RUN apt-add-repository 'deb https://apt.kitware.com/ubuntu/ xenial main'
RUN apt-get update
RUN apt-get install -y cmake
# Clear apt-cache to reduce image size
RUN rm -rf /var/lib/apt/lists/*

# install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    python-rosdep 
# Clear apt-cache to reduce image size
RUN rm -rf /var/lib/apt/lists/*

# Install ros packages
# RUN apt-get update && apt-get install -y \
#     ros-${ROS_DISTRO}-catkin \
#     ros-${ROS_DISTRO}-roslint \
#     ros-${ROS_DISTRO}-uuid-msgs \
#     ros-${ROS_DISTRO}-controller-manager \
#     ros-${ROS_DISTRO}-joint-limits-interface \
#     ros-${ROS_DISTRO}-actionlib \
#     ros-${ROS_DISTRO}-control-msgs \
#     ros-${ROS_DISTRO}-combined-robot-hw \
#     ros-${ROS_DISTRO}-realtime-tools \
#     ros-${ROS_DISTRO}-joint-trajectory-controller \
#     ros-${ROS_DISTRO}-xacro \
#     ros-${ROS_DISTRO}-joint-state-controller
# Clear apt-cache to reduce image size
# RUN rm -rf /var/lib/apt/lists/*

# install updated libmodbus
COPY ./${LIBMODBUS} /
RUN dpkg -i /${LIBMODBUS}

# create catkin directories
RUN mkdir -p ${CATKIN_WS}/src
WORKDIR ${CATKIN_WS}

COPY . .

# RUN rosdep init
# RUN rosdep update

# Initialize local catkin workspace
RUN source /opt/ros/${ROS_DISTRO}/setup.bash \
    # Update apt-get because its cache is always cleared after installs to keep image size down
    && apt-get update \
    # Install dependencies
    && cd ${CATKIN_WS} \
    && rosdep install -r -y --from-paths . --ignore-src --rosdistro ${ROS_DISTRO} \
    # Build catkin workspace
    && catkin_make -j8

RUN echo "source /opt/ros/${ROS_DISTRO}}/setup.bash" >> ~/.bashrc

# COPY ./ros_entrypoint.sh /
# RUN chmod +x /ros_entrypoint.sh

# ENTRYPOINT ["/ros_entrypoint.sh"]
# CMD ["bash"]
