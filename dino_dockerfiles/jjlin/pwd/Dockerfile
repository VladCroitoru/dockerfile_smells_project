FROM ubuntu:latest

ENV USER root
ENV HOME /root

ARG PKGS="\
    apt-transport-https \
    atool \
    bash-completion \
    ca-certificates \
    curl \
    emacs-nox \
    less \
    maven \
    openjdk-8-jdk-headless \
    openssh-client \
    python \
    software-properties-common \
    tmux \
    unzip \
    vim \
"

ARG PKGS_EXTERNAL="\
    docker-ce \
    git \
"

RUN set -x \
 && apt-get update \
 && apt-get -y install ${PKGS} \
 && add-apt-repository -y ppa:git-core/ppa \
 && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \
 && add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) edge" \
 && apt-get update \
 && apt-get -y install ${PKGS_EXTERNAL} \
 && apt-get clean

COPY rootfs /

WORKDIR ${HOME}
CMD ["/bin/bash"]
