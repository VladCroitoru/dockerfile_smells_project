FROM ros:melodic-ros-base
CMD ["bash"]
SHELL ["/bin/bash", "-c"]
RUN apt-get update -y && apt-get install autoconf automake libtool curl wget make g++ unzip -y && \
    mkdir /protocol_buffers && \
    cd /protocol_buffers && \
    wget -c https://github.com/protocolbuffers/protobuf/releases/download/v3.9.2/protobuf-all-3.9.2.tar.gz && \
    tar xvf protobuf-all-3.9.2.tar.gz && cd protobuf-3.9.2/ && \
    ./configure && \
    make && \
    sudo make install && \
    sudo ldconfig
    
RUN apt-get update && apt-get install -y \
    python3 \
    python-pip 

RUN pip install numpy  

RUN export uid=1000 gid=1000 && \
  mkdir -p /home/workspace && \
  mkdir -p /etc/sudoers.d && \
  echo "workspace:x:${uid}:${gid}:workspace,,,:/home/workspace:/bin/bash" >> /etc/passwd && \
  echo "workspace:x:${uid}:" >> /etc/group && \
  echo "workspace ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/workspace && \
  chmod 0440 /etc/sudoers.d/workspace && \
  chown ${uid}:${gid} -R /home/workspace && \
  adduser workspace sudo

# set working directory
ENV HOME /home/workspace
WORKDIR $HOME/udacity_ws/src


RUN chown -R workspace:workspace $HOME/udacity_ws/
RUN chmod 755 $HOME/udacity_ws/

RUN wget https://github.com/git-lfs/git-lfs/releases/download/v3.0.1/git-lfs-linux-amd64-v3.0.1.tar.gz && \
    tar -xvzf git-lfs-linux-amd64-v3.0.1.tar.gz &&\
    ./install.sh 

RUN apt-get install ros-melodic-image-transport ros-melodic-cv-bridge -y
RUN cd $HOME/udacity_ws/src/ &&\
    git clone https://github.com/vijaysamula/udacity_c-_capstone.git &&\
    cd udacity_c-_capstone &&\
    unzip libtensorflow.zip 

RUN /bin/bash -c 'source /opt/ros/melodic/setup.bash &&\
    cd $HOME/udacity_ws &&\
    catkin_make'

RUN echo "source /home/workspace/udacity_ws/devel/setup.bash">> ~/.bashrc

RUN echo "roslaunch efficientdet_deploy start_all_rgb.launch">> ~/.bashrc

