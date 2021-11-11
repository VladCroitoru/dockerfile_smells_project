FROM alpine:3.7

LABEL maintainer="Nate Morse <nathan@shadyoaksoftware.com>"

ENV HUGO_VERSION=0.38

RUN apk add --no-cache --update curl py3-pygments && \
	curl -L https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz | tar xvz -C /tmp && \
    mv /tmp/hugo /usr/local/bin/hugo && \
    ln -s /usr/bin/pygmentize-3 /usr/local/bin/pygmentize && \
    rm -rf /tmp/*

WORKDIR /app

EXPOSE 1313

ENTRYPOINT ["hugo"]
CMD ["--help"]
