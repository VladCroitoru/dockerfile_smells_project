FROM ruby:2.4.0-alpine

RUN apk add --no-cache build-base && \
    gem install --no-rdoc --no-document jekyll && \
    apk del build-base && \
    mkdir -p /workdir
WORKDIR ["/workdir"]
ENTRYPOINT ["jekyll"]
LABEL   io.whalebrew.config.ports='["4000:4000"]'
