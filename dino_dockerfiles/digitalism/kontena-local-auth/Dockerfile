FROM ubuntu:trusty
MAINTAINER jussi.nummelin@gmail.com

RUN echo 'deb http://ppa.launchpad.net/brightbox/ruby-ng/ubuntu trusty main' >> /etc/apt/sources.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0x80f70e11f0f0d5f10cb20e62f5da5f09c3173aa6 && \
    apt-get update && \
    apt-get install -y ruby2.2 ruby2.2-dev build-essential ca-certificates libssl-dev sqlite3 libsqlite3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    gem install bundler

ADD Gemfile /app/
ADD Gemfile.lock /app/

RUN cd /app ; bundle install --without development test

ADD . /app
RUN chown -R nobody:nogroup /app
USER nobody

ENV RACK_ENV production
EXPOSE 5000

WORKDIR /app

CMD ["./run.sh"]
