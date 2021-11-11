FROM dougbtv/asterisk14:latest
MAINTAINER Alexander Nikiforov <painkiller359@gmail.com>
ENV build_date 2018-01-28

RUN mkdir -p /etc/defaults/

RUN useradd -m asterisk -s /sbin/nologin
RUN chown asterisk:asterisk /var/run/asterisk
RUN chown -R asterisk:asterisk /etc/asterisk/
RUN chown -R asterisk:asterisk /var/{lib,log,spool}/asterisk
RUN chown -R asterisk:asterisk /usr/lib64/asterisk/

COPY data/default-configs /etc/defaults/asterisk
RUN chown -R asterisk:asterisk /etc/defaults/asterisk/

ADD data/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

CMD /docker-entrypoint.sh
