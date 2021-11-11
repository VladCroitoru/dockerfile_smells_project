FROM picymru/base:latest
MAINTAINER Matthew Gall <matthew@picymru.org.uk>

ENV HOST 127.0.0.1
ENV PORT 80
ENV HUGO_VERSION 0.16
ENV HUGO_BINARY hugo_${HUGO_VERSION}_linux-64bit

ADD https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tgz /tmp
RUN tar xzf /tmp/${HUGO_BINARY}.tgz -C /tmp \
	&& ln -s /tmp/hugo /usr/local/bin/hugo \
	&& rm /tmp/${HUGO_BINARY}.tgz

WORKDIR /app
COPY . /app

EXPOSE 80

CMD ["/app/run.sh"]