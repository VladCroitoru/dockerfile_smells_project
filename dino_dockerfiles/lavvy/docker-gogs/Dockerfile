#
# Gogs Dockerfile
#
# https://github.com/rosstimson/docker-gogs
#
# AUTHOR:   Ross Timson <ross@rosstimson.com>
# LICENSE:  WTFPL - http://wtfpl.net
#
# Installs Gogs: A self-hosted Git service written in Go.
#
# Gogs:   http://gogs.io
#


FROM golang:1.4
MAINTAINER Ross Timson <ross@rosstimson.com>

ENV GOGS_VERSION v1.0.0
ENV GOGS_PATH $GOPATH/src/github.com/gogits/gogs
ENV GOGS_CUSTOM_CONF_PATH $GOGS_PATH/custom/conf
ENV GOGS_CUSTOM_CONF $GOGS_CUSTOM_CONF_PATH/app.ini

RUN apt-get update \
    && apt-get -y install openssh-server \
    && mkdir -p /var/run/sshd \
    && sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config \
    && sed '/pam_loginuid.so/s/^/#/g' -i  /etc/pam.d/*

RUN useradd -s /bin/bash -u 2000 -m -c gogs git
RUN mkdir -p $GOPATH/src/github.com/gogits \
    && git clone https://github.com/lavvy/gogs.git $GOGS_PATH \
    && cd $GOGS_PATH \
    && git checkout -b $GOGS_VERSION \
    && go get -tags 'redis' ./... \
    && go build -tags 'redis' \
    && mkdir -p $GOGS_CUSTOM_CONF_PATH \
    && cp conf/app.ini $GOGS_CUSTOM_CONF \
    && chown -R git $GOGS_PATH

ADD start.sh /start.sh
RUN chmod +x /start.sh

ENV HOME /home/git
ENV PATH $GOGS_PATH:$PATH
# WORKDIR $GOGS_PATH - env var expansion doesn't work here.
WORKDIR /go/src/github.com/gogits/gogs
EXPOSE 22 3000
CMD ["/start.sh"]
