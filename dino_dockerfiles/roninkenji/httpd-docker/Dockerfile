FROM roninkenji/slackware-base
MAINTAINER roninkenji

RUN slackpkg -batch=on -default_answer=y install httpd-2.4 apr-util sqlite cyrus-sasl apr openssl-solib
RUN mkdir -p /srv/config /srv/data /srv/logs
COPY myinit.sh /tmp/
RUN chmod +x /tmp/myinit.sh
EXPOSE 80 443
ENTRYPOINT ["/tmp/myinit.sh"]

