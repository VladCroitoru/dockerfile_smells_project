FROM alpine:3.4
MAINTAINER Lars Krantz

ENV TEMP_SQL_DIR /sqltemp
RUN mkdir $TEMP_SQL_DIR

RUN apk -Uv add python py-pip \
 && apk -UvX http://dl-4.alpinelinux.org/alpine/edge/main add postgresql \
 && apk -UvX http://dl-4.alpinelinux.org/alpine/edge/main add gawk \
 && apk -UvX http://dl-4.alpinelinux.org/alpine/edge/main add bash \
 && pip install --upgrade pip \
 && pip install awscli \
 && apk --purge -v del py-pip \
 && rm -rf /var/cache/apk/*
ADD ./execute_psql /

ENTRYPOINT ["/execute_psql"]
