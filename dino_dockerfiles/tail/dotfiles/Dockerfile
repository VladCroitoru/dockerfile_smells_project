FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV SHELL bash
ENV TZ=Etc/UTC

RUN set -ex; \
    apt-get update; apt-get install -y \
        bash-completion \
        build-essential \
        git \
        httpie \
        iotop \
        iproute2 \
        nodejs \
        npm \
        perl \
        python2 \
        python2-dev \
        python3 \
        python3-dev \
        python3-pip \
        python3-setuptools \
        python3-wheel \
        screen \
        software-properties-common \
        strace \
        sysstat \
        tmux \
        tzdata \
        universal-ctags \
        vim \
        yarnpkg \
        \
        curl \
        dnsutils \
        dstat \
        iftop \
        htop \
        iputils-ping \
        jq \
        netcat \
        net-tools \
        tcpdump \
        telnet \
        wget \
        whois \
        ; \
    add-apt-repository ppa:neovim-ppa/unstable; \
    apt-get update; \
    apt-get install -y neovim; \
    :; \
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py; \
    python2 get-pip.py; \
    rm get-pip.py; \
    :; \
    ln -s /usr/bin/yarnpkg /usr/local/bin/yarn; \
    pip install neovim; \
    pip3 install neovim; \
    rm -rf /var/lib/apt/lists/*

RUN set -ex; \
    useradd ubuntu; \
    curl -L https://github.com/tianon/gosu/releases/download/1.12/gosu-amd64 > /usr/local/bin/gosu; \
    curl -L https://github.com/tianon/gosu/releases/download/1.12/gosu-amd64.asc > /usr/local/bin/gosu.asc; \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4; \
    gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \
    chmod +sx /usr/local/bin/gosu; \
    rm /usr/local/bin/gosu.asc

COPY . /home/ubuntu/dotfiles

RUN chown -R ubuntu:ubuntu /home/ubuntu

USER ubuntu

WORKDIR /home/ubuntu

RUN set -ex; \
    cd dotfiles; \
    ./install.sh; \
    /usr/bin/vim -S vim-plug-snapshot.vim +qall; \
    nvim -S nvim-plug-snapshot.vim +qall
