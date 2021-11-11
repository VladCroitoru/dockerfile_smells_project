FROM ubuntu:xenial
MAINTAINER OldFrostDragon <shevchukvb@gmail.com>

RUN apt-get update && apt-get install -y software-properties-common python-software-properties && add-apt-repository ppa:beineri/opt-qt56-xenial

RUN apt-get update

# install build suite
RUN apt-get -y install \
        git \
        build-essential \
        libgl1-mesa-dev \
        mesa-common-dev

#install Qt
# Source /opt/qt56/bin/qt56-env.sh to set the correct environment.
RUN apt-get -y install \
        qt56-meta-full

RUN rm -rf /var/lib/apt/lists/*

ENV QT_BASE_DIR=/opt/qt56
ENV QTDIR=$QT_BASE_DIR
ENV PATH=$QT_BASE_DIR/bin:$PATH
ENV LD_LIBRARY_PATH=$QT_BASE_DIR/lib/x86_64-linux-gnu:$QT_BASE_DIR/lib:$LD_LIBRARY_PATH
ENV PKG_CONFIG_PATH=$QT_BASE_DIR/lib/pkgconfig:$PKG_CONFIG_PATH

WORKDIR /usr/src

CMD ["/bin/bash"]