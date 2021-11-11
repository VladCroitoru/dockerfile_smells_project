FROM ubuntu:xenial
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt update && apt dist-upgrade -y && apt install -y snapcraft && apt clean

# enable multiverse as snapcraft cleanbuild does
RUN sed -i 's/ universe/ universe multiverse/' /etc/apt/sources.list
RUN apt update &&\
    apt upgrade -y &&\
    apt install -y \
        git \
        software-properties-common \
        build-essential \
        libxcb1-dev     \
        libx11-dev      \
        libgl1-mesa-dev

RUN add-apt-repository ppa:beineri/opt-qt58-xenial -y &&\
    apt update &&\
    apt install -y \
        qt58-meta-full

RUN echo "source /opt/qt58/bin/qt58-env.sh" >> ~/.bashrc

ENV QT_BASE_DIR=/opt/qt58
ENV QTDIR=$QT_BASE_DIR
ENV PATH=$QT_BASE_DIR/bin:$PATH
ENV LD_LIBRARY_PATH=$QT_BASE_DIR/lib:$LD_LIBRARY_PATH
ENV PKG_CONFIG_PATH=$QT_BASE_DIR/lib/pkgconfig:$PKG_CONFIG_PATH

WORKDIR /home/root/

CMD ["/bin/bash"]