FROM ubuntu:latest

# Use mirror(JAIST) for apt-get
# RUN sed -i'~' -E "s@http://(..\.)?(archive|security)\.ubuntu\.com/ubuntu@http://ftp.jaist.ac.jp/pub/Linux/ubuntu@g" /etc/apt/sources.list

# Install dependencies
RUN apt-get update -y && \
    apt-get install -y build-essential cmake cmake-curses-gui wget unzip git qt5-default libqt5svg5-dev qtcreator && \
    apt-get clean -y

RUN mkdir -p /home/developer
ENV HOME /home/developer
WORKDIR /home/developer

# Download OpenCV
RUN wget -nv -O opencv-2.4.13.zip https://github.com/Itseez/opencv/archive/2.4.13.zip && \
    unzip -q opencv-2.4.13.zip

# Install OpenCV
RUN cd opencv-2.4.13 && \
    mkdir build && \
    cd build && \
    cmake -DCMAKE_BUILD_TYPE=Release .. && \
    make -j4 && \
    make install && \
    cd ../.. && \
    rm -rf opencv-2.4.13*

# Download OpenBR
RUN git clone https://github.com/biometrics/openbr.git && \
    cd openbr && \
    git checkout v1.1.0 && \
    git submodule init && \
    git submodule update

# Build OpenBR
RUN cd openbr && \
    mkdir build &&  cd build && \
    cmake -DCMAKE_BUILD_TYPE=Release .. && \
    make -j4 && \
    make install

# Clean up
RUN apt-get remove --purge -y wget unzip

# Replace 1000 with your user / group id
RUN export uid=1000 gid=1000 && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    mkdir -p /etc/sudoers.d && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer && \
    adduser developer video
USER developer
