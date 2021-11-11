FROM jruby:9.1.5.0-onbuild

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get -y upgrade && \
    apt-get install --no-install-recommends -y git curl supervisor  && \
    apt-get clean

ADD supervisord.conf /etc/supervisor/conf.d/nero.conf
VOLUME /var/log/nero
ENTRYPOINT ["/usr/bin/supervisord"]
