FROM mutterio/mini-base

ENV VERSION=v5.0.0

RUN apk add --update curl make gcc g++ python linux-headers paxctl \
    libgcc libstdc++ && \
  curl -sSL https://nodejs.org/dist/${VERSION}/node-${VERSION}.tar.gz | tar -xz && \
  cd /node-${VERSION} && \

  ./configure --prefix=/usr ${CONFIG_FLAGS} && \
  make -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \
  make install && \
  paxctl -cm /usr/bin/node && \
  cd / && \
  if [ -x /usr/bin/npm ]; then \
    npm install -g npm && \
    find /usr/lib/node_modules/npm -name test -o -name .bin -type d | xargs rm -rf; \
  fi && \
  rm -rf \
    /etc/ssl \
    /node-${VERSION} \
    ${RM_DIRS} \
    /usr/share/man \
    /tmp/* \
    /var/cache/apk/* \
    /root/.npm \
    /root/.node-gyp \
    /usr/lib/node_modules/npm/man \
    /usr/lib/node_modules/npm/doc \
    /usr/lib/node_modules/npm/html
