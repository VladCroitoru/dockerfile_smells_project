FROM alpine:latest

RUN apk add --no-cache \
	bash \
	coreutils \
	curl \
	python \
	nodejs \
	fontconfig \
	ttf-freefont

ENV PHANTOMJS_VERSION 2.1.1
ENV CASPERJS_VERSION 1.1.3
ENV BACKSTOP_VERSION 2.5.0

RUN \
	mkdir -p /opt && \
	# PhantomJS
	echo "Downloading PhantomJS v${PHANTOMJS_VERSION}..." && \
	curl -sL "https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2" | tar jx && \
	mv phantomjs-$PHANTOMJS_VERSION-linux-x86_64 /opt/phantomjs && \
	ln -s /opt/phantomjs/bin/phantomjs /usr/bin/phantomjs && \
	echo "Fixing PhantomJS on Alpine" && \
	curl -sL "https://github.com/dustinblackman/phantomized/releases/download/$PHANTOMJS_VERSION/dockerized-phantomjs.tar.gz" | tar zx -C /

RUN \
	# CasperJS
	echo "Downloading CaperJS v${CASPERJS_VERSION}..." && \
	curl -sL "https://github.com/casperjs/casperjs/archive/$CASPERJS_VERSION.tar.gz" | tar zx && \
	mv casperjs-$CASPERJS_VERSION /opt/casperjs && \
	ln -s /opt/casperjs/bin/casperjs /usr/bin/casperjs

RUN npm install -g backstopjs@${BACKSTOP_VERSION}

RUN \
	adduser -D backstop && \
	mkdir -p /app/.fonts && \
	# Fix not honored general font configuration in user space. We need to explicit add directory
	ln -s /app/.fonts /home/backstop/.fonts

# Make our font config system wide
COPY fonts.conf /etc/fonts/local.conf

RUN \
	fc-cache && \
	chown backstop:backstop /app && \
	su - backstop

WORKDIR /app

ENTRYPOINT ["backstop"]
