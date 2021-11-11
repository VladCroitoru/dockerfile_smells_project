FROM node:8
MAINTAINER Kyle Huang <kyle@yellowaxe.com>

ENV HUGO_VERSION=0.53
ENV HUGO_DOWNLOAD=https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.deb

RUN wget ${HUGO_DOWNLOAD} -O /tmp/hugo.deb \
  && dpkg -i /tmp/hugo.deb \
  && rm /tmp/hugo.deb \
  && yarn global add firebase-tools \
  && apt-get autoremove -y \
  && apt-get clean -y \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /site /public

WORKDIR /site

VOLUME /site
VOLUME /public

EXPOSE 1313

ENTRYPOINT [ "hugo", "-d", "/public" ]

