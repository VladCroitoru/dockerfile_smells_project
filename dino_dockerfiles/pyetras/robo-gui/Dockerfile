FROM plumbee/nvidia-virtualgl:2.5.2

MAINTAINER Piotr Sokolski

RUN apt-get update --fix-missing && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        tmux wget \
        xvfb \
        vim nano \
        git \
        cmake \
        qt5-default qtcreator \
        net-tools \
        lib32z1 lib32ncurses5 lib32stdc++6 \
        libopencv-dev && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -r /var/lib/apt/lists/*

# ROS Installation

# install packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    dirmngr \
    gnupg2 \
    && rm -rf /var/lib/apt/lists/*

# setup keys
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 421C365BD9FF1F717815A3895523BAEEB01FA116

# setup sources.list
RUN echo "deb http://packages.ros.org/ros/ubuntu xenial main" > /etc/apt/sources.list.d/ros-latest.list

# install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
    python-rosdep \
    python-rosinstall \
    python-vcstools \
    && rm -rf /var/lib/apt/lists/*

# setup environment
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONIOENCODING UTF-8

# bootstrap rosdep
RUN rosdep init \
    && rosdep update

# install ros packages
ENV ROS_DISTRO kinetic

RUN apt-get update && apt-get install -y \
    ros-${ROS_DISTRO}-desktop-full=1.3.1-0* \
    && rm -rf /var/lib/apt/lists/*

# Upgrade Gazebo 7
RUN echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list \
    && wget http://packages.osrfoundation.org/gazebo.key -O - | apt-key add - \
    && apt-get update \
    && apt-get install -y gazebo7 libignition-math2-dev \
    && rm -rf /var/lib/apt/lists/*

# Set this variable so that Gazebo properly loads its UI when using VirtualGL - See https://github.com/P0cL4bs/WiFi-Pumpkin/issues/53
ENV QT_X11_NO_MITSHM 1

# Setup workspace.

RUN mkdir -p /catkin_ws/src
RUN /bin/bash -c "source /opt/ros/${ROS_DISTRO}/setup.bash && \
                  cd /catkin_ws/src && \
                  catkin_init_workspace"

ENV DISPLAY :0

# Initialize gazebo models.
RUN gzserver --verbose --iters 1 worlds/empty.world

# setup entrypoint
COPY ./rosentrypoint.sh /

ENTRYPOINT ["/rosentrypoint.sh"]
CMD ["bash"]
