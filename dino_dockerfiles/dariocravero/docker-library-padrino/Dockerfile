FROM ruby:2.1.3

RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV PADRINO_VERSION 0.12.3

RUN gem install padrino --version "$PADRINO_VERSION"
