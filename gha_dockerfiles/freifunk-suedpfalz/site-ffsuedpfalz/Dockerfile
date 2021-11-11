FROM debian:stable-slim
ENV GLUON_VERSION=v2021.1.1
ENV BUILD_TYPE=beta
ENV BRANCH_NAME=1.4.14_b
ENV VERSION=1.4.14
ENV GLUON_URL=https://github.com/freifunk-gluon/gluon.git

ENV SITE_URL=https://github.com/freifunk-suedpfalz/site-ffsuedpfalz
ENV SITE_BRANCH=1.4.14_b

ENV FORCE_UNSAFE_CONFIGURE=1
ENV CORES=7

ENV VERBOSE=w

ENV GLUON_IMAGEDIR=/output
VOLUME /output

RUN apt-get update \
    && apt-get install -y cmake help2man wget curl python2.7 build-essential gnupg gawk unzip ncurses-dev git \
    && apt-get update \
    && curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py && python2.7 get-pip.py

COPY build-jenkins.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/build-jenkins.sh
RUN ln -s /usr/local/bin/build-jenkins.sh /

ENTRYPOINT build-jenkins.sh $BRANCH_NAME $GLUON_VERSION $BUILD_TYPE $VERSION $SITE_URL $SITE_BRANCH $CORES $VERBOSE \
           && cd /tmp/$BRANCH_NAME \
           && for TARGET in $(make list-targets); do \
               make -j $CORES GLUON_DEPRECATED=full GLUON_TARGET=$TARGET GLUON_AUTOUPDATER_BRANCH=$BUILD_TYPE GLUON_AUTOUPDATER_ENABLED=1 GLUON_RELEASE=$VERSION$BUILD_TYPE; \
           done
