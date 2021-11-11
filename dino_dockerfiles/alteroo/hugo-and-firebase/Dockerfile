FROM node:6.9.2-alpine

RUN npm install -g firebase-tools

ENV HUGO_VERSION 0.19
ENV HUGO_BINARY hugo_${HUGO_VERSION}_linux_amd64

# Download and Install hugo
ADD https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz /usr/local/
RUN tar xzf /usr/local/${HUGO_BINARY}.tar.gz -C /usr/local/ \
	&& ln -s /usr/local/${HUGO_BINARY}/${HUGO_BINARY} /usr/local/bin/hugo \
	&& rm /usr/local/${HUGO_BINARY}.tar.gz
