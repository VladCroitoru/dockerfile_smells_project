FROM debian:7.7

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get install -q -y postfix net-tools

RUN echo Europe/Paris > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

RUN echo "postfix postfix/mailname string gmail.com" | debconf-set-selections
RUN echo "postfix postfix/main_mailer_type string 'Internet Site'" | debconf-set-selections

ADD run-smtp.sh /run-smtp.sh

CMD /run-smtp.sh
