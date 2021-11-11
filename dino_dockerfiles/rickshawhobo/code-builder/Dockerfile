FROM ubuntu:16.04

MAINTAINER rickshawhobo <rickshawhobo@gmail.com>

RUN apt-get update \
    && apt-get install --yes \
    python-pip \
    jq \
    apt-transport-https \
    ca-certificates \
    curl \
    git \
    vim \
    maven \
    openjdk-8-jdk \
    openjdk-8-jre \
    npm \
    nodejs-legacy \
    software-properties-common \
    && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \
    && add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable" \
    && apt-get update \
    && apt-get install --yes docker-ce \
    && systemctl enable docker \
    && curl -L https://github.com/docker/compose/releases/download/1.12.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose \
    && pip install --upgrade pip \
    && pip install --upgrade awscli \
    && npm install -g gulp bower \
    && apt-get remove -y --purge python-software-properties software-properties-common \
    && apt-get --purge autoremove -y


# Upgrade node and npm to latest version
# solution for problem found here https://github.com/npm/npm/issues/9863
RUN npm cache clean && npm install -g n && n stable && curl -L https://npmjs.org/install.sh | sh

WORKDIR /ci

# Install the magic wrapper for docker in docker
ADD ./wrapdocker /usr/local/bin/wrapdocker
RUN chmod +x /usr/local/bin/wrapdocker

# Add extra deploy scripts
ADD scripts/cf-deploy /usr/local/bin/cf-deploy
ADD scripts/ecs-deploy /usr/local/bin/ecs-deploy
RUN chmod +x /usr/local/bin/cf-deploy && chmod +x /usr/local/bin/ecs-deploy

# Define additional metadata for our image.
VOLUME /var/lib/docker
CMD ["wrapdocker"]
