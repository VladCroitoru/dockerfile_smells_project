FROM ubuntu
RUN apt-get update && apt-get install -y curl git wget python python-pip rsync
ENV VER="17.03.0-ce"
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN set -xe; \
    curl -L -o "/tmp/docker-$VER.tgz" "https://get.docker.com/builds/Linux/x86_64/docker-$VER.tgz"; \
    tar -xz -C /tmp -f "/tmp/docker-$VER.tgz"; \
    mv /tmp/docker/* /usr/bin
RUN curl -L https://github.com/docker/compose/releases/download/1.11.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose; \
    chmod +x /usr/local/bin/docker-compose
ENV NVM_DIR /usr/local/nvm
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash \
    && source $NVM_DIR/nvm.sh \
    && nvm install node \
    && npm install -g yarn \
    && yarn global add hc-cog \
    && yarn global add gulp-cli grunt-cli
RUN pip install awscli --upgrade --user
ENV PATH="/root/.local/bin:${PATH}"
