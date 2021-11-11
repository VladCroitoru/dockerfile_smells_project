FROM openjdk:8-jre

ENV RPKI_VERSION 2.24

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
 rsync \
 curl \
 procps \
 && rm -rf /var/lib/apt/lists/*

RUN curl -O https://rrdp.ripe.net/certification/content/static/validator/rpki-validator-app-$RPKI_VERSION-dist.tar.gz

RUN tar xzpf rpki-validator-app-$RPKI_VERSION-dist.tar.gz
RUN curl -o /rpki-validator-app-$RPKI_VERSION/conf/tal/arin-ripevalidator.tal https://www.arin.net/resources/rpki/arin-ripevalidator.tal

WORKDIR rpki-validator-app-$RPKI_VERSION

EXPOSE 8080 8282

ENTRYPOINT /rpki-validator-app-$RPKI_VERSION/rpki-validator.sh run
