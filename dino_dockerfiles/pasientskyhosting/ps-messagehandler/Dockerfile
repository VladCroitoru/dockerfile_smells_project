FROM cantara/alpine-zulu-jdk8
MAINTAINER Andreas Krüger <ak@patientsky.com>

RUN apk -Uu add bash jq supervisor tzdata

RUN ln -s /usr/local/java/bin/java /bin/java && \
    ulimit -m unlimited && \
    ulimit -v unlimited && \
    ulimit -n 65536 && \
    mkdir -p /data

ADD conf/supervisord.conf /etc/supervisord.conf

ADD scripts/start.sh /start.sh
RUN chmod 755 /start.sh

EXPOSE 80
CMD ["/start.sh"]
