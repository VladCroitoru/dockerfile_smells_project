FROM ros:melodic-ros-base
SHELL ["/bin/bash", "-c"]

WORKDIR /root

ENV PLANNER_WS=planner_workspace

RUN apt update
RUN apt install -y python-catkin-pkg python-rosdep ros-melodic-catkin
RUN apt install -y python3-pip python3-colcon-common-extensions python3-setuptools python3-vcstool python-pip
RUN pip3 install -U setuptools
RUN apt-get install -y ros-melodic-catkin python-catkin-tools
RUN rosdep update
RUN apt-get install -y python3-pip
RUN apt-get install -y python-pip
RUN pip install --upgrade pip
RUN pip install -U rospkg
RUN pip3 install commonroad-io
RUN pip3 install rospkg numpy matplotlib
RUN apt-get install -y libproj-dev
RUN apt-get install -y libprotobuf-dev protobuf-compiler
RUN apt-get install -y ros-melodic-cmake-modules
RUN apt-get install -y ros-melodic-rosbash

RUN git clone https://github.com/arminstr/ros_scenario_simulation.git
WORKDIR /root/ros_scenario_simulation
RUN rosdep install -y --from-paths /root/ros_scenario_simulation/src --ignore-src --rosdistro melodic

RUN git submodule update --init --recursive
WORKDIR src/open_scenario_helper/include/ad-xolib/build
RUN cmake .. -DBUILD_EMBED_TARGETS=OFF
RUN make

WORKDIR /root
RUN mkdir $PLANNER_WS
WORKDIR $PLANNER_WS
RUN mkdir src
COPY ./ci-test.repos /
RUN vcs import src < /ci-test.repos
RUN rosdep update
RUN apt-get update
RUN sudo rosdep install -y --from-paths src --ignore-src --rosdistro melodic
RUN source "/opt/ros/$ROS_DISTRO/setup.bash" && colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release


WORKDIR /root/ros_scenario_simulation
RUN git pull
RUN git pull
RUN source "/opt/ros/$ROS_DISTRO/setup.bash" && catkin build; exit 0
RUN source "/opt/ros/$ROS_DISTRO/setup.bash" && catkin build

COPY ./ros_entrypoint.sh /
COPY ./ros_launchscript.sh /

RUN ["chmod", "+x", "/ros_entrypoint.sh"]
RUN ["chmod", "+x", "/ros_launchscript.sh"]

RUN chown -R root:root reports

USER root

RUN apt-get update
RUN apt-get install -y nginx nodejs

# Remove the default Nginx configuration file
RUN rm -v /etc/nginx/nginx.conf

# Copy a configuration file from the current directory
ADD nginx.conf /etc/nginx/

# Append "daemon off;" to the beginning of the configuration
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Expose ports
EXPOSE 90

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["/ros_launchscript.sh"]