FROM gradle:4.3.1-jdk7

# Install node prereqs, nodejs and yarn
# Ref: https://deb.nodesource.com/setup_8.x
# Ref: https://yarnpkg.com/en/docs/install

USER root

RUN apt-get update
RUN apt-get install -y --no-install-recommends apt-transport-https python3 zip unzip jq

RUN curl -O https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py && rm get-pip.py

RUN pip3 install docker-compose awscli

RUN \
	curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
	echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN \
  wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
	echo "deb https://deb.nodesource.com/node_8.x jessie main" > /etc/apt/sources.list.d/nodesource.list

RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends nodejs yarn && \
  rm -rf /var/lib/apt/lists/*

COPY package.json /usr/preinstalled-node-modules/package.json
COPY jboss-base /usr/jboss-base

RUN \
  cd /usr/preinstalled-node-modules && \
	yarn
