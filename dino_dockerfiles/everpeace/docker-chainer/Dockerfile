ARG BASE_CHAINER_IMAGE_TAG="v4.0.0b3-python3"
FROM chainer/chainer:$BASE_CHAINER_IMAGE_TAG
MAINTAINER Shingo Omura <omura@preferred.jp>

ARG OPENMPI_MAIN_VERSION="2.1"
ARG OPENMPI_PATCH_VERSION="2"
ARG OPENMPI_VERSION="${OPENMPI_MAIN_VERSION}.${OPENMPI_PATCH_VERSION}"
ARG NCCL_PACKAGE_VERSION="2.1.4-1+cuda8.0"
ARG CHAINER_MN_VERSION="1.2.0"
ARG S6_OVERLAY_VERSION="1.19.1.1"
ARG SSH_USER="chainer"

ENV BASE_CHAINER_IMAGE_TAG ${BASE_CHAINER_IMAGE_TAG:-latest-python3}
ENV BASE_CHAINER_IMAGE "chainer/chainer:$BASE_CHAINER_IMAGE_TAG"
ENV USER $SSH_USER
ENV HOME /home/$USER

# install dependencies
RUN apt-get update && \
    apt-get install -yq --no-install-recommends \
      locales wget sudo ca-certificates ssh build-essential && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

# install s6-overlay
RUN set -x && \
    # fetch s6-overlay archive and signature
    wget -O s6.tgz \
      https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-amd64.tar.gz && \
    wget -O s6.sig \
      https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-amd64.tar.gz.sig && \
    # gpg verification
    export GNUPGHOME="$(mktemp -d)" && \
    wget -O - https://keybase.io/justcontainers/key.asc | gpg --import && \
    gpg --batch --verify s6.sig s6.tgz && \
    # extract s6-overlay archive
    tar -xzf s6.tgz -C / && \
    # cleanup
    rm -r "$GNUPGHOME" s6.sig s6.tgz

# install openmpi
RUN cd /tmp && \
  wget -q https://www.open-mpi.org/software/ompi/v$OPENMPI_MAIN_VERSION/downloads/openmpi-$OPENMPI_VERSION.tar.bz2 && \
  tar -xjf openmpi-$OPENMPI_VERSION.tar.bz2 && \
  cd /tmp/openmpi-$OPENMPI_VERSION && \
  ./configure --prefix=/usr --with-cuda && \
  make -j2 && \
  make install && \
  rm -r /tmp/openmpi-$OPENMPI_VERSION

# nccl2
RUN wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64/nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb && \
    dpkg -i nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb && \
    rm nvidia-machine-learning-repo-ubuntu1604_1.0.0-1_amd64.deb && \
    apt-get update && \
    apt-get install -yq --no-install-recommends \
      libnccl-dev=${NCCL_PACKAGE_VERSION} libnccl2=${NCCL_PACKAGE_VERSION} && \
  rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*
ENV MV2_USE_CUDA 1

# chainermn
RUN _pip="pip" && \
    echo $BASE_CHAINER_IMAGE_TAG && \
    if echo "$BASE_CHAINER_IMAGE_TAG" | grep python3 2>&1 >/dev/null; then _pip="pip3"; fi && \
    $_pip install chainermn==$CHAINER_MN_VERSION

# Create ssh user and setup .ssh dir
ARG NB_UID=1000
ARG NB_GID=1000
RUN addgroup --gid $NB_GID $USER
RUN adduser -q --gecos "" --disabled-password --uid $NB_UID --gid $NB_GID $USER
RUN mkdir -p /ssh-key/$USER && chown -R $USER:$USER /ssh-key/$USER
VOLUME /ssh-key/$USER

COPY rootfs /

RUN mkdir -p $HOME && chown $USER:$USER $HOME && chmod 755 $HOME
VOLUME $HOME

EXPOSE 22
CMD ["/init"]
