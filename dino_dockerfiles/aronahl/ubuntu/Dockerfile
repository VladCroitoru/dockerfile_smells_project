FROM ubuntu:16.04
MAINTAINER https://github.com/aronahl
RUN apt-get update && \
    apt-get install -fy locales && \
    locale-gen en_US.UTF-8  
ENV LANG=en_US.UTF-8  \
    LANGUAGE=en_US:en  \
    LC_ALL=en_US.UTF-8 \
    DEBIAN_FRONTEND=noninteractive \
    HOME=/root
RUN apt-get dist-upgrade -fy && \
    apt-get install --no-install-recommends -fy \
        bsdmainutils \
        command-not-found \
        curl \
        git \
        htop \
        jq \
        less \
        man \
        mosh \
        netmask \
        openssh-client \
        patch \
        python-pip \
        socat \
        vim-nox \
        w3m && \
    pip install --upgrade pip && \
    pip install setuptools && \
    pip install awscli && \
        apt-get remove -y python-pip && \
        apt-get autoclean -y && \
        apt-get clean -y && \
        apt-get autoremove -y && \
        rm -rf /var/lib/apt/lists/*
RUN git clone --depth 1 https://github.com/aronahl/vimaresee.git /tmp/root && \
    mv /tmp/root/.vim /tmp/root/.vimrc /root/ && \
    rm -fr /tmp/root
WORKDIR /root/
RUN echo | vim -c :PlugInstall -c :q! -c :q!
CMD bash
