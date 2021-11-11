FROM ubuntu:17.04

RUN apt-get update && apt-get install -y mariadb-client openssh-client gnupg cron

COPY backup/ /

CMD /entrypoint.sh
