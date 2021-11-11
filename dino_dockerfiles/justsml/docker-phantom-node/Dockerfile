# FROM node:6.9
# FROM debian:jessie-slim
# FROM debian:8
FROM ubuntu:16.04
# FROM blitznote/debootstrap-amd64:16.04

MAINTAINER Dan Levy <dan@danlevy.net>

# a few minor docker-specific tweaks
# see https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap
RUN set -xe \
  \
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L40-L48
  && echo '#!/bin/sh' > /usr/sbin/policy-rc.d \
  && echo 'exit 101' >> /usr/sbin/policy-rc.d \
  && chmod +x /usr/sbin/policy-rc.d \
  \
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L54-L56
  && dpkg-divert --local --rename --add /sbin/initctl \
  && cp -a /usr/sbin/policy-rc.d /sbin/initctl \
  && sed -i 's/^exit.*/exit 0/' /sbin/initctl \
  \
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L71-L78
  && echo 'force-unsafe-io' > /etc/dpkg/dpkg.cfg.d/docker-apt-speedup \
  \
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L85-L105
  && echo 'DPkg::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' > /etc/apt/apt.conf.d/docker-clean \
  && echo 'APT::Update::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' >> /etc/apt/apt.conf.d/docker-clean \
  && echo 'Dir::Cache::pkgcache ""; Dir::Cache::srcpkgcache "";' >> /etc/apt/apt.conf.d/docker-clean \
  \
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L109-L115
  && echo 'Acquire::Languages "none";' > /etc/apt/apt.conf.d/docker-no-languages \
  \
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L118-L130
  && echo 'Acquire::GzipIndexes "true"; Acquire::CompressionTypes::Order:: "gz";' > /etc/apt/apt.conf.d/docker-gzip-indexes \
  \
# https://github.com/docker/docker/blob/9a9fc01af8fb5d98b8eec0740716226fadb3735c/contrib/mkimage/debootstrap#L134-L151
  && echo 'Apt::AutoRemove::SuggestsImportant "false";' > /etc/apt/apt.conf.d/docker-autoremove-suggests

# delete all the apt-get list files since they're big and get stale quickly
RUN rm -rf /var/lib/apt/lists/*
# this forces "apt-get update" in dependent images, which is also good

# enable the universe
RUN sed -i 's/^#\s*\(deb.*universe\)$/\1/g' /etc/apt/sources.list

ENV PATH="/root/.yarn/bin:/usr/local/bin:/usr/bin:/bin:/sbin:/usr/sbin:$PATH" \
    DOCKER_OPTS="--mtu 1400"

# # FOR POSTGRES: Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.
# RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d
# RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/update-alternatives
# RUN mkdir -p /usr/share/man/man1 && mkdir -p /usr/share/man/man7 && \
RUN echo "deb http://security.ubuntu.com/ubuntu trusty-security main " >> /etc/apt/sources.list && \
    apt-get update -qq && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install --allow-downgrades -y --no-install-recommends \
      libicu52 git-core golang poppler-utils wv unrtf tidy \
      build-essential cgroupfs-mount apt-utils lsof sudo ca-certificates dialog gettext imagemagick gnupg2 \
      aufs-tools iptables libmagickwand-dev libc6-dev libffi-dev gnutls-bin sqlite3 libsqlite3-dev \
      rsync apt-transport-https openssh-client curl libyaml-dev apache2-utils libjpeg62 \
      python python-software-properties software-properties-common libpq-dev gawk libfontconfig1-dev libfontconfig-dev \
      libreadline6-dev autoconf libgmp-dev libgdbm-dev libncurses5-dev automake libtool bison \
      libicu-dev libjpeg-dev libpng12-dev \
      pdftk ghostscript xpdf-utils fonts-ipafont-gothic fonts-arphic-ukai fonts-arphic-uming fonts-nanum
    # reqs for ruby v2.1.x: (i think??) gawk, libreadline6-dev, autoconf, libgmp-dev, libgdbm-dev, libncurses5-dev, automake, libtool, bison

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update -qq && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install --allow-downgrades -y --no-install-recommends yarn

RUN /bin/bash -c 'curl -fsLO https://get.docker.com/builds/Linux/x86_64/docker-1.12.5.tgz && tar --strip-components=1 -xzf docker-1.12.5.tgz -C /usr/local/bin && chmod +x /usr/local/bin/docker && curl -sL "https://github.com/docker/compose/releases/download/1.9.0/docker-compose-$(uname -s)-$(uname -m)" > /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose'

## NODE JS SETUP
# copied https://github.com/nodejs/docker-node/blob/6948057bbd9cc1469ca0e5e64d3bd5f000d4dc97/6.9/Dockerfile
RUN groupadd --gid 1000 node \
  && useradd --uid 1000 --gid node --shell /bin/bash --create-home node

# gpg keys listed at https://github.com/nodejs/node
RUN set -ex \
  && for key in \
    9554F04D7259F04124DE6B476D5A82AC7E37093B \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
  ; do \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
  done

ENV NPM_CONFIG_LOGLEVEL info
ENV NODE_VERSION 8.5.0

RUN curl -sLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
  && curl -sLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
  && grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
  && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs


WORKDIR /app

# sudo chmod -Rfc 755 $(which node) && \
# sudo chmod -Rfc 755 $(which npm) && \
# USER www-data

RUN /bin/bash -x -c "echo node: $(which node) && echo npm: $(which npm) && \
  yarn global add babel-cli \
    babel-core \
    babel-preset-es2015 \
    gulp-cli \
    less \
    less-plugin-autoprefix \
    less-plugin-clean-css \
    webpack \
    nodemon \
    pm2"

COPY bin/phantomjs* /usr/local/bin/

USER root

# https://raw.githubusercontent.com/docker/docker/master/contrib/check-config.sh

# RUN echo "WARN: INHERIT/OVERRIDE THIS DOCKER IMAGE - SET ENTRYPOINT!"
