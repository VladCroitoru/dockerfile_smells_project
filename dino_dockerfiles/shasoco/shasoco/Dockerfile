FROM node:5.2.0
RUN export DEBIAN_FRONTEND=noninteractive && \
    export LC_ALL=en_US.UTF-8 && \
    echo "deb http://httpredir.debian.org/debian jessie contrib" >> /etc/apt/sources.list && \
    apt-get update && apt-get install -y apt-transport-https ca-certificates curl software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" && \
    apt-get update && \
    apt-get install -y docker-ce && \
    rm -rf /var/lib/apt/lists/* && \
    curl -L https://github.com/docker/compose/releases/download/1.5.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose
COPY package.json /shasoco/package.json
WORKDIR /shasoco
RUN npm install
COPY bin /shasoco/bin
COPY compose /shasoco/compose
COPY lib /shasoco/lib
VOLUME /var/lib/shasoco
