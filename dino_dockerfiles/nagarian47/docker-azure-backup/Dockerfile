FROM microsoft/azure-cli

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -yqq update \
    && apt-get -yqq install incron \
    && rm -f /etc/incron.allow

ADD ./run.sh /usr/bin/azure-backup

RUN chmod 777 /usr/bin/azure-backup

VOLUME ["/var/files"]

ENTRYPOINT ["/usr/bin/azure-backup"]
CMD ["start"]