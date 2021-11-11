# Lastest visono/debian
FROM visono/debian:latest

MAINTAINER Patrik Hagedorn <p.hagedorn@visono.com>

USER root

# Install Serf
ADD https://releases.hashicorp.com/serf/0.7.0/serf_0.7.0_linux_amd64.zip serf.zip
RUN unzip serf.zip \
    && rm serf.zip \
    && mv serf /usr/bin/

# Adding supervisord.conf
COPY supervisord-serf.conf /etc/supervisor/conf.d/00-serf.conf

# Adding scripts
COPY start-serf.sh /start-serf.sh
RUN chmod 755 /*.sh

CMD ["/bin/bash"]