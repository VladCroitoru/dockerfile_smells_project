FROM ubuntu:18.04

ENV CRIU 3.11
ENV TERM xterm-256color

WORKDIR /src
RUN apt-get -q update && \
    apt-get install -qy \
        apt-utils \
        bash \
        bc \
        bridge-utils \
        bsdmainutils \
        build-essential \
        cmake \
        curl \
        curl \
        docker \
        gcc \
        git \
        golang \
        htop \
        jq \
        libaio-dev \
        libcap-dev \
        libncurses5-dev  \
        libnet-dev \
        libnl-3-dev \
        libprotobuf-c0-dev \
        libprotobuf-dev \
        libreadline6-dev  \
        linux-headers-generic \
        make \
        mono-xbuild  \
        npm  \
        pkg-config \
        postgresql \
        protobuf-c-compiler \
        protobuf-c-compiler \
        protobuf-compiler \
        python \
        python-dev \
        python-pip \
        python-protobuf \
        sed \
        sysstat \
        tmux \
        tmux  \
        unzip  \
        wget \
        zsh && \
    rm -rf /var/lib/apt/lists/*

RUN curl -SL https://github.com/xemul/criu/archive/v$CRIU.tar.gz | tar xvz- && \ 
    cd criu-$CRIU && \
    make && \
    make install-criu && \
    cd .. && \
    rm -rf criu-$CRIU

ADD wrapper /usr/local/sbin/
CMD ["wrapper"]
