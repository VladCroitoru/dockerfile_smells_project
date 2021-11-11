FROM nvidia/cuda
ARG PYTHON_VERSION=3.5
ARG NB_USER=ubuntu

ENV OPENCV_DIR /opt/opencv
ENV NUM_CORES 8
ENV NB_UID 1000
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER

RUN apt-get update && \
    apt-get install -y build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev wget libhdf5-dev g++ graphviz vim nano unzip cmake libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev python3-dev python3-tk libcupti-dev && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    mkdir -p /src && \
    pip3 install numpy theano nose cython && \
    cd /src && \
    mkdir -p $OPENCV_DIR && \
    wget https://github.com/Itseez/opencv/archive/3.2.0.zip && \
    unzip 3.2.0.zip && \
    mv /src/opencv-3.2.0/ $OPENCV_DIR/ && \
    rm -rf /src/3.2.0.zip && \
    wget https://github.com/opencv/opencv_contrib/archive/3.2.0.zip -O 3.2.0-contrib.zip && \
    unzip 3.2.0-contrib.zip && \
    mv /src/opencv_contrib-3.2.0 $OPENCV_DIR/ && \
    rm -rf /src/3.2.0-contrib.zip && \
    mkdir -p $OPENCV_DIR/opencv-3.2.0/build && \
    cd $OPENCV_DIR/opencv-3.2.0/build && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE -D BUILD_PYTHON_SUPPORT=ON -D CMAKE_INSTALL_PREFIX=/usr/local -D INSTALL_C_EXAMPLES=OFF -D INSTALL_PYTHON_EXAMPLES=OFF -D PYTHON3_EXECUTABLE=/usr/bin/python3 -D PYTHON_INCLUDE_DIR=/usr/include/python3.5 -D PYTHON_INCLUDE_DIR2=/usr/include/x86_64-linux-gnu/python3.5m -D PYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.5m.so -D PYTHON3_NUMPY_INCLUDE_DIRS=/usr/local/lib/python3.5/dist-packages/numpy/core/include/ -D OPENCV_EXTRA_MODULES_PATH=$OPENCV_DIR/opencv_contrib-3.2.0/modules -D BUILD_EXAMPLES=OFF -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_IPP=OFF -D WITH_V4L=ON -D WITH_CUDA=OFF .. && \
    make -j8 && \
    make install && \
    ldconfig && \
    rm -R $OPENCV_DIR

USER $NB_USER

CMD ["bash"]
