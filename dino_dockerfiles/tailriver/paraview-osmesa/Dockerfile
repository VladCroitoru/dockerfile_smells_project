FROM ubuntu:latest
MAINTAINER Shinsuke Ogawa <shinsuke@tailriver.net>

RUN apt-get update && apt-get -y install \
        libpthread-stubs0-dev \
        llvm \
        python2.7 \
 && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get -y install \
        autoconf \
        bison \
        cmake \
        curl \
        flex \
        g++ \
        pkg-config \
        python2.7-dev \
        python-mako \
 && curl -L ftp://ftp.freedesktop.org/pub/mesa/13.0.5/mesa-13.0.5.tar.gz | tar xz \
 && cd mesa-13.0.5 \
 && ./configure \
        --disable-dri \
        --disable-egl \
        --disable-gbm \
        --disable-glx \
        --disable-omx \
        --disable-texture-float \
        --disable-xvmc \
        --disable-va \
        --disable-vdpau \
        --enable-gallium-osmesa \
        --with-dri-drivers= \
        --with-egl-platforms= \
        --with-gallium-drivers=swrast \
 && make \
 && make install \
 && ldconfig \
 && cd / \
 && curl -L "http://www.paraview.org/paraview-downloads/download.php?submit=Download&version=v5.2&type=source&os=all&downloadFile=ParaView-v5.2.0.tar.gz" | tar xz \
 && mkdir build \
 && cd build \
 && cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DVTK_USE_X=OFF \
        -DOPENGL_INCLUDE_DIR=IGNORE \
        -DOEPNGL_gl_LIBRARY=IGNORE \
        -DOPENGL_xmesa_INCLUDE_DIR=IGNORE \
        -DOSMESA_INCLUDE_DIR=/usr/local/include \
        -DOSMESA_LIBRARY=/usr/local/lib/libOSMesa.so \
        -DPARAVIEW_BUILD_QT_GUI=OFF \
        -DPARAVIEW_ENABLE_PYTHON=ON \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython2.7.so \
        -DVTK_OPENGL_HAS_OSMESA=ON \
        -DVTK_USE_OFFSCREEN=ON \
        /ParaView-v5.2.0 \
 && make \
 && make install \
 && ldconfig \
 && cd / \
 && rm -r /mesa-13.0.5 /ParaView-v5.2.0 /build \
 && apt-get purge -y --auto-remove --purge \
        autoconf \
        bison \
        cmake \
        curl \
        flex \
        g++ \
        pkg-config \
        python2.7-dev \
        python-mako \
 && rm -rf /var/lib/apt/lists/*
RUN apt update && apt install -y libpython2.7 \
 && rm -rf /var/lib/apt/lists/*
