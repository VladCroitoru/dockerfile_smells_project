FROM ruby:2.3-alpine

RUN apk add --update --no-cache \
    libstdc++ \
    sqlite-dev \
    && apk add --no-cache --virtual build-dependencies \
    gcc \
    g++ \
    make \
    && gem install mailcatcher \
    && apk del build-dependencies

EXPOSE 1025 1080
CMD ["ruby", "/usr/local/bundle/gems/mailcatcher-0.6.5/bin/mailcatcher", "-f", "--ip=0.0.0.0"]
