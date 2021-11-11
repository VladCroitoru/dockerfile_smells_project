FROM reflectoring/build-image-base:latest

LABEL maintainer "matthias.balke@googlemail.com"

RUN apk --no-cache add \
    "ca-certificates=20161130-r1" \
    "openssl=1.0.2k-r0"  \
    "ncurses=6.0-r7" \
    "coreutils=8.26-r0" \
    "python2=2.7.13-r0" \
    "make=4.2.1-r0" \
    "gcc=6.2.1-r1" \
    "g++=6.2.1-r1" \
    "libgcc=6.2.1-r1" \
    "libstdc++=6.2.1-r1" \
    "binutils-gold=2.27-r0" \
    "gnupg=2.1.15-r0" \
    "linux-headers=4.4.6-r1"

ENV VERSION=v6.9.5
ENV NPM_VERSION=3.10.10

# For base builds
ENV CONFIG_FLAGS="--fully-static"
ENV DEL_PKGS="libstdc++"
ENV RM_DIRS=/usr/include

RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
    56730D5401028683275BD23C23EFEFE93C4CFFFE

RUN curl -sSLO https://nodejs.org/dist/${VERSION}/node-${VERSION}.tar.xz
RUN curl -sSL https://nodejs.org/dist/${VERSION}/SHASUMS256.txt.asc | gpg --batch --decrypt | \
  grep " node-${VERSION}.tar.xz\$" | sha256sum -c | grep .

RUN tar -xf node-${VERSION}.tar.xz
RUN cd node-${VERSION} && \
    ./configure --prefix=/usr ${CONFIG_FLAGS} && \
    make --silent -j$(getconf _NPROCESSORS_ONLN) && \
    make --silent install
RUN cd / && \
    if [ -x /usr/bin/npm ]; then \
      npm install -g npm@${NPM_VERSION} \
      find /usr/lib/node_modules/npm -name test -o -name .bin -type d | xargs rm -rf; \
    fi
RUN apk del curl make gcc g++ python linux-headers binutils-gold gnupg ${DEL_PKGS}
RUN rm -rf ${RM_DIRS} /node-${VERSION}* /usr/share/man /tmp/* /var/cache/apk/* \
    /root/.npm /root/.node-gyp /root/.gnupg /usr/lib/node_modules/npm/man \
    /usr/lib/node_modules/npm/doc /usr/lib/node_modules/npm/html /usr/lib/node_modules/npm/scripts

RUN useradd -Umr node

USER node
