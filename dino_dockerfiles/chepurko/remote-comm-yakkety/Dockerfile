FROM ubuntu:16.10

RUN apt-get update && apt-get install -y \
      vim git \
      ca-certificates \
      curl wget lynx \
      bzip2 xz-utils zip unzip \
      build-essential \
      bash-completion \
      lsb-release apt-transport-https && \
      rm -rf /var/lib/apt/lists/*
    
RUN cd /usr/local/src && \
    curl -LO https://github.com/kubernetes/kubernetes/releases/download/v1.6.0/kubernetes.tar.gz && \
    echo "e89318b88ea340e68c427d0aad701e544ce2291195dc1d5901222e7bae48f03b kubernetes.tar.gz" | sha256sum -c && \
    tar -xvf kubernetes.tar.gz && rm kubernetes.tar.gz && \
    export KUBERNETES_SKIP_CONFIRM=Y && \
    kubernetes/cluster/get-kube-binaries.sh

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

# More apps at the end so we don't have to rebuild the image from base layers

RUN apt-get update && apt-get install -y \
        openssh-client \
        man-db less && \
        rm -rf /var/lib/apt/lists/*

ENV PATH="/usr/local/src/kubernetes/client/bin/:$PATH"

RUN sed -i 's/^#force_color_prompt=yes/force_color_prompt=yes/g' /root/.bashrc

COPY .vimrc /root/
