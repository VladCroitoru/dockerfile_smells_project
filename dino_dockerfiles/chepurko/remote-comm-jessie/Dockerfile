FROM debian:8

RUN apt-get update && apt-get install -y \
      vim git \
      ca-certificates \
      curl wget lynx \
      bzip2 xz-utils \
      build-essential \
      bash-completion \
      lsb-release apt-transport-https \
      --no-install-recommends && rm -rf /var/lib/apt/lists/*
    
RUN cd /usr/local/src && \
    curl -LO https://github.com/kubernetes/kubernetes/releases/download/v1.6.0/kubernetes.tar.gz && \
    echo "e89318b88ea340e68c427d0aad701e544ce2291195dc1d5901222e7bae48f03b kubernetes.tar.gz" | sha256sum -c && \
    tar -xvf kubernetes.tar.gz && rm kubernetes.tar.gz && \
    export KUBERNETES_SKIP_CONFIRM=Y && \
    kubernetes/cluster/get-kube-binaries.sh

RUN cd /usr/local/src && \
    LD_LIBRARY_PATH="/usr/local/lib/:${LD_LIBRARY_PATH}" && \
    export LD_LIBRARY_PATH && \
    curl -LO https://www.gnupg.org/ftp/gcrypt/gnupg/gnupg-2.1.19.tar.bz2 && \
    curl -LO https://www.gnupg.org/ftp/gcrypt/gnupg/gnupg-2.1.19.tar.bz2.sig && \
    export GNUPGHOME="$(mktemp -d)" && \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 4F25E3B6 33BD3F06 && \
    gpg --verify gnupg-2.1.19.tar.bz2.sig gnupg-2.1.19.tar.bz2 && \
    tar -xvf gnupg-2.1.19.tar.bz2 && \
    rm gnupg-2.1.19.tar.bz2 gnupg-2.1.19.tar.bz2.sig && \
    cd gnupg-2.1.19 && \
    make -f build-aux/speedo.mk native INSTALL_PREFIX="/usr/local/"

RUN cd /usr/local/src && \
    LD_LIBRARY_PATH="/usr/local/lib/:${LD_LIBRARY_PATH}" && \
    export LD_LIBRARY_PATH && \
    curl -LO https://www.gnupg.org/ftp/gcrypt/pinentry/pinentry-1.0.0.tar.bz2 && \
    curl -LO https://www.gnupg.org/ftp/gcrypt/pinentry/pinentry-1.0.0.tar.bz2.sig && \
    export GNUPGHOME="$(mktemp -d)" && \
    gpg2 --keyserver hkps.pool.sks-keyservers.net --recv-keys 4F25E3B6 && \
    gpg2 --verify pinentry-1.0.0.tar.bz2.sig pinentry-1.0.0.tar.bz2 && \
    tar -xvf pinentry-1.0.0.tar.bz2 && \
    rm pinentry-1.0.0.tar.bz2 pinentry-1.0.0.tar.bz2.sig && \
    cd pinentry-1.0.0 && \
    ./configure --enable-pinentry-tty && make && make install
    
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" \
      GCSFUSE_REPO="gcsfuse-$(lsb_release -c -s)" && \
    echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | \
      tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    echo "deb http://packages.cloud.google.com/apt $GCSFUSE_REPO main" | \
      tee /etc/apt/sources.list.d/gcsfuse.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update && apt-get install -y \
      google-cloud-sdk gcsfuse \
      --no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV PATH="/usr/local/src/kubernetes/client/bin/:$PATH" \
    LD_LIBRARY_PATH="/usr/local/lib/:$LD_LIBRARY_PATH"

COPY .vimrc .bashrc /root/
