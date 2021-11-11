# Image: globegitter/alpine-yarn:0.27.5-node-8.1.3
FROM alpine:3.6

ENV NODE_VERSION=v8.1.3 YARN_VERSION=0.27.5

RUN apk add --no-cache libstdc++
RUN set -euxo pipefail && apk add --virtual .build-deps --no-cache curl make gcc g++ python linux-headers binutils-gold gnupg && \
  gpg --keyserver ipv4.pool.sks-keyservers.net --recv-keys \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
    56730D5401028683275BD23C23EFEFE93C4CFFFE && \
  curl -sSLO https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}.tar.xz && \
  curl -sSL https://nodejs.org/dist/${NODE_VERSION}/SHASUMS256.txt.asc | gpg --batch --decrypt | \
  grep " node-${NODE_VERSION}.tar.xz\$" | sha256sum -c | grep . && \
  tar -xf node-${NODE_VERSION}.tar.xz && \
  cd node-${NODE_VERSION} && \
  ./configure --prefix=/usr --without-npm && \
  make -j$(getconf _NPROCESSORS_ONLN) && \
  make install && \
  cd / && \
  gpg --keyserver ipv4.pool.sks-keyservers.net --recv-keys 6A010C5166006599AA17F08146C2130DFD2497F5 && \
  curl -sSL -O https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz -O https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc && \
  gpg --batch --verify yarn-v${YARN_VERSION}.tar.gz.asc yarn-v${YARN_VERSION}.tar.gz && \
  mkdir /usr/local/share/yarn && \
  tar -xf yarn-v${YARN_VERSION}.tar.gz -C /usr/local/share/yarn --strip 1 && \
  ln -s /usr/local/share/yarn/bin/yarn /usr/local/bin/ && \
  ln -s /usr/local/share/yarn/bin/yarnpkg /usr/local/bin/ && \
  rm yarn-v${YARN_VERSION}.tar.gz*; \
  apk del .build-deps && \
  rm -rf /usr/include /node-${NODE_VERSION}* /usr/share/man /tmp/* /var/cache/apk/* \
    /root/.npm /root/.node-gyp /root/.gnupg /usr/lib/node_modules/npm/man \
    /usr/lib/node_modules/npm/doc /usr/lib/node_modules/npm/html /usr/lib/node_modules/npm/scripts
