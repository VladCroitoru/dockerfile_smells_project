FROM alpine

MAINTAINER andy@hassiumlabs.com

ENV HUGO_VERSION 0.20.7

RUN apk --no-cache add --update curl python py-pip && \
	curl -L https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz | tar xvz -C /tmp && \
    find /tmp -perm /a+x -exec cp {} /usr/local/bin/hugo \; && \
    rm -rf /tmp/* && \
    pip install Pygments

EXPOSE 1313

ENTRYPOINT ["hugo"]
