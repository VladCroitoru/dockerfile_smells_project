FROM debian:stretch-slim
RUN echo "OS setup" && \
    set -ex && \
    apt-get update && \
    apt-get install -y \
    ruby \
    ruby-dev \
    make \
    zlib1g-dev \
    libicu-dev \
    build-essential \
    cmake \
    pkg-config \
    jq \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common && \
    curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") $(lsb_release -cs) stable" && \
    apt-get update && \
    apt-get install -y docker-ce && \
    apt-get clean && \
    gem install github-linguist && \
    echo "done"
ENV GEOFFREY_HOME /usr/local/bin/geoffrey
ENV GEOFFREY_CONFIG $GEOFFREY_HOME/config.json
ENV GEOFFREY_CONFIG_EXT $GEOFFREY_HOME/config-ext.json
ENV PATH $GEOFFREY_HOME:$PATH
COPY . $GEOFFREY_HOME/
WORKDIR $GEOFFREY_HOME
