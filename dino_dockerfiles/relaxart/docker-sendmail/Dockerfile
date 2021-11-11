FROM ubuntu:latest

MAINTAINER Ilya Isaev "me@ilyaisaev.com"

WORKDIR /etc/mail

RUN set -e && \
 apt-get update && \
 apt-get install -y sendmail

COPY sendmail.mc /etc/mail/sendmail.mc

RUN m4 sendmail.mc > sendmail.cf && \
 echo "Connect:172 RELAY" >> access && \
 echo "Connect:10 RELAY" >> access && \
 make

EXPOSE 25

CMD /usr/lib/sendmail -bD -X /proc/self/fd/1
