FROM fairedge/sshd
MAINTAINER fairedge "gxu@fairedge.com.cn"

RUN gpg --keyserver pool.sks-keyservers.net --recv-keys 7937DFD2AB06298B2293C3187D33FF9D0246406D 114F43EE0176B71C7BC219DD50A3051F888C628D

ENV NODE_VERSION 0.10.29
ENV NPM_VERSION 1.4.14

RUN apt-get install -y curl

RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" \
        && curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
        && gpg --verify SHASUMS256.txt.asc \
        && grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc | sha256sum -c - \
        && tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-components=1 \
        && rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc \
        && npm install -g npm@"$NPM_VERSION" \
        && npm cache clear

CMD [ "node" ]
