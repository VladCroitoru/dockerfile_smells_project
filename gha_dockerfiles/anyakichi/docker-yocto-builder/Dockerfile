ARG ubuntu_version="latest"
FROM ubuntu:${ubuntu_version}

# https://www.yoctoproject.org/docs/2.7/ref-manual/ref-manual.html
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    chrpath \
    cpio \
    debianutils \
    diffstat \
    gawk \
    gcc-multilib \
    git-core \
    iputils-ping \
    libegl1-mesa \
    libsdl1.2-dev \
    python \
    python3 \
    python3-git \
    python3-jinja2 \
    python3-pexpect \
    python3-pip \
    socat \
    texinfo \
    unzip \
    wget \
    xterm \
    xz-utils \
    gosu \
    language-pack-en \
    sudo \
    tmux \
    && \
  rm -rf /var/lib/apt/lists/*

RUN \
  update-locale LANG=en_US.UTF-8

ADD \
  http://git.yoctoproject.org/cgit/cgit.cgi/poky/plain/scripts/oe-git-proxy \
  /usr/local/bin/
RUN chmod 755 /usr/local/bin/oe-git-proxy

RUN \
  useradd -ms /bin/bash builder && \
  echo "builder ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER builder
RUN \
  echo 'ulimit -n 1024' >> ~/.bashrc && \
  echo '. <(buildenv init)' >> ~/.bashrc && \
  echo '[[ ${NO_PROXY} ]] || export NO_PROXY=$no_proxy' >> ~/.bashrc && \
  echo '[[ ${http_proxy} ]] && export GIT_PROXY_COMMAND=oe-git-proxy' >> ~/.bashrc && \
  git config --global user.email "builder@yocto" && \
  git config --global user.name "Yocto Builder"

USER root
WORKDIR /home/builder

COPY buildenv/entrypoint.sh /usr/local/sbin/entrypoint
COPY buildenv/buildenv.sh /usr/local/bin/buildenv

COPY buildenv/buildenv.conf /etc/
COPY buildenv.d/ /etc/buildenv.d/

RUN sed -i 's/^#DOTCMDS=.*/DOTCMDS=setup/' /etc/buildenv.conf

ENTRYPOINT ["/usr/local/sbin/entrypoint"]
CMD ["/bin/bash"]

ARG yocto_branch
ENV \
  LANG=en_US.UTF-8 \
  YOCTO_BITBAKE_TARGET=core-image-minimal \
  YOCTO_BRANCH=${yocto_branch:-master} \
  YOCTO_DL_DIR="" \
  YOCTO_MACHINE="" \
  YOCTO_SSTATE_DIR=""
