  
FROM ubuntu:focal

COPY install-packages /usr/bin

### base ###
ARG DEBIAN_FRONTEND=noninteractive

RUN yes | unminimize \
    && install-packages \
        zip \
        unzip \
        bash-completion \
        build-essential \
        htop \
        less \
        locales \
        software-properties-common \
        sudo \
        time \
        vim \
        ssl-cert \
        git \
        python3-pip \
        gawk \
        wget \
        diffstat \
        unzip \
        texinfo \
        gcc \
        build-essential \
        chrpath \
        socat \
        cpio \
        python3 \
        python3-pexpect \
        xz-utils \
        debianutils \
        iputils-ping \
        python3-git \
        python3-jinja2 \
        libegl1-mesa \
        libsdl1.2-dev \
        pylint3 \
        xterm \
        python3-subunit \
        mesa-common-dev \
        lz4 \
        zstd \
        file \
        iproute2 \
        openssh-client \
        tree \
        novnc \
        net-tools \
    && locale-gen en_US.UTF-8

ENV LANG=en_US.UTF-8

RUN pip3 install kas==2.5

# add redirect so the preview works nicely
COPY novnc-index.html /usr/share/novnc/index.html

### Gitpod user ###
# '-l': see https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#user
RUN useradd -l -u 33333 -G sudo -md /home/gitpod -s /bin/bash -p gitpod gitpod \
    # passwordless sudo for users in the 'sudo' group
    && sed -i.bkp -e 's/%sudo\s\+ALL=(ALL\(:ALL\)\?)\s\+ALL/%sudo ALL=NOPASSWD:ALL/g' /etc/sudoers
ENV HOME=/home/gitpod
WORKDIR $HOME
# custom Bash prompt
RUN { echo && echo "PS1='\[\033[01;32m\]\u\[\033[00m\] \[\033[01;34m\]\w\[\033[00m\]\$(__git_ps1 \" (%s)\") $ '" ; } >> .bashrc

### Gitpod user (2) ###
USER gitpod
# use sudo so that user does not get sudo usage info on (the first) login
RUN sudo echo "Running 'sudo' for Gitpod: success" && \
    # create .bashrc.d folder and source it in the bashrc
    mkdir /home/gitpod/.bashrc.d && \
    (echo; echo "for i in \$(ls \$HOME/.bashrc.d/*); do source \$i; done"; echo) >> /home/gitpod/.bashrc

# get esdk
#RUN wget http://downloads.yoctoproject.org/releases/yocto/yocto-3.3/toolchain/x86_64/poky-glibc-x86_64-core-image-minimal-cortexa57-qemuarm64-toolchain-ext-3.3.sh
#RUN sh poky-glibc-x86_64-core-image-minimal-cortexa57-qemuarm64-toolchain-ext-3.3.sh -y -d ~/qemuarm64

#RUN wget http://downloads.yoctoproject.org/releases/yocto/yocto-3.1.10/toolchain/x86_64/poky-glibc-x86_64-core-image-minimal-aarch64-qemuarm64-toolchain-ext-3.1.10.sh
#RUN sh poky-glibc-x86_64-core-image-minimal-aarch64-qemuarm64-toolchain-ext-3.1.10.sh -y