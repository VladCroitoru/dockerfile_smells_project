FROM alpine:3.5

RUN apk add --no-cache \
		bash \
		curl

ADD lib/lib-x64.tgz /

ARG P4_VERSION=16.2
RUN curl -sSL -O http://cdist2.perforce.com/perforce/r${P4_VERSION}/bin.linux26x86_64/p4 && mv p4 /usr/bin/p4 && chmod +x /usr/bin/p4
RUN curl -sSL -O http://cdist2.perforce.com/perforce/r${P4_VERSION}/bin.linux26x86_64/p4d && mv p4d /usr/sbin/p4d && chmod +x /usr/sbin/p4d

ENV VISUAL=vi
ENV P4PORT=1666
ENV P4ROOT=/metadata
ENV P4NAME=myserver
ENV P4JOURNAL=/journals/journal

RUN mkdir /metadata && mkdir /library && mkdir /journals && mkdir /backup
VOLUME ["/metadata", "/library", "/journals", "/backup"]

COPY docker-entrypoint.sh /
WORKDIR /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["p4d"]



