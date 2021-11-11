FROM uqlibrary/docker-base:9

RUN \
    yum install -y cifs-utils unison240 && \
    yum clean all

COPY bin/unison-sync.sh /usr/bin/unison-sync.sh

CMD ["unison-sync.sh"]
