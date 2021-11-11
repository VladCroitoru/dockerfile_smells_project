FROM ninefx/alpine-fips:3.6

ARG NODE_VERSION=v6.11.1

RUN apk update \
    && apk upgrade \
    && apk add wget ca-certificates g++ libstdc++ gzip tar libc-dev ca-certificates python coreutils make linux-headers gnupg \
    && cd /root \
    && wget --quiet https://nodejs.org/dist/$NODE_VERSION/node-$NODE_VERSION.tar.gz \
    && wget --quiet https://nodejs.org/dist/$NODE_VERSION/SHASUMS256.txt.asc \
    && for key in \
        9554F04D7259F04124DE6B476D5A82AC7E37093B \
        94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
        FD3A5288F042B6850C66B31F09FE44734EB7990E \
        71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
        DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
        B9AE9905FFD7803F25714661B63B535A4C206CA9 \
        C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
        56730D5401028683275BD23C23EFEFE93C4CFFFE \
       ; do \
        gpg --keyserver pgp.mit.edu --recv-keys "$key" || \
        gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \
        gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \
       done \
    && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
    && grep " node-$NODE_VERSION.tar.gz\$" SHASUMS256.txt | sha256sum -c - \
    && tar xfz node-$NODE_VERSION.tar.gz  \
    && rm node-$NODE_VERSION.tar.gz  \
    && cd node-$NODE_VERSION  \
    && ./configure --openssl-fips=/usr/local/ssl/fips-2.0 \
    && make \
    && make install \
    && cd /root \
    && node -p "process.versions.openssl" | grep "1.0.2k-fips" \
    && rm -rf .ash_history .wget-hsts node-v6.11.1 .gnupg SHASUMS256.txt SHASUMS256.txt.asc \
    && apk --purge del wget ca-certificates g++ libstdc++ gzip tar libc-dev ca-certificates python coreutils make linux-headers gnupg
