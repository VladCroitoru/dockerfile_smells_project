FROM kaixhin/cuda-torch

ENV DEBIAN_FRONTEND noninteractive

# Install dependencies 

RUN sed -i "/^# deb .* multiverse$/ s/^# //" /etc/apt/sources.list && apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:mc3man/trusty-media && \
    apt-get -yqq update && apt-get install -y --force-yes wget unzip                \
      build-essential checkinstall cmake pkg-config                                      \
      yasm git libtiff4-dev libjpeg-dev libjasper-dev libavcodec-dev libavformat-dev     \
      libswscale-dev libdc1394-22-dev libxine-dev libgstreamer0.10-dev                   \
      libgstreamer-plugins-base0.10-dev libv4l-dev libtbb-dev                            \
      libav-tools ffmpeg flvmeta libboost1.55-all-dev && \
      apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Build OpenCV 3.1.0

RUN cd /tmp && wget https://github.com/Itseez/opencv/archive/3.1.0.zip && \
    unzip 3.1.0.zip && mkdir /tmp/opencv-3.1.0/build        && \
    cd /tmp/opencv-3.1.0/build                              && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON  \
          -D BUILD_NEW_PYTHON_SUPPORT=OFF -D WITH_V4L=ON -D INSTALL_C_EXAMPLES=OFF       \
          -D INSTALL_PYTHON_EXAMPLES=OFF -D BUILD_EXAMPLES=OFF -D WITH_QT=OFF            \
          -DBUILD_opencv_nonfree=ON -D WITH_OPENGL=OFF  ..      && \
    make -j8 && make install && echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf && \
    ldconfig && rm -rf /tmp/*

RUN luarocks install cv

