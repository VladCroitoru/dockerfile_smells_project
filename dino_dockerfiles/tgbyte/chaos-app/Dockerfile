FROM ruby:2.3.1-slim

EXPOSE 4567

ENV DUMBINIT_VERSION=1.1.1
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y -o Apt::Install-Recommends=0 wget ca-certificates && \
    wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v${DUMBINIT_VERSION}/dumb-init_${DUMBINIT_VERSION}_amd64 && \
    chmod +x /usr/local/bin/dumb-init && \
    apt-get remove -y --purge wget ca-certificates && \
    adduser --uid 500 --disabled-password --gecos "www" --quiet www && \
    mkdir /data && \
    chown www.www /data

ADD Gemfile* /app/
WORKDIR /app
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -o Apt::Install-Recommends=0 libssl-dev build-essential && \
    bundle -j4 --without development test && \
    apt-get remove -y --purge build-essential libssl-dev && \
    apt-get autoremove -y --purge

ADD . /app/

USER www

ENTRYPOINT ["/usr/local/bin/dumb-init"]
CMD ["ruby", "/app/app.rb"]
