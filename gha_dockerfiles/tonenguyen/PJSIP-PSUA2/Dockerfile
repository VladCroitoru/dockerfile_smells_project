
# base most on https://github.com/robvangeloven/PJSUA2-Docker
# Only internal playback without any real audio devices

FROM python:3.9.6-slim-buster AS base

MAINTAINER ="Toan Nguyen"

ARG VERSION_PJSIP=2.10

ENV JAVA_HOME /usr/lib/jvm/default-java/

#Hack for JDK install:

RUN mkdir -p /usr/share/man/man1

RUN apt-get update  &&  apt-get upgrade -y &&  apt-get install -y  \
    gcc \
    build-essential\

#JDK 

   default-jdk  \

#PJSIP

    swig \
    wget \
    openssl\
    libasound2-dev \
    libssl-dev \
    libv4l-dev \
    libsdl2-dev \
    libsdl2-gfx-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-net-dev \
    libsdl2-ttf-dev \
    libx264-dev \
    libavcodec-dev \
    libavdevice-dev \
    libavfilter-dev \
    libavformat-dev \
    libavresample-dev \
    libavutil-dev \
    libpostproc-dev \
    libswresample-dev \
    libswscale-dev \
    libavcodec-extra \
    libopus-dev \
    libopencore-amrnb-dev \
    libopencore-amrwb-dev \
    libvo-amrwbenc-dev \
    portaudio19-dev \
    --assume-yes \
    --no-install-recommends

RUN wget --no-verbose "https://github.com/pjsip/pjproject/archive/refs/tags/$VERSION_PJSIP.tar.gz" -O - | tar xzf -

RUN apt-get autoremove --purge && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR pjproject-$VERSION_PJSIP

RUN ./configure \
      --enable-shared \
      --prefix=/install

# Customization of pjsip for further refinement

# RUN cp /pjproject-$VERSION_PJSIP/pjsip/src/pjsip-ua/ /pjproject-$VERSION_PJSIP/pjsip/src/pjsip-ua/

RUN make dep \
    && make \
    && make install

WORKDIR pjsip-apps/src/swig
RUN make \
    && make install

# Minimize image footprint

FROM base AS final
ENV LD_LIBRARY_PATH=/usr/local/lib

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y\
    libpcap0.8 \
    #libncurses5\
    libncurses6\
    #libasound2 \
    libssl1.1 \
    openssl\
    libv4l-0 \
    libsdl2-2.0-0 \
    libsdl2-gfx-1.0-0 \
    libsdl2-image-2.0-0 \
    libsdl2-mixer-2.0-0 \
    libsdl2-net-2.0-0 \
    libsdl2-ttf-2.0-0 \
    libx264-155 \
    libavformat58 \
    #libavcodec58 \
    libavcodec-extra58 \
    libavdevice58 \
    libavfilter-extra7\
    libavresample4 \
    libavutil56 \
    #libpostproc55 \
    #libswresample3 \
    #libswscale5 \
    libopus0 \
    #libopencore-amrnb0 \
    libopencore-amrwb0 \
    #libportaudio2 \
    #libportaudiocpp0 \
    --assume-yes \
    --no-install-recommends \
    && apt-get autoremove --purge \
    && apt-get clean
    
COPY --from=base /install /usr/local
COPY --from=base /root/.local/lib/python3.9/site-packages /root/.local/lib/python3.9/site-packages    

