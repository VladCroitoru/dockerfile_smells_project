FROM       pyrites/rubybase
MAINTAINER Yosuke Yamamoto "yosuke@pyrites.jp"

RUN gem install geminabox

ADD apps apps
RUN (cd apps; bundle install) && \
    mkdir -p /var/geminabox/data

EXPOSE 9292:9292
VOLUME ["/var/geminabox/data"]

ENV RACK_ENV production

WORKDIR /apps
ENTRYPOINT ["rackup", "config.ru", "-p", "9292"]

