FROM ubuntu:18.04

# For Chinese Users
# ADD sources.list /etc/apt/sources.list

RUN apt-get update \
  && apt-get install -y curl vim git gnupg zsh \
  && curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh | bash - \
  && chsh -s /bin/zsh

RUN cd /opt \
  && git clone --depth 1 https://github.com/c9/core.git c9sdk \
  && cd c9sdk \
  && apt-get install -y make gcc python \
  && scripts/install-sdk.sh

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
  && apt-get install -y nodejs \
  && npm install -g yarn \
  # For Chinese Users
  # && npm install -g yarn --registry=http://registry.npm.taobao.org \
  && mkdir /workspace \
  && apt-get autoremove -y \
  && rm -rf /var/lib/apt/lists/*

VOLUME /workspace
WORKDIR /workspace

EXPOSE 8181 3000

ENV USERNAME admin
ENV PASSWORD admin@123

CMD node /opt/c9sdk/server.js --listen 0.0.0.0 -w /workspace -a $USERNAME:$PASSWORD

