# FROM robopaas/rosdocked-kinetic
FROM osrf/ros:kinetic-desktop-full-xenial


# Arguments
ARG user=ros
ARG uid=1000
ARG gid=1000

#Remove interative elements from apt-get
ENV DEBIAN_FRONTEND=noninteractive

#Build tools and other
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y sudo git python-wstool python-rosdep ninja-build wget stow
#
# # Intel Graphics support
RUN apt-get update && \
    apt-get -y install libgl1-mesa-glx libgl1-mesa-dri
#
# RUN apt-get -y install  ros-kinetic-realsense2-camera
#

COPY deb_files /deb_files
RUN cd /deb_files && wget https://milhouse.cloudlab.zhaw.ch/s/pY8KBeLXkPgqngr && dpkg -i /deb_files/*.deb

# #Turtlebot packages
RUN apt-get update && \
    apt-get install ros-kinetic-turtlebot ros-kinetic-turtlebot-apps \
                    ros-kinetic-turtlebot-interactions ros-kinetic-turtlebot-simulator \
                    ros-kinetic-kobuki-ftdi -y

# Rosbridge for server communication
RUN apt-get update && \
    apt-get install ros-kinetic-rosbridge-server -y

# Move a launch file so that gazebo can find it
RUN cp /opt/ros/kinetic/share/turtlebot_navigation/launch/includes/gmapping/gmapping.launch.xml \
       /opt/ros/kinetic/share/turtlebot_navigation/launch/includes/


# Clone user to container, necessary to get X server access.
RUN export uid="${uid}" gid="${gid}" && \
    groupadd -g "${gid}" "${user}" && \
    useradd -m -u "${uid}" -g "${user}" -s /bin/bash "${user}" && \
    passwd -d "${user}" && \
    usermod -aG sudo "${user}"

# Enable access to graphics HW
RUN adduser "${user}" video

# Enable NVIDIA graphics
ENV NVIDIA_DRIVER_CAPABILITIES graphics,utility

WORKDIR "/ros"

# Add whole repository for build.
ADD . "/ros"
# Entrypoint
ADD "./docker/ros_entrypoint.sh" "/ros_entrypoint.sh"

# Update repositories
RUN wstool update -t src --delete-changed-uris


RUN chown -R "${user}:${user}" "/ros"
USER "${user}"
# Install deb dependencies.
RUN rosdep update && \
    rosdep install --from-paths src --ignore-src -y -r

RUN ./src/cartographer/scripts/install_proto3.sh
RUN ./src/cartographer/scripts/install_abseil.sh



# Build and install.
SHELL ["/bin/bash", "-c"]
RUN source "/opt/ros/kinetic/setup.bash" &&\
    catkin_make_isolated --install --use-ninja


# Make SSH available
EXPOSE 22

# Reduce image size
RUN sudo rm -rf /var/lib/apt/lists/*

# Run robot base launch as default
CMD ["roslaunch", "robotslam_launcher", "robot_3dsensor.launch"]

# Mount the user's home directory
VOLUME "/host_home"
VOLUME "/rosbag"
