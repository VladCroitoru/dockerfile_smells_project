FROM ubuntu:trusty
MAINTAINER Borja Juncosa <borja.juncosa@socialpoint.es>

ENV TMP_PACKAGES="build-essential ruby-dev"
ENV PACKAGES="ruby librrd-ruby collectd"

WORKDIR /usr/src
RUN apt-get update && \
    apt-get install -y $TMP_PACKAGES $PACKAGES && \
    gem install visage-app

RUN apt-get install -y rrdtool
RUN sed -i 's|\(Rack::Server.new(:config => config, :Port => port, :server => "webrick"\)|\1, :Host => "0.0.0.0"|g' /var/lib/gems/1.9.1/gems/visage-app-2.1.0/bin/visage-app

# Clean up APT when done.
RUN apt-get remove -y --purge $TMP_PACKAGES && \
    apt-get autoremove -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 9292:9292/tcp

VOLUME [ "/var/lib/collectd/rrd" ]

ENV RRDDIR=/var/lib/collectd/rrd

ADD start.sh /usr/local/bin/

CMD [ "/usr/local/bin/start.sh" ]

