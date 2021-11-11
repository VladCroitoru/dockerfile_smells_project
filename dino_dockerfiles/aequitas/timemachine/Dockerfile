FROM ubuntu:14.04
MAINTAINER Johan Bloemberg <docker@ijohan.nl>

RUN apt-get update 
ENV DEBIAN_FRONTEND noninteractive
RUN ln -s -f /bin/true /usr/bin/chfn
RUN apt-get install -yqq netatalk
RUN mkdir -p /backup/timemachine
RUN echo '/backup/timemachine "Backups" allow:timemachine options:usedots,upriv,tm' >> /etc/netatalk/AppleVolumes.default
RUN echo '-setuplog "default log_info /var/log/afpd.log"' >> /etc/netatalk/afpd.conf
RUN useradd timemachine -m -p sdsoOK9QxTpiM
RUN chown timemachine /backup/timemachine
RUN touch /var/log/afpd.log

ADD start.sh /start.sh

EXPOSE 548

VOLUME ["/backup"]

CMD [ "/bin/bash", "/start.sh" ]
