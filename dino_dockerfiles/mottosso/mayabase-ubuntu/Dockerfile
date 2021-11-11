FROM ubuntu:14.04

MAINTAINER marcus@abstractfactory.io

RUN apt-get update && apt-get install -y \
    nano \
    alien \
    csh \
    elfutils \
    gamin \
    mesa-utils \
    libaudiofile-dev \
    libxinerama1 \
    libglw1-mesa \
    libssl1.0.0 \
    libssl-dev \
    libgamin0 \
    libglw1-mesa-dev \
    libtiff5 \
    libxp6 \
    libcurl4-openssl-dev \
    libgstreamer-plugins-base0.10-0 \
    tcsh \
    ttf-liberation \
    xfstt \
    xfonts-100dpi \
    xfonts-75dpi \
    xorg \
    wget

RUN ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so.62 /usr/lib/libjpeg.so.62 && \
    ln -s /usr/lib/x86_64-linux-gnu/libtiff.so.5.2.0 /usr/lib/libtiff.so.3 && \
    ln -s /lib/x86_64-linux-gnu/libssl.so.1.0.0 /lib/x86_64-linux-gnu/libssl.so.10 && \
    ln -s /lib/x86_64-linux-gnu/libcrypto.so.1.0.0 /lib/x86_64-linux-gnu/libcrypto.so.10 && \
    rm /usr/lib/libfam.so.0 && ln -s /usr/lib/libfam.so.0.0.0 /usr/lib/libfam.so.0

ENV RPM_INSTALL_PREFIX=/usr
ENV LD_LIBRARY_PATH=/opt/Autodesk/Adlm/R5/lib64/
ENV LIBCRYPTO="/usr/lib/x86_64-linux-gnu/libcrypto.so.0.9.8"
ENV LIBSSL="/usr/lib/x86_64-linux-gnu/libssl.so.0.9.8"
