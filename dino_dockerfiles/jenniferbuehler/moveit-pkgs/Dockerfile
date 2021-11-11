FROM jenniferbuehler/general-message-pkgs 

MAINTAINER Jennifer Buehler

# Install required ROS dependencies
RUN apt-get update && apt-get install -y \
    ros-indigo-moveit-core \
    ros-indigo-shape-tools \
    ros-indigo-eigen-conversions \
    ros-indigo-roslint \
    && rm -rf /var/lib/apt/lists/

# install git
RUN apt-get update && apt-get install -y git
    
COPY moveit_controller_multidof /catkin_ws/src/moveit_controller_multidof
COPY moveit_object_handling /catkin_ws/src/moveit_object_handling

# Get the repository convenience-pkgs as well
RUN bin/bash -c "cd /catkin_ws/src \
    && git clone https://github.com/JenniferBuehler/convenience-pkgs.git"

# Build
RUN bin/bash -c "source /.bashrc \
    && cd /catkin_ws \
    && catkin_make \
    && catkin_make install"

RUN bin/bash -c "source .bashrc"

CMD ["bash","-l"]
