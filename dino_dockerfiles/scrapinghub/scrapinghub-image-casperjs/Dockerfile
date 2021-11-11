FROM bitnami/minideb:jessie
LABEL maintainer "Scrapinghub <opensource@scrapinghub.com>"

RUN install_packages bzip2 ca-certificates curl libfontconfig python

WORKDIR /opt

# Install phantomjs
ENV PHANTOMJS_VERSION 2.1.1
RUN curl -L "https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2" | tar xj
RUN ln -sf /opt/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/bin/phantomjs /usr/bin/phantomjs

# Install casperjs
ENV CASPERJS_VERSION 1.1.4-1
RUN curl -L "https://github.com/casperjs/casperjs/archive/$CASPERJS_VERSION.tar.gz" | tar xz
RUN ln -sf /opt/casperjs-$CASPERJS_VERSION/bin/casperjs /usr/bin/casperjs

# Helper script
ADD ./bin/shub-exec /usr/bin/shub-exec
