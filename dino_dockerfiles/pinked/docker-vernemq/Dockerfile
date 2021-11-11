FROM erlio/docker-vernemq

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /usr/sbin/wait-for-it.sh
COPY bin/vernemq.sh /usr/sbin/start_vernemq
COPY bin/healthcheck.sh /usr/sbin/healthcheck
COPY bin/kill-dead.sh /usr/sbin/kill-dead

STOPSIGNAL SIGTERM

HEALTHCHECK --interval=10s CMD /usr/sbin/healthcheck

RUN chmod +x /usr/sbin/wait-for-it.sh /usr/sbin/healthcheck
