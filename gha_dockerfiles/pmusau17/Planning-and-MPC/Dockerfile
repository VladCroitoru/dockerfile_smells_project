#FROM ros:melodic-robot


#pull from the osrf full melodic build
FROM nvidia/cudagl:10.1-base-ubuntu18.04
ENV NVIDIA_DRIVER_CAPABILITIES ${NVIDIA_DRIVER_CAPABILITIES},display
ENV DEBIAN_FRONTEND=noninteractive 

#install ros
RUN apt-get update && apt-get install -q -y \
    dirmngr \
    gnupg2 \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*

# setup keys
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

# setup sources.list
RUN echo "deb http://packages.ros.org/ros/ubuntu `lsb_release -sc` main" > /etc/apt/sources.list.d/ros-latest.list



# install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
    python-rosdep \
    python-rosinstall \
    python-vcstools 
    #\
    
#&& rm -rf /var/lib/apt/lists/*

# setup environment
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# bootstrap rosdep
RUN rosdep init \
    && rosdep update

RUN echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/ros-latest.list
# install ros packages
ENV ROS_DISTRO melodic
RUN apt-get update && apt-get install -y ros-melodic-desktop-full && rosdep update && apt install -y python-rosinstall python-rosinstall-generator python-wstool build-essential
RUN apt-get update &&  apt-get install -y ros-melodic-ros-control ros-melodic-ros-controllers ros-melodic-gazebo-ros-control ros-melodic-ackermann-msgs ros-melodic-joy
RUN apt-get update &&  apt-get install -y ros-melodic-teb-local-planner ros-melodic-move-base ros-melodic-navigation ros-melodic-hector-slam ros-melodic-driver-common ros-melodic-actionlib


#install pip
RUN apt-get install -y python-pip && apt-get install -y python3-pip

RUN pip install rospkg defusedxml PySide2
RUN pip install empy 

#Need these packages for debugging
RUN apt-get install -y nano
RUN apt-get install -y net-tools

# RUN pip install --upgrade pip && apt-get remove -y python-enum34 python-pyasn1-modules && pip2 install numpy scipy &&  pip2 install tensorflow-gpu && apt-get install -y python-opencv && apt-get install -y ros-melodic-cv-bridge ros-melodic-vision-opencv && pip install pathlib

# #navigate to the home directory
# WORKDIR home
# RUN pip install gdown
# RUN gdown https://drive.google.com/uc?id=152KL7JzDReYdg6quBznL9WtC0I5IvNx6
# RUN apt-get install unzip && unzip rl_library.zip 
# WORKDIR rl_library
# RUN pip install -e .
# WORKDIR ..


# RUN git clone https://github.com/pmusau17/Platooning-F1Tenth
# WORKDIR Platooning-F1Tenth 

# # try eigen three installation
# RUN git pull && apt-get update && apt-get install -y ros-melodic-pcl-conversions ros-melodic-pcl-msgs ros-melodic-pcl-ros libeigen3-dev libproj-dev libmove-base-msgs-dev
# RUN ln -s /usr/include/eigen3/Eigen /usr/local/include/Eigen
# RUN /bin/bash -c 'source /opt/ros/melodic/setup.bash && catkin_make'

# # get the model files so that there's no lag in starting gazebo
# RUN apt-get install wget && wget -l 2 -nc -r "http://models.gazebosim.org/" --accept gz && mkdir /usr/share/gazebo-7/models/
# WORKDIR models.gazebosim.org
# RUN ls /usr/share/gazebo && ls /usr/share/gazebo-7 && for i in *; do tar -zvxf "$i/model.tar.gz";  done && mv * /usr/share/gazebo-7/models/
# WORKDIR .. 
# RUN rm -r models.gazebosim.org

# RUN apt-get install -y ros-melodic-gazebo-ros-pkgs

# # Pytorch python 2.7
# RUN pip install torch torchvision
# RUN pip install future
# RUN pip install keras==2.3.1
# RUN pip install imutils
# RUN pip install seaborn

# CMD /bin/bash -c "source devel/setup.bash && roslaunch race sim_for_rtreach.launch verbose:=true gui:=true"


RUN apt-get update && apt-get install apt-transport-https 
RUN apt-get update &&  apt-get install -y ros-melodic-ros-control ros-melodic-ros-controllers ros-melodic-gazebo-ros-control ros-melodic-ackermann-msgs ros-melodic-joy
RUN apt-get update &&  apt-get install -y ros-melodic-teb-local-planner ros-melodic-move-base ros-melodic-navigation ros-melodic-hector-slam ros-melodic-driver-common ros-melodic-actionlib


# try eigen three installation
RUN apt-get update && apt-get install -y ros-melodic-pcl-conversions ros-melodic-pcl-msgs ros-melodic-pcl-ros libeigen3-dev libproj-dev libmove-base-msgs-dev
RUN ln -s /usr/include/eigen3/Eigen /usr/local/include/Eigen
#RUN /bin/bash -c 'source /opt/ros/melodic/setup.bash && catkin_make'


# Install OSQP
RUN git clone --recursive https://github.com/oxfordcontrol/osqp
WORKDIR osqp 
RUN mkdir build
WORKDIR build 
RUN cmake -G "Unix Makefiles" .. && cmake --build .
RUN cmake --build . --target install
WORKDIR ../../

# Install Osqp Eigen
RUN git clone https://github.com/robotology/osqp-eigen.git
WORKDIR osqp-eigen
RUN mkdir build 
WORKDIR build 
RUN cmake ../ && make && make install 

WORKDIR ../../


# Install Catch2

RUN git clone https://github.com/catchorg/Catch2.git
WORKDIR Catch2
RUN cmake -Bbuild -H. -DBUILD_TESTING=OFF && cmake --build build/ --target install 
WORKDIR ..


RUN apt-get install ros-melodic-ompl && apt-get update && apt-get install ros-melodic-eband-local-planner

RUN git clone https://github.com/fuzzylite/fuzzylite
WORKDIR fuzzylite/fuzzylite
RUN git checkout fuzzylite-6.x && mkdir build
WORKDIR build
RUN cmake .. && make && make install
WORKDIR ../../..

RUN mkdir -p ~/catkin_ws/src
ENV OsqpEigen_DIR=/osqp-eigen
RUN apt-get install -y ros-melodic-teb-local-planner && apt-get install -y ros-melodic-rviz 

#install pip
RUN apt-get install -y software-properties-common && add-apt-repository main && apt-add-repository universe && add-apt-repository restricted && add-apt-repository multiverse &&  apt-get update -y && sudo apt install python2.7 && apt-get -y  install python-pip

RUN apt-get install -y wget && wget https://raw.githubusercontent.com/pmusau17/Planning-and-MPC/main/learning_ompl/install-ompl-ubuntu.sh && chmod u+x install-ompl-ubuntu.sh  && /bin/bash -c "./install-ompl-ubuntu.sh --python" 
WORKDIR catkin_ws/

# # small details they often don't tell you I'm tirrrrreeeeeeed
ENV PYTHONPATH="/ompl-1.5.2/py-bindings"

# CMD source /opt/ros/melodic/setup.bash