FROM alpine:latest AS build-env

ENV GOPATH /gopath
ENV CADDY_REPO_OWNER mholt
ENV CADDY_REPO_NAME caddy

COPY plugins.txt /plugins

RUN apk add --no-cache musl build-base su-exec libcap tini go git musl \
	&& mkdir -p $GOPATH/src/github.com/$CADDY_REPO_OWNER \
	&& cd $GOPATH/src/github.com/$CADDY_REPO_OWNER \
	&& git clone https://github.com/$CADDY_REPO_OWNER/$CADDY_REPO_NAME 
RUN cd $GOPATH/src/github.com/$CADDY_REPO_OWNER/$CADDY_REPO_NAME \
	&& cd caddy/caddymain \
	&& export line="$(grep -n "// This is where other plugins get plugged in (imported)" < run.go | sed 's/^\([0-9]\+\):.*$/\1/')" \
	&& head -n ${line} run.go > newrun.go \
	&& cat /plugins >> newrun.go \
	&& line=`expr $line + 1` \
	&& tail -n +${line} run.go >> newrun.go \
	&& rm -f run.go \
	&& mv newrun.go run.go \
	&& go get github.com/$CADDY_REPO_OWNER/$CADDY_REPO_NAME/... \
	&& cp $GOPATH/bin/caddy /root/caddy \
	&& rm -rf $GOPATH/* 

RUN mkdir -p $GOPATH/src/github.com/miniers/docker-gen  \
    && git clone https://github.com/miniers/docker-gen.git $GOPATH/src/github.com/miniers/docker-gen \
    && cd $GOPATH/src/github.com/miniers/docker-gen \
    && go get github.com/robfig/glock \
    && $GOPATH/bin/glock sync -n < GLOCKFILE \
    && go get github.com/miniers/docker-gen/... \
	&& cp $GOPATH/bin/docker-gen /root/docker-gen \
	&& rm -rf $GOPATH/*

FROM alpine:latest
MAINTAINER miniers <m@lk.mk>

ARG S6_OVERLAY_VERSION=v1.21.4.0

ENV CADDY_OPTIONS ""
ENV DOCKER_HOST unix:///tmp/docker.sock

# install s6
RUN apk add --update --no-cache curl tzdata inotify-tools && \
    curl -sSL https://github.com/just-containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-amd64.tar.gz \
    | tar xfz - -C / && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    apk del tzdata && \
    rm -rf /var/cache/apk/*

RUN apk add --no-cache openssh-client git tar php7-fpm curl

# essential php libs
RUN apk add --no-cache php7-curl php7-dom php7-gd php7-ctype php7-zip php7-xml php7-iconv php7-sqlite3 php7-mysqli php7-pgsql php7-json php7-phar php7-openssl php7-pdo php7-pdo_mysql php7-pdo_sqlite php7-session php7-mbstring php7-bcmath

# symblink php7 to php
RUN ln -sf /usr/bin/php7 /usr/bin/php

# symlink php-fpm7 to php-fpm
RUN ln -sf /usr/bin/php-fpm7 /usr/bin/php-fpm

# composer
RUN curl --silent --show-error --fail --location \
      --header "Accept: application/tar+gzip, application/x-gzip, application/octet-stream" \
      "https://getcomposer.org/installer" \
    | php -- --install-dir=/usr/bin --filename=composer

# allow environment variable access.
RUN echo "clear_env = no" >> /etc/php7/php-fpm.conf


# install caddy
COPY --from=build-env /root/caddy /usr/bin/caddy

# install docker-gen

COPY --from=build-env /root/docker-gen /usr/local/bin/docker-gen

# validate install
RUN /usr/bin/caddy -version
RUN /usr/bin/caddy -plugins

ADD root /

EXPOSE 80 443 2015

ENTRYPOINT ["/init"]