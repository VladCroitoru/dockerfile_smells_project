# This is an auto generated Dockerfile for ros:desktop-full
# generated from docker_images/create_ros_image.Dockerfile.em
FROM ubuntu:xenial

RUN apt-get update && apt-get install -y --no-install-recommends \
    dirmngr \
    gnupg2 \
    && rm -rf /var/lib/apt/lists/*

# setup keys and sources
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 421C365BD9FF1F717815A3895523BAEEB01FA116
RUN echo "deb http://packages.ros.org/ros/ubuntu xenial main" > /etc/apt/sources.list.d/ros-latest.list

# install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
    python-rosdep \
    python-rosinstall \
    python-vcstools \
    python-catkin-pkg \
    python-wstool \
    ros-kinetic-catkin \
    libttspico-utils \
    #mpg123 \ # doesnt seem to work in a docker
    libgnutls28-dev \
    && rm -rf /var/lib/apt/lists/*

# bootstrap rosdep
RUN rosdep init \
    && rosdep update


# install ros packages
ENV ROS_DISTRO kinetic
RUN apt-get update && apt-get install -y \
    ros-kinetic-desktop-full=1.3.1-0* \
    && rm -rf /var/lib/apt/lists/*

# setup entrypoint
COPY ./ros_entrypoint.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]




# Install all dependencies, using wstool first and rosdep second.

# WORKDIR ~/sara_ws/src
# RUN wstool init
# RUN wget https://raw.githubusercontent.com/WalkingMachine/wm_ci_build/feature/test_docker/sara.rosinstall
# RUN wstool merge sara.rosinstall
# RUN wstool up

# WORKDIR ~/sara_ws
# RUN rosdep install -y --from-paths src --ignore-src --rosdistro kinetic


# compile and test

# RUN source /opt/ros/kinetic/setup.bash
# WORKDIR ~/sara_ws
# RUN catkin_make
# RUN source devel/setup.bash
# RUN catkin_make run_tests && catkin_test_results
