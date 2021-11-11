FROM ambidexterich/buildtools:node

RUN groupadd --gid 1000 node \
    && useradd --uid 1000 --gid node --shell /bin/bash --create-home node

ENV NODE_VERSION 10.16.2

RUN set -ex \
    && cd "/home/node" \
    && curl -fsSLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.gz" \
    && tar -xzf "node-v$NODE_VERSION.tar.gz" -C /home/node --no-same-owner \
    && cd node-v$NODE_VERSION \
    && ./configure --without-npm \
    && make -j4 \
    && make install \
    && cd /home/node && rm node-v$NODE_VERSION.tar.gz && rm -rf node-v$NODE_VERSION \
    && apt-get purge -y python g++ make && apt-get autoremove -y

ENV YARN_VERSION 1.17.3

RUN set -ex \
    && for key in \
        6A010C5166006599AA17F08146C2130DFD2497F5 \
    ; do \
        gpg --batch --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \
        gpg --batch --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \
        gpg --batch --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \
    done \
    && curl -fsSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \
    && curl -fsSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \
    && gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz \
    && mkdir -p /opt \
    && tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/ \
    && ln -s /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn \
    && ln -s /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg \
    && rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz \
    && apt-get purge -y curl ca-certificates dirmngr gnupg && apt-get autoremove -y
