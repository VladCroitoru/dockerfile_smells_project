FROM debian:7

MAINTAINER v00rh33s jason@sysadminwiki.net

RUN apt-get update && apt-get install -y git python2.7 supervisor && \
    git clone --recursive https://github.com/Dieterbe/anthracite.git /anthracite && \
    mkdir -p /var/log/supervisor

COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 8081

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]