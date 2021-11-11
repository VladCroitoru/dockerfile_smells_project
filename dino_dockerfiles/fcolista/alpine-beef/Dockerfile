FROM alpine:latest
MAINTAINER Francesco Colista <fcolista@alpinelinux.org>
ENV LANG en_US.UTF-8
RUN echo "http://nl.alpinelinux.org/alpine/v3.4/community" >> /etc/apk/repositories && \
    echo "http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
	apk add -U \
		git \
		bash \
		ruby \
		ruby-dev \
		ruby-io-console \
		ruby-bigdecimal \
		sqlite-dev \
		sqlite-libs \
		build-base \
		libstdc++ \
		nodejs \
		ruby-bundler && \
	cd /usr/share && \
    	git clone git://github.com/beefproject/beef.git && \
	cd beef && \
	bundle install && \
	apk del git \
		build-base \
		bash \
		sqlite-dev \
		ruby-dev \
	&& rm -rf /var/cache/apk/*

WORKDIR /usr/share/beef
EXPOSE 3000
ENTRYPOINT [ "./beef" ]
