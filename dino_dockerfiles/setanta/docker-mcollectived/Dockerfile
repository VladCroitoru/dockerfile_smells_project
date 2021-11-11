FROM alpine:3.9

ARG MCOLLECTIVE_VERSION=2.12.4

RUN apk add --update ruby ruby-json ca-certificates
RUN apk add --update --virtual build-dependencies build-base ruby-dev wget \
 && gem install --no-rdoc --no-ri stomp etc \
 && wget -q https://github.com/puppetlabs/marionette-collective/archive/$MCOLLECTIVE_VERSION.tar.gz -O mcollective.tar.gz \
 && tar xf mcollective.tar.gz \
 && apk del build-dependencies

RUN mv /marionette-collective-$MCOLLECTIVE_VERSION /mcollective

RUN mkdir -p /etc/mcollective /usr/share/mcollective/plugins

RUN cp /mcollective/etc/facts.yaml.dist /etc/mcollective/facts.yaml
RUN cp /mcollective/etc/*.erb /etc/mcollective

RUN cp /mcollective/etc/server.cfg.dist /etc/mcollective/server.cfg
RUN cp /mcollective/etc/client.cfg.dist /etc/mcollective/client.cfg
RUN sed -i 's/^libdir *= *.*$/libdir = \/usr\/lib\/ruby\/vendor_ruby/g' /etc/mcollective/*.cfg

RUN cp -r /mcollective/lib/* /usr/lib/ruby/vendor_ruby

RUN cp /mcollective/bin/mcollectived /usr/sbin/
RUN cp /mcollective/bin/mco /usr/bin/

RUN rm mcollective.tar.gz
RUN rm -rf /mcollective /var/cache/apk/*

ENTRYPOINT ["mcollectived", "--no-daemonize"]
