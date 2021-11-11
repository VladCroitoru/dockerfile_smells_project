FROM azul/zulu-openjdk-debian:8

MAINTAINER Gyula Voros <gyulavoros87@gmail.com>

ENV UPSOURCE_VERSION 3.5.3550

WORKDIR /opt

RUN apt-get update && apt-get install -y unzip wget ca-certificates && \
    wget -q https://download.jetbrains.com/upsource/upsource-$UPSOURCE_VERSION.zip && \
    unzip -q upsource-$UPSOURCE_VERSION.zip -x */internal/java/* && \
    rm -rf upsource-$UPSOURCE_VERSION.zip && \
    mv upsource-$UPSOURCE_VERSION Upsource && \ 
    apt-get autoremove -y unzip wget && \
    rm -rf /var/cache/apt/archives

RUN echo "* - memlock unlimited" >> /etc/security/limits.conf && \
    echo "* - nofile 100000"     >> /etc/security/limits.conf && \
    echo "* - nproc 32768"       >> /etc/security/limits.conf && \
    echo "* - as unlimited"      >> /etc/security/limits.conf

WORKDIR /opt/Upsource

EXPOSE 8080
VOLUME ["/opt/Upsource/conf", "/opt/Upsource/data", "/opt/Upsource/logs", "/opt/Upsource/backups"]

ENTRYPOINT ["bin/upsource.sh"]
CMD ["run"]
