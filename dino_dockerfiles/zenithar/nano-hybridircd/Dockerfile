FROM frolvlad/alpine-glibc:latest
MAINTAINER Thibault NORMAND <me@zenithar.org>

WORKDIR /src

RUN apk add --update -t build-deps make gcc g++ git wget bison openssl-dev \
    && apk add -u musl && rm -rf /var/cache/apk/* \
    && wget http://prdownloads.sourceforge.net/ircd-hybrid/ircd-hybrid-8.2.21.tgz \
    && tar zxvf ircd-hybrid-8.2.21.tgz \
    && cd /src/ircd-hybrid-8.2.21 \
    && ./configure --prefix="/opt/ircd" --enable-openssl \
    && make \
    && make install \
    && rm -Rf /src && apk del --purge build-deps

ADD ./config /opt/ircd/etc

RUN addgroup ircd \
    && adduser -G ircd -D ircd \
    && chown -R ircd:ircd /opt/ircd

USER ircd
WORKDIR /opt/ircd

VOLUME /var/log/ircd

EXPOSE 6667
ENTRYPOINT ["/opt/ircd/bin/ircd"]
CMD ["-foreground"]

