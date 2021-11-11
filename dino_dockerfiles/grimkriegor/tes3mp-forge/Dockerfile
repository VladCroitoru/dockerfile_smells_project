FROM debian:stretch as builder

ENV FORGE_VERSION 2.1.0

ARG BUILD_THREADS=4

ENV PATH=/usr/local/bin:$PATH
ENV LD_LIBRARY_PATH=/usr/local/lib64:/usr/local/lib

RUN echo deb http://deb.debian.org/debian stretch-backports main >> /etc/apt/sources.list \
    && cat /etc/apt/sources.list | sed "s/deb /deb-src /g" >> /etc/apt/sources.list \
    && sed -i "s/ main/ main contrib/g" /etc/apt/sources.list \
    && apt-get update \
    && apt-get -y install \
        build-essential \
        git \
        wget

RUN apt-get -y build-dep \
        libboost-all-dev \
    && apt-get -y install \
        python3-dev \
    && cd /tmp \
    && wget https://dl.bintray.com/boostorg/release/1.65.0/source/boost_1_65_0.tar.gz \
    && tar xf boost_1_65_0.tar.gz \
    && cd boost_1_65_0 \
    && ./bootstrap.sh \
        --with-libraries=program_options,filesystem,system,iostreams \
        --prefix=/usr/local \
    && ./b2 -j ${BUILD_THREADS} install \
    && rm -rf /tmp/boost_1_65_0*

RUN apt-get -y build-dep \
        libmygui-dev \
    && apt-get -y install \
        libfreetype6-dev \
    && cd /tmp \
    && git clone https://github.com/MyGUI/mygui.git mygui \
    && cd mygui \
    && git checkout 82fa8d4fdcaa06cf96dfec8a057c39cbaeaca9c \
    && mkdir build \
    && cd build \
    && cmake \
        -DCMAKE_INSTALL_PREFIX=/usr/local .. \
        -DMYGUI_BUILD_DEMOS=OFF \
        -DMYGUI_BUILD_PLUGINS=OFF \
        -DMYGUI_BUILD_TOOLS=OFF \
        -DMYGUI_RENDERSYSTEM=1 \
    && make -j ${BUILD_THREADS} \
    && make install \
    && rm -rf /tmp/mygui

RUN apt-get -y build-dep \
        libopenscenegraph-3.4-dev \
    && cd /tmp \
    && git clone -b 3.4 https://github.com/OpenMW/osg.git \
    && cd osg \
    && mkdir build \
    && cd build \
    && cmake \
        -DBUILD_OSG_DEPRECATED_SERIALIZERS=0 \
        -DBUILD_OSG_PLUGINS_BY_DEFAULT=0 \
        -DBUILD_OSG_PLUGIN_BMP=1 \
        -DBUILD_OSG_PLUGIN_DDS=1 \
        -DBUILD_OSG_PLUGIN_JPEG=1 \
        -DBUILD_OSG_PLUGIN_OSG=1 \
        -DBUILD_OSG_PLUGIN_PNG=1 \
        -DBUILD_OSG_PLUGIN_SHADOW=1 \
        -DBUILD_OSG_PLUGIN_TGA=1 \
        -DCMAKE_INSTALL_PREFIX=/usr/local .. \
    && make -j ${BUILD_THREADS} \
    && make install \
    && rm -rf /tmp/osg

RUN apt-get -y install \
        libmp3lame-dev \
        libopenjp2-7-dev \
        libopus-dev \
        libspeex-dev \
        libtheora-dev \
        libvorbis-dev \
        libx264-dev \
        pkg-config \
        yasm \
    && cd /tmp \
    && git clone https://github.com/FFmpeg/FFmpeg.git ffmpeg \
    && cd ffmpeg \
    && ./configure \
        --enable-gpl \
        --enable-libmp3lame \
        --enable-libopus \
        --enable-libtheora \
        --enable-libvorbis \
        --enable-shared \
        --prefix=/usr/local \
    && make -j ${BUILD_THREADS} \
    && make install \
    && rm -rf /tmp/ffmpeg

FROM debian:stretch

LABEL maintainer="Grim Kriegor <grimkriegor@krutt.org>"
LABEL description="A container to simplify the packaging of TES3MP for GNU/Linux"

ARG BUILD_THREADS=4
ENV BUILD_THREADS=${BUILD_THREADS}

ENV PATH=/usr/local/bin:$PATH
ENV LD_LIBRARY_PATH=/usr/local/lib64:/usr/local/lib

COPY --from=builder /usr/local /usr/local

RUN echo deb http://deb.debian.org/debian stretch-backports main >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get -y install \
        build-essential \
        git \
        cmake \
        qt5-default \
        qtbase5-dev \
        qtbase5-dev-tools \
        libbullet-dev/stretch-backports \
        libfreetype6 \
        libluajit-5.1-dev \
        libmp3lame0 \
        libncurses5-dev \
        libopenal-dev \
        libopus0 \
        libpng16-16 \
        libqt5opengl5-dev \
        libsdl2-dev \
        libtheora0 \
        libunshield-dev \
        lsb-release \
        unzip \
        wget

RUN git config --global user.email "nwah@mail.com" \
    && git config --global user.name "N'Wah" \
    && git clone https://github.com/GrimKriegor/TES3MP-deploy.git /deploy \
    && mkdir /build

VOLUME [ "/build" ]
WORKDIR /build

ENTRYPOINT [ "/bin/bash", "/deploy/tes3mp-deploy.sh", "--script-upgrade", "--cmake-local", "--skip-pkgs", "--handle-corescripts" ]
CMD [ "--install", "--make-package" ]
