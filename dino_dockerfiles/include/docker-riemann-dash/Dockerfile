FROM ruby:latest
MAINTAINER include <francisco.cabrita@gmail.com>

ENV DOCKERIZE_VERSION "0.0.3"

ADD https://github.com/jwilder/dockerize/releases/download/v${DOCKERIZE_VERSION}/dockerize-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz \
    /dockerize-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz

RUN tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz && \
    rm  dockerize-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz && \
    gem install thin fog && \
    mkdir -p /app && \
    cd /app && \
    git clone git://github.com/aphyr/riemann-dash.git && \
    cd riemann-dash && bundler

WORKDIR /app/riemann-dash

ADD config.rb.tmpl /app/riemann-dash/config.rb.tmpl

ENTRYPOINT [ "dockerize", "-template", "/app/riemann-dash/config.rb.tmpl:/app/riemann-dash/config.rb"]

CMD ["bin/riemann-dash", "config.rb"]
