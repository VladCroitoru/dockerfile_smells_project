FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libhighgui-dev \
    libgsl-dev \
    libopencv-core-dev \
    libopencv-highgui-dev \
    libopencv-imgproc-dev \
    libopencv-flann-dev \
    libopencv-photo-dev \
    libopencv-video-dev \
    libopencv-features2d-dev \
    libopencv-objdetect-dev \
    libopencv-calib3d-dev \
    libopencv-ml-dev \
    libopencv-contrib-dev \
    git \
    unzip

RUN git clone https://github.com/NicolasCARPi/curietrack /app

RUN cd /app/src/CellTracking && make

CMD ["/app/src/CellTracking/bin/Release/Tracking"]
