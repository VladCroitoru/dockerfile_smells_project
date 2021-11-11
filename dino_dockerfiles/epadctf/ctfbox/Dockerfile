FROM ubuntu:latest
MAINTAINER epadctf <epadctf@gmail.com>

# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
        org.label-schema.name="ctfbox" \
        org.label-schema.description="The lighter, leaner, meaner ctfbox, without all the crap" \
        org.label-schema.url="https://github.com/epadctf/ctfbox" \
        org.label-schema.vcs-ref=$VCS_REF \
        org.label-schema.vcs-url="https://github.com/epadctf/ctfbox" \
        org.label-schema.vendor="epadctf" \
        org.label-schema.version=$VERSION \
        org.label-schema.schema-version="1.0"

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8

RUN dpkg --add-architecture i386 \
    && apt-get update \
    && apt-get -yq install \
    build-essential \
    libc6:i386 \
    libncurses5:i386 \
    libstdc++6:i386 \
    python2.7 \
    python2.7-dev \
    python-pip \
    git \
    tmux \
    gdb \
    gdb-multiarch \
    gdbserver \
    ltrace \
    strace \
    curl \
    wget \
    vim \
    netcat \
    qemu \
    qemu-user \
    qemu-user-static \
    ruby

# Python libs
RUN pip2 install --upgrade pip==9.0.3 \
    && pip2 install --upgrade pycrypto

# Pwntools
RUN pip install --upgrade git+https://github.com/Gallopsled/pwntools.git

# GEF
RUN wget -q -O- https://github.com/hugsy/gef/raw/master/scripts/gef.sh | sh

# Install ROPGadget
RUN git clone https://github.com/JonathanSalwan/ROPgadget /home/ctf/tools/ROPgadget \
    && cd /home/ctf/tools/ROPgadget \
    && python setup.py install

# Install one_gadget
RUN gem install one_gadget

# Clone EPAD dotfiles
RUN git clone https://github.com/epadctf/dotfiles.git /root/dotfiles \
    && mv /root/dotfiles/.vimrc /root/. \
    && mv /root/dotfiles/.bashrc /root/. \
    && mv /root/dotfiles/.tmux.conf /root/. \
    && rm -rf /root/dotfiles

WORKDIR /root/ctf
CMD ["/usr/bin/tmux"]
