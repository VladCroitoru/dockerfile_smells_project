FROM ruby:alpine
MAINTAINER btquanto@gmail.com

RUN apk update && \
    apk upgrade && \
    apk add build-base && \
    rm -rf /var/cache/apk/* && \
    gem install jekyll rdiscount kramdown jekyll-redirect-from rouge jekyll-paginate jekyll-mermaid

VOLUME ["/src"]
EXPOSE 4000

WORKDIR /src
