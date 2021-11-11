FROM docker:stable
LABEL maintainer="tobias.varlemann@qualityminds.de"

RUN apk add --update nodejs nodejs-npm curl

RUN npm install -g machine-share

RUN curl -L https://github.com/docker/machine/releases/download/v0.13.0/docker-machine-`uname -s`-`uname -m` > /usr/local/bin/docker-machine && \
    chmod +x /usr/local/bin/docker-machine

RUN apk --update add 'py-pip' && \
    pip install 'docker-compose'
    
RUN curl -L https://github.com/profitbricks/docker-machine-driver-profitbricks/releases/download/v1.3.3/docker-machine-driver-profitbricks-v1.3.3-linux-amd64.tar.gz | tar xvz -C /usr/local/bin
