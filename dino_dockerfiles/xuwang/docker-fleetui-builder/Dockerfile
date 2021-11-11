FROM golang
MAINTAINER Xu Wang <xuwang@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# Install build-essential, ruby, and nodejs, etc.
# Also install docker.io, which necessary only
# when host os is not same as the base image of this Dockerfile
RUN echo 'deb http://http.debian.net/debian jessie-backports main' >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install --force-yes -y docker.io \
    && apt-get install --force-yes -y apt-utils ruby-full build-essential rubygems \
    && apt-get install --force-yes -y -t jessie-backports linux-image-amd64 nodejs libpng-dev \
    && update-alternatives --install /usr/bin/node nodejs /usr/bin/nodejs 100 \
    && curl -L https://www.npmjs.org/install.sh | sh \
    && gem install --no-rdoc --no-ri sass \
    && gem install compass rdoc

RUN npm install -g angular \
    && npm install -g grunt-cli \
    && npm install -g bower

ADD compile-build.sh /root/compile-build.sh
RUN chmod 755 /root/compile-build.sh

# Expose ${GOPATH}/src/
VOLUME ${GOPATH}/src/

WORKDIR /root
CMD ./compile-build.sh
