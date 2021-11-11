# Ubuntu install cloned from https://github.com/Rob-Johnson/ubuntu-opencv
FROM ubuntu:12.04.5

# facetracker install from the documentation
# Note: Getting the example code working with a webcam is not currently supported, because it requires additional libraries

RUN echo 'deb http://archive.ubuntu.com/ubuntu precise multiverse' >> /etc/apt/sources.list
RUN apt-get update

RUN apt-get install -y wget
RUN apt-get install -y unzip
RUN apt-get install -y libopencv-dev build-essential checkinstall cmake pkg-config yasm libtiff4-dev libjpeg-dev libjasper-dev libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev libxine-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev libv4l-dev python-dev python-numpy libtbb-dev libqt4-dev libgtk2.0-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev x264 v4l-utils ffmpeg

WORKDIR /tmp
RUN wget https://github.com/Itseez/opencv/archive/2.4.8.zip
RUN unzip 2.4.8.zip

WORKDIR /tmp/opencv-2.4.8
RUN mkdir /tmp/opencv-2.4.8/build

WORKDIR /tmp/opencv-2.4.8/build

RUN cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON -D WITH_QT=ON -D WITH_OPENGL=ON ..
RUN make -j2
RUN make install
RUN echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf
RUN ldconfig

WORKDIR /
RUN rm -rf /tmp/*

# facetracker
#git clone git://github.com/kylemcdonald/FaceTracker.git
#cd FaceTracker
COPY . /FaceTracker
WORKDIR /FaceTracker
RUN make
