FROM debian:stretch

ADD entrypoint.sh /opt/entrypoint.sh
ADD config /root/.ssh/config

RUN apt-get update \
    && apt-get install -y ssh sshpass rsync

ENTRYPOINT ["sh", "/opt/entrypoint.sh"]
