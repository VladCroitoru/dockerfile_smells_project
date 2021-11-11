FROM maven:alpine
LABEL maintainer="CN Services <noninojulian@gmail.com>"

RUN apk add --no-cache git subversion mercurial wget curl unzip openssh ca-certificates procps bash && \
    rm -rf /var/cache/apk/*

RUN addgroup -S -g 10000 jenkins && \
    adduser -S -u 10000 -h /home/jenkins -G jenkins jenkins

USER jenkins

ENV USER_HOME_DIR /home/jenkins
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"
RUN ./usr/local/bin/mvn-entrypoint.sh

WORKDIR /home/jenkins

CMD ["/bin/sh"]