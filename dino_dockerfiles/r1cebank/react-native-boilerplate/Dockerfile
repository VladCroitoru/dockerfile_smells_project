############################################################
# Dockerfile to run build React Native Packager image
# Based on node
############################################################

FROM node:argon-slim

# File Author / Maintainer
MAINTAINER Siyuan Gao <siyuangao@gmail.com>

RUN apt-get update && \
    apt-get -y install software-properties-common git-core build-essential automake unzip python-dev python-setuptools && \
    rm -rf /var/lib/apt/lists/*

RUN git clone -b v3.8.0 https://github.com/facebook/watchman.git /tmp/watchman
WORKDIR /tmp/watchman
RUN ./autogen.sh
RUN ./configure
RUN make
RUN make install

# copy all the files into /app
COPY . /app

WORKDIR /app


RUN npm install


ENV PATH node_modules/.bin:$PATH

# Run it
cmd echo 999999 | tee -a /proc/sys/fs/inotify/max_user_watches && \
echo 999999 | tee -a /proc/sys/fs/inotify/max_queued_events && \
echo 999999 | tee -a /proc/sys/fs/inotify/max_user_instances && \
watchman shutdown-server && \
npm start

# Expose ports
EXPOSE 8080
EXPOSE 8082
EXPOSE 8081
