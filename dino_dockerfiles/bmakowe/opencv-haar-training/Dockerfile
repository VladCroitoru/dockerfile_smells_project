FROM            ubuntu:latest

LABEL           de.innoq.opencv-haar-training.maintainer="Bjoern.Makowe@innoq.com" \
                de.innoq.opencv-haar-training.vendor="innoQ Deutschland GmbH" \
                de.innoq.opencv-haar-training.name="OpenCV HAAR classifier training" \
                de.innoq.opencv-haar-training.description="Image for automated OpenCV HAAR classifier training" \
                de.innoq.opencv-haar-training.version="1.0"

ENV             VERSION=3.2.0

COPY            docker-entrypoint.sh /usr/local/bin/

RUN             apt-get update \
             && apt-get install --yes \
                    git \
                    curl \
                    python \
                    perl \
                    build-essential \
                    cmake \
                    pkg-config \
                    libjpeg8-dev \
                    libtiff5-dev \
                    libjasper-dev \
                    libpng12-dev \
                    libavcodec-dev \
                    libavformat-dev \
                    libswscale-dev \
                    libv4l-dev \
                    libxvidcore-dev \
                    libx264-dev \
                    libatlas-base-dev \
                    gfortran \
             && cd /home \
             && curl -o opencv.tar.gz -L https://github.com/opencv/opencv/archive/${VERSION}.tar.gz \
             && tar -zxf opencv.tar.gz \
             && rm -f opencv.tar.gz \
             && mv opencv-* opencv \
             && cd opencv \
             && mkdir build \
             && cd build \
             && cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local .. \
             && make -j7 \
             && make clean \
             && make \
             && make install \
             && ldconfig \
             && cd /home \
             && git clone https://github.com/mrnugget/opencv-haar-classifier-training.git \
             && ln -s /home/opencv-haar-classifier-training/positive_images /positive_images \
             && ln -s /home/opencv-haar-classifier-training/negative_images /negative_images \
             && ln -s /home/opencv-haar-classifier-training/classifier /classifier \
             && rm -rf /var/lib/apt/lists/* \
             && ln -s usr/local/bin/docker-entrypoint.sh /docker-entrypoint.sh \
             && chmod +x /docker-entrypoint.sh

VOLUME          /positive_images \
                /negative_images \
                /classifier

ENTRYPOINT      docker-entrypoint.sh
