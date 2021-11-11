FROM alpine:latest
MAINTAINER "Matthew Scharley <matt.scharley@gmail.com>"

USER root
RUN apk add --no-cache bash curl git gzip ncurses openssh-client openjdk8 tar && \
    curl -s https://raw.githubusercontent.com/paulp/sbt-extras/master/sbt > /usr/local/bin/sbt && chmod 0755 /usr/local/bin/sbt
ENV TERM=xterm
WORKDIR /tmp
CMD ["sh"]
