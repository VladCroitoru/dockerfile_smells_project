FROM ubuntu:16.04
MAINTAINER Jonathan Ferretti

RUN apt-get update && apt-get install -y software-properties-common && \
	add-apt-repository "deb http://archive.ubuntu.com/ubuntu xenial multiverse"

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y build-essential \
    cmake git pkg-config libavcodec-dev libavformat-dev libswscale-dev \
    libatlas-base-dev gfortran \
    cmake-curses-gui \
    python3 python3-dev python3-numpy python3-pip python3-scipy python3-matplotlib python-dev python-matplotlib python-numpy python-scipy python-pip python-tk \
    libeigen3-dev yasm libfaac-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev sphinx-common texlive-latex-extra libv4l-dev libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev ant

RUN apt-get install -y qt5-default libqt5opengl5-dev libgtk2.0-dev libgtkglext1 libgtkglext1-dev \
    libvtk6-dev libvtk6-qt-dev libvtk6.2 libvtk6.2-qt

RUN apt-get install -y libpng3 libpng16-dev libpng16-16 \
    libjpeg-dev libjpeg9 libjpeg9-dbg libjpeg-progs libtiff5-dev libtiff5 libtiffxx5 libtiff-tools libjasper-dev libjasper1  libjasper-runtime zlib1g zlib1g-dbg zlib1g-dev \
    libavformat-dev libavutil-ffmpeg54 libavutil-dev libxine2-dev libxine2 libswscale-dev libswscale-ffmpeg3 libdc1394-22 libdc1394-22-dev libdc1394-utils

RUN apt-get install -y libavcodec-dev \
    libfaac-dev libmp3lame-dev \
    libopencore-amrnb-dev libopencore-amrwb-dev \
    libtheora-dev libvorbis-dev libxvidcore-dev \
    ffmpeg x264 libx264-dev \
    libv4l-0 libv4l-dev v4l-utils

RUN apt-get install -y libtbb-dev \
    doxygen

RUN apt-get install -y ant default-jdk

WORKDIR /opt

RUN git config --global http.postBuffer 1048576000 && \
    git clone https://github.com/Itseez/opencv && \
    git clone https://github.com/Itseez/opencv_contrib && \
    mkdir -p /opt/opencv/build

WORKDIR /opt/opencv/build

# Build tiff on as opencv supports tiff4, which is older version, which ubuntu has dropped
#  If you get an error, try disabling freetype by adding the following line in between the cmake command
#  -DBUILD_opencv_freetype=OFF \
RUN cmake -DCMAKE_BUILD_TYPE=RELEASE \
 -DCMAKE_INSTALL_PREFIX=/usr/local \
 -DBUILD_opencv_cvv=OFF \
 -DOPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
 -DBUILD_NEW_PYTHON_SUPPORT=ON \
 -DPYTHON2_EXECUTABLE="/usr/bin/python2" \
 -DPYTHON2_INCLUDE_DIR="/usr/include/python2.7" \
 -DPYTHON2_PACKAGES_PATH="/usr/lib/python2.7/dist-packages" \
 -DPYTHON3_EXECUTABLE="/usr/local/bin/python3" \
 -DPYTHON3_INCLUDE_DIR="/usr/local/include/python3.6m" \
 -DPYTHON3_PACKAGES_PATH="/usr/local/lib/python3.6/site-packages" \
 -DWITH_TBB=ON \
 -DWITH_V4L=ON \
 -DWITH_QT=ON \
 -DWITH_OPENGL=ON \
 -DWITH_VTK=ON \
 -DWITH_IPP=OFF \
 -DWITH_CUDA=OFF \
 -DBUILD_TESTS=OFF \
 -DBUILD_TIFF=ON \
 -DBUILD_opencv_java=ON \
 -DENABLE_AVX=ON ..

RUN make -j8
RUN make install

RUN /bin/bash -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf'
RUN ldconfig

RUN mkdir -p /opt/py_opencv/ && \
    mkdir -p /var/log/py_opencv

WORKDIR /opt/py_opencv

RUN pip install -U pip
COPY requirements.txt /opt/py_opencv/requirements.txt
RUN pip install -r requirements.txt

COPY app /opt/py_opencv/app
COPY run.py /opt/py_opencv/run.py
COPY config.py /opt/py_opencv/config.py

CMD python run.py
