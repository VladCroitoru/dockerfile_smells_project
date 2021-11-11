FROM ubuntu:14.04

RUN \
     apt-get update \
  && apt-get install -y \
       beanstalkd \
       supervisor \
       wget \
  && wget -O - http://deb.openalpr.com/openalpr.gpg.key | apt-key add - \
  && echo "deb http://deb.openalpr.com/commercial/ trusty main" > /etc/apt/sources.list.d/openalpr.list \
  && apt-get update \
  && apt-get -y install \
       openalpr \
       openalpr-daemon

VOLUME ["/var/lib/openalpr/plateimages"]

EXPOSE 11300

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY update_config.sh /
COPY alprd.conf.template /

ENTRYPOINT ["/update_config.sh"]
CMD ["/usr/bin/supervisord"]
