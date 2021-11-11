# vim:set ft=dockerfile:
FROM alpine:edge

# add community and testing repo
RUN echo "@community http://dl-4.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
    echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

# install the packges we need
RUN apk add --no-cache bash curl openjdk7-jre-base stress@testing tar

# setup jmeter
RUN mkdir -p /opt/jmeter && \
    curl -Ls http://mirrors.gigenet.com/apache//jmeter/binaries/apache-jmeter-3.0.tgz \
	| tar xz --strip=1 -C /opt/jmeter && \
	ln -s /opt/jmeter/bin/jmeter.sh /usr/bin/jmeter

# copy entrypoint script
COPY docker-entrypoint.sh test.jmx /

ENTRYPOINT ["/docker-entrypoint.sh"]
