FROM alpine:3.5
MAINTAINER dishuostecli "dishuostec@gmail.com"

ARG ALPINE_REPO=http://dl-cdn.alpinelinux.org

RUN ver=$(cat /etc/alpine-release | awk -F '.' '{printf "%s.%s", $1, $2;}') \
	&& repos=/etc/apk/repositories \
        && mv -f ${repos} ${repos}_bk \
	&& echo "${ALPINE_REPO}/alpine/v${ver}/main" > ${repos} \
	&& echo "${ALPINE_REPO}/alpine/v${ver}/community" >> ${repos} \
        \
        && cd /tmp \
        && apk --no-cache add wget ca-certificates \
        && wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub \
        && wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.23-r3/glibc-2.23-r3.apk \
        && apk add glibc-2.23-r3.apk \
        \
        && mv -f ${repos}_bk ${repos} \
        && apk del wget ca-certificates \
        && rm -f \
                /root/.wget-hsts \
                glibc-2.23-r3.apk \
                /etc/apk/keys/sgerrand.rsa.pub
