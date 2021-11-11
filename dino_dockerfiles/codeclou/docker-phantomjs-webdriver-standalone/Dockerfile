FROM ubuntu:16.04

ENV PHANTOMJS_VERSION 2.1.1
ENV PHANTOMJS_SHA512S 039b62ecf2fa4196357e129727871a53b046948e17b21900c78a1af4d0b523e41b9d4137e7454b0a638333d7fc27e65d14f4af8c665e982a504c12f828525419

#
# PACKAGES
#
COPY docker-entrypoint.sh /opt/
RUN apt-get update && \
    apt-get -y install fontconfig curl bzip2 zlib1g-dev && \
    echo "=== INSTALLING PHANTOMJS =========================" && \
    echo "${PHANTOMJS_SHA512S}  /opt/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2" > /opt/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2.sha512 && \
    curl -jkSL -o /opt/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2 \
         https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2 && \
    sha512sum -c /opt/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2.sha512 && \
    tar -C /opt/ -xf /opt/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2 && \
    rm -f /opt/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2 && \
    addgroup --gid 10777 phantomjs && \
    adduser --uid 10777 --gid 10777 --no-create-home --disabled-password --disabled-login -gecos "" phantomjs && \
    mkdir /opt/phantomwork && \
    mkdir /work && \
    chown phantomjs:phantomjs /opt/phantomwork && \
    chown phantomjs:phantomjs /work && \
    rm -rf /var/lib/apt/lists/* && \
    chmod u+rx,g+rx,o+rx,a-w /opt/docker-entrypoint.sh

#
# RUN PHANTOMJS SELENIUM SERVER STANDALONE
#
USER phantomjs
ENV PATH $PATH:/opt/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64/bin
EXPOSE 4444
VOLUME /work
WORKDIR /opt/phantomwork
ENTRYPOINT ["/opt/docker-entrypoint.sh"]
CMD ["phantomjs", "--webdriver", "4444"]
