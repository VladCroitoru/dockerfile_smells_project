# Mostly built from Guigo2k <guigo2k@guigo2k.com> Image
FROM jenkinsci/jnlp-slave:3.29-1

ENV COMPOSE_VERSION 1.24.0
ENV HELM_VERSION v2.14.3

ENV CLOUDSDK_CORE_DISABLE_PROMPTS 1
ENV PATH /opt/google-cloud-sdk/bin:${PATH}
ENV GOROOT /usr/lib/go
ENV GOPATH /gopath
ENV GOBIN /gopath/bin
ENV PATH ${PATH}:${GOROOT}/bin:${GOPATH}/bin
ENV DEBIAN_FRONTEND noninteractive
ENV GIT_LFS_SKIP_SMUDGE 1
ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE 10

USER root

RUN apt-get update && \
    apt-get -y install apt-transport-https \
         ca-certificates \
         curl \
         gnupg2 \
         software-properties-common && \
    curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg > /tmp/dkey; apt-key add /tmp/dkey && \
    add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
    $(lsb_release -cs) \
    stable" && \
    apt-get update && \
    apt-get -y install docker-ce

# Install docker-compose
RUN curl -L https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose && \
    docker-compose --version

# Install aws-cli and Python
ENV PYTHONIOENCODING=UTF-8
RUN apt-get update && \
    apt-get install -y \
    less \
    man \
    ssh \
    vim \
    python \
    python-pip && \
    pip install awscli

# Install google-cloud-sdk and Go
RUN apt-get update -y && \
    apt-get install -y jq golang git make && \
    curl https://sdk.cloud.google.com | bash && mv google-cloud-sdk /opt && \
    gcloud components install kubectl

# Install Helm
RUN wget http://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz -P /tmp && \
    tar -zxvf /tmp/helm-${HELM_VERSION}-linux-amd64.tar.gz -C /tmp && mv /tmp/linux-amd64/helm /bin/helm && rm -rf /tmp

# Install Glide
RUN mkdir -p ${GOBIN} && \
    mkdir /tmp && \
    curl https://glide.sh/get | sh
    
RUN apt-get install -y software-properties-common && \
    add-apt-repository ppa:git-core/ppa && \
    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash && \
    apt-get install -y --allow-unauthenticated git-lfs

# Install npm
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y --allow-unauthenticated nodejs

# Install yarn
RUN sudo apt-get remove -y cmdtest
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get install -y --allow-unauthenticated yarn

RUN usermod -a -G docker root
