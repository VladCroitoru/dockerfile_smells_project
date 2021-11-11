From ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install --no-install-recommends -y \
    lsb-release \
    sudo \
    bash-completion \
    software-properties-common

RUN apt-get install -y locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get install clang-11 -y
RUN apt-get install make -y
RUN apt-get install vim -y

# install ROS
RUN apt-get install curl gpg-agent -y
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
RUN apt-get update
RUN apt install ros-noetic-desktop-full -y
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

# install eigenpy
RUN sh -c "echo 'deb [arch=amd64] http://robotpkg.openrobots.org/packages/debian/pub $(lsb_release -cs) robotpkg' >> /etc/apt/sources.list.d/robotpkg.list"
RUN curl http://robotpkg.openrobots.org/packages/debian/robotpkg.key | sudo apt-key add -
RUN apt-get update
RUN apt install robotpkg-py38-eigenpy
RUN ln -s /opt/openrobots/lib/cmake/eigenpy /usr/lib/cmake/eigenpy

# set a new user
RUN useradd -U -m pinocchio && \
    usermod -G users pinocchio
# user setting
RUN echo "pinocchio ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/pinocchio
RUN chmod 0440 /etc/sudoers.d/pinocchio
RUN chown -R pinocchio:pinocchio /home/pinocchio
ENV USER=pinocchio
ENV HOME=/home/pinocchio
ENV TERM=xterm-256color
ENV COLORTERM=truecolor
USER pinocchio
WORKDIR /home/pinocchio
