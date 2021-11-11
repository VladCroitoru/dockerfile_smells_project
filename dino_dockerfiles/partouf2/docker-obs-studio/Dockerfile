FROM rsmmr/clang:latest

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
          build-essential \
          checkinstall \
          git \
          wget \
          libmbedtls-dev \
          libasound2-dev \
          libavcodec-dev \
          libavdevice-dev \
          libavfilter-dev \
          libavformat-dev \
          libavutil-dev \
          libcurl4-openssl-dev \
          libfdk-aac-dev \
          libfontconfig-dev \
          libfreetype6-dev \
          libgl1-mesa-dev \
          libjack-jackd2-dev \
          libjansson-dev \
          libluajit-5.1-dev \
          libpulse-dev \
          libqt5x11extras5-dev \
          libspeexdsp-dev \
          libswresample-dev \
          libswscale-dev \
          libudev-dev \
          libv4l-dev \
          libvlc-dev \
          libx11-dev \
          libx264-dev \
          libxcb-shm0-dev \
          libxcb-xinerama0-dev \
          libxcomposite-dev \
          libxinerama-dev \
          pkg-config \
          python3-dev \
          qtbase5-dev \
          libqt5svg5-dev \
          swig \
          libxcb-randr0-dev \
          libxcb-xfixes0-dev \
          libx11-xcb-dev \
          libxcb1-dev

WORKDIR /home

RUN cd /home && \
    mkdir cmake && \
    cd cmake && \
    wget https://github.com/Kitware/CMake/releases/download/v3.17.1/cmake-3.17.1-Linux-x86_64.sh && \
    chmod +x cmake-3.17.1-Linux-x86_64.sh && \
    ./cmake-3.17.1-Linux-x86_64.sh --skip-license && \
    export PATH=/home/cmake/bin:$PATH

RUN cd /home && \
    git clone --recursive https://github.com/obsproject/obs-studio.git && \
    cd obs-studio && \
    mkdir build && cd build && \
    cmake -DUNIX_STRUCTURE=1 .. && \
    make -j4 && \
    checkinstall --pkgname=obs-studio --fstrans=no --backup=no \
       --pkgversion="$(date +%Y%m%d)-git" --deldoc=yes
