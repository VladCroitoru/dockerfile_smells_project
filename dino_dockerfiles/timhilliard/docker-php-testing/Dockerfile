FROM timhilliard/docker-phpenv-multiversion:latest

MAINTAINER Tim Hilliard "https://github.com/timhilliard"

COPY install.sh /tmp/install.sh
RUN /tmp/install.sh
RUN rm /tmp/install.sh
VOLUME /var/lib/mysql

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/bin/bash", "--login"]
