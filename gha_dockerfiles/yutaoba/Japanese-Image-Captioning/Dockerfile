FROM nvidia/cuda:11.0-devel-ubuntu20.04

ENV DEBIAN_FRONTEND=noninteractive

# Install packages
RUN apt-get update -q  && \
    apt-get upgrade -yq && \
    apt-get install -yq \
        wget \
        curl \
        git \
        build-essential \
        vim \
        sudo \
        lsb-release \
        locales \
        bash-completion \
        tzdata \
        gnupg2 \
        tmux \
        x11-apps \
        eog \
        iputils-ping \
        net-tools \
        iproute2 \
        software-properties-common \
        libopencv-dev \
        libgl1-mesa-dev \
        python3 \
        python3-pip \
        mecab \
        libmecab-dev \
        mecab-ipadic-utf8

# Python packages
RUN pip3 install -U pip && \
    pip3 install numpy \
    matplotlib \
    scipy \
    opencv-python \
    opencv-contrib-python \
    PyYaml \
    tqdm \
    tensorflow \
    tensorboard \
    mecab-python3 \
    boto3

# mecab-ipadic-NEologd configuration
WORKDIR /root
RUN git clone https://github.com/neologd/mecab-ipadic-neologd.git
RUN cd mecab-ipadic-neologd && bin/install-mecab-ipadic-neologd -n -y
RUN echo "dicdir=/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd">/etc/mecabrc
