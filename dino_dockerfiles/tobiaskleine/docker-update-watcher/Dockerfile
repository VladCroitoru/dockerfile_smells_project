FROM wernight/kubectl:1.3.6

USER root

RUN apk update
RUN apk add docker
RUN apk add openrc
RUN apk add perl
RUN rc-update add docker boot

ADD crontab.txt /crontab.txt

ADD ./config/ /config/
COPY script.sh /script.sh
COPY entry.sh /entry.sh
RUN chmod 755 /script.sh /entry.sh
RUN /usr/bin/crontab /crontab.txt

ENTRYPOINT []
CMD ["/entry.sh"]
