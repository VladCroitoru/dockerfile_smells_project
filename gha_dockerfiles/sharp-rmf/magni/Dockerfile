# Setup romio
# Reference: https://answers.ros.org/question/312577/catkin_make-command-not-found-executing-by-a-dockerfile/

FROM ros:melodic

# install build tools
RUN apt-get update && apt-get install -y \
    python3-catkin-tools \
    git python3-vcstool \
    wget qt5-default \
    python3-colcon-common-extensions \
    # For rslidar
    libpcap-dev \
    && rm -rf /var/lib/apt/lists/*

# clone ros package repo
ENV ROS_WS /opt/ros_ws
RUN mkdir -p $ROS_WS/src
WORKDIR $ROS_WS
RUN git -C src clone https://github.com/sharp-rmf/magni.git && \
    vcs import src < src/magni/magni.repos

# install ros package dependencies
RUN apt-get update && \
    rosdep update && \
    rosdep install -y \
      --from-paths \
        src \
      --ignore-src -r &&\
    rm -rf /var/lib/apt/lists/*


# build ros package source
# 'catkin build can't be run directly from docker. Refer to the refernce above for explanation.
RUN catkin config \
      --extend /opt/ros/$ROS_DISTRO && \
    catkin build --cmake-args -DBUILD_IDLC=NO 

# source ros package from entrypoint, used for launching ros nodes from the docker
# RUN sed --in-place --expression \
#       '$isource "$ROS_WS/devel/setup.bash"' \
#       /ros_entrypoint.sh

# run ros package launch file
# CMD ["roslaunch", "roscpp_tutorials", "talker_listener.launch"]