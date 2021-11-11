# from	python:2.7-onbuild
FROM	python:2.7

# Ubuntu sides with libav, I side with ffmpeg.
# RUN	echo "deb http://ppa.launchpad.net/jon-severinsson/ffmpeg/ubuntu quantal main" >> /etc/apt/sources.list
# RUN	apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1DB8ADC1CFCA9579

# Prerequisites
RUN	apt-get update
RUN	apt-get install -y -q wget curl
# RUN	apt-get install -y -q build-essential
RUN	apt-get install -y -q cmake
RUN	apt-get install -y -q unzip
RUN	pip install numpy
# RUN	apt-get install -y -q libavformat-dev libavcodec-dev libavfilter-dev libswscale-dev
# RUN	apt-get install -y -q libjpeg-dev libpng-dev libtiff-dev libjasper-dev zlib1g-dev libopenexr-dev libxine-dev libeigen3-dev libtbb-dev

# Install OpenCV
RUN wget 'http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.11/opencv-2.4.11.zip/download' -O opencv-2.4.11.zip \
    && unzip opencv-2.4.11.zip \
    && rm opencv-2.4.11.zip \
    && mkdir -p opencv-2.4.11/release \
    && cd opencv-2.4.11/release \
    && cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D BUILD_PYTHON_SUPPORT=ON -D WITH_XINE=ON -D WITH_TBB=ON .. \
    && make && make install \
    && cd / \
    && rm -rf opencv-2.4.11 \

