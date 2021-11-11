FROM ubuntu:14.04
MAINTAINER include <francisco.cabrita@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV DOCKERIZE_VERSION "0.0.3"
ENV RIEMANN_VERSION "0.2.10"

RUN apt-get -yq update && \
    apt-get -yq install default-jre-headless && \
    apt-get clean -y && \
    apt-get autoremove -y

ADD https://github.com/jwilder/dockerize/releases/download/v${DOCKERIZE_VERSION}/dockerize-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz \
    /dockerize-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz

ADD http://aphyr.com/riemann/riemann-${RIEMANN_VERSION}.tar.bz2 \
    /riemann-${RIEMANN_VERSION}.tar.bz2

RUN mkdir -p /app/etc && \
    tar xjvf riemann-${RIEMANN_VERSION}.tar.bz2 -C /app && \
    tar xzvf /dockerize-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz -C /usr/local/bin && \
    rm  riemann-*.tar.bz2 dockerize-linux-amd64-v*.tar.gz

EXPOSE 5555/udp
EXPOSE 5555/tcp
EXPOSE 5556/tcp

WORKDIR /app/riemann-${RIEMANN_VERSION}

ADD riemann.config.tmpl /app/riemann-${RIEMANN_VERSION}/etc/riemann.config.tmpl
ADD main.clj /app/etc/main.clj

ENTRYPOINT [ "dockerize", "-template", "/app/riemann-0.2.10/etc/riemann.config.tmpl:/app/riemann-0.2.10/etc/riemann.config"]

CMD ["/app/riemann-0.2.10/bin/riemann", "/app/riemann-0.2.10/etc/riemann.config"]
