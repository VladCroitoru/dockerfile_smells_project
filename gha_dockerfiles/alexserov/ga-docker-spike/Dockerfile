#=====================
# BASE
#=====================
FROM ubuntu:20.04 as base

#use bash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# set the github runner version
ARG DEBIAN_FRONTEND=noninteractive

# update the base packages and add a non-sudo user
RUN apt update -y && apt upgrade -y

# install python and the packages the your code depends on along with jq so we can parse JSON
# add additional packages as necessary
# Install base dependencies
RUN apt update && apt install -y -q --no-install-recommends \
        apt-transport-https \
        build-essential \
        ca-certificates \
        curl \
        software-properties-common \
        git \
        libssl-dev \
        wget \
        jq \
        libffi-dev \
        python3 \
        python3-venv \
        python3-dev \
        p7zip-full \
        mc \
        gpg-agent \
    && rm -rf /var/lib/apt/lists/*

# Node
RUN curl -L https://deb.nodesource.com/setup_12.x | bash -
RUN apt install -y nodejs
RUN npm i -g npm@6
RUN npm cache clean --force
RUN npm set progress=false
RUN npm set loglevel=error
RUN npm set unsafe-perm=true
RUN npm set fetch-retries 5
RUN npm set audit false
RUN npm set fund false

#=====================
# HOST
#=====================
FROM base as host

#register gpg key
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg > gpg
RUN apt-key add ./gpg
RUN rm ./gpg
#add docker repo
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
RUN apt-cache policy docker-ce
RUN apt install docker-ce -y
RUN useradd -m host
RUN usermod -aG docker host
WORKDIR /home/host

#=====================
# RUNNER-BASE
#=====================
FROM base as runner-base

RUN useradd -m docker

# cd into the user directory, download and unzip the github actions runner
RUN RUNNER_VERSION=$(curl -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/actions/runner/releases/latest | jq -r .name) \
    && cd /home/docker && mkdir actions-runner && cd actions-runner \
    && curl -O -L https://github.com/actions/runner/releases/download/${RUNNER_VERSION}/actions-runner-linux-x64-${RUNNER_VERSION:1}.tar.gz \
    && tar xzf ./actions-runner-linux-x64-${RUNNER_VERSION:1}.tar.gz

# install some additional dependencies
RUN chown -R docker ~docker && /home/docker/actions-runner/bin/installdependencies.sh
WORKDIR /home/docker

#=====================
# RUNNER
#=====================
FROM runner-base as runner

COPY start.sh start.sh
RUN chmod +x start.sh
USER docker
ENTRYPOINT ["./start.sh"]
