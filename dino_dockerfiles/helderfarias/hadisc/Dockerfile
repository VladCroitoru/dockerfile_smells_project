FROM golang

RUN apt-get update \
    && apt-get install -y libssl1.0.0 --no-install-recommends \
    && apt-get install -y libc6-dev libpcre3-dev libssl-dev \
    && apt-get -y install supervisor \
    && rm -rf /var/lib/apt/lists/*


# Install nginx
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/mainline/debian/ wheezy nginx" >> /etc/apt/sources.list
RUN apt-get update && \
    apt-get install -y ca-certificates nginx && \
    rm -rf /var/lib/apt/lists/*

# Install haproxy
ENV HAPROXY_MAJOR 1.5
ENV HAPROXY_VERSION 1.5.11
ENV HAPROXY_MD5 5500a79d0d2b238d4a1e9749bd0c2cb2
RUN set -x \
	&& apt-get update && apt-get install -y $buildDeps --no-install-recommends && rm -rf /var/lib/apt/lists/* \
	&& curl -SL "http://www.haproxy.org/download/${HAPROXY_MAJOR}/src/haproxy-${HAPROXY_VERSION}.tar.gz" -o haproxy.tar.gz \
	&& echo "${HAPROXY_MD5}  haproxy.tar.gz" | md5sum -c \
	&& mkdir -p /usr/src/haproxy \
	&& tar -xzf haproxy.tar.gz -C /usr/src/haproxy --strip-components=1 \
	&& rm haproxy.tar.gz \
	&& make -C /usr/src/haproxy \
		TARGET=linux2628 \
		USE_PCRE=1 PCREDIR= \
		USE_OPENSSL=1 \
		USE_ZLIB=1 \
		all \
		install-bin \
	&& mkdir -p /usr/local/etc/haproxy \
	&& cp -R /usr/src/haproxy/examples/errorfiles /usr/local/etc/haproxy/errors \
	&& rm -rf /usr/src/haproxy


RUN go get github.com/tools/godep
RUN go install github.com/tools/godep
RUN mkdir -p cd $GOPATH/src/github.com/helderfarias/hadisc
COPY discovery $GOPATH/src/github.com/helderfarias/hadisc/discovery
COPY drive $GOPATH/src/github.com/helderfarias/hadisc/drive
COPY Godeps $GOPATH/src/github.com/helderfarias/hadisc/Godeps
COPY helper $GOPATH/src/github.com/helderfarias/hadisc/helper
COPY templates $GOPATH/src/github.com/helderfarias/hadisc/templates
COPY util $GOPATH/src/github.com/helderfarias/hadisc/util
COPY main.go $GOPATH/src/github.com/helderfarias/hadisc/
RUN cd src/github.com/helderfarias/hadisc && godep go build
RUN cd src/github.com/helderfarias/hadisc \
    && cp hadisc /usr/bin/hadisc \
    && chmod +x /usr/bin/hadisc

RUN cd $GOPATH/src/github.com/helderfarias/hadisc \
    && mkdir -p /etc/haproxy/template \
    && cp templates/haproxy.tpl /etc/haproxy/template

RUN cd $GOPATH/src/github.com/helderfarias/hadisc \
    && mkdir -p /etc/nginx/template \
    && cp templates/nginx.tpl /etc/nginx/template

RUN cd $GOPATH/src/github.com/helderfarias/hadisc \
    && cp templates/*.conf /etc/supervisor/conf.d/

RUN rm /etc/nginx/conf.d/*
COPY templates/nginx_server.conf /etc/nginx/nginx.conf

COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8080

CMD ["/entrypoint.sh"]

