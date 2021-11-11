FROM ruby:2.6.2

RUN curl -L 'https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64' \
      > /usr/bin/jq && \
    chmod +x /usr/bin/jq

RUN apt update && \
    apt install -y graphviz &&  \
    gem install bundler && \
    rm -rf /var/lib/apt/lists/*

RUN chmod 777 -R /usr/local/bundle

USER 1000
WORKDIR /code
