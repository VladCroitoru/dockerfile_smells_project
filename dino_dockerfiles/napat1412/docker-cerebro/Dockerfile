FROM openjdk:8-jre

ENV CEREBRO_VERSION=0.6.6
ENV CEREBRO_HOME=/opt/cerebro

ADD https://github.com/lmenezes/cerebro/releases/download/v${CEREBRO_VERSION}/cerebro-${CEREBRO_VERSION}.tgz /tmp/cerebro.tgz

RUN tar -C /opt -xzf /tmp/cerebro.tgz && \
  rm /tmp/cerebro.tgz && \
  mkdir /opt/cerebro-${CEREBRO_VERSION}/logs && \
  mv /opt/cerebro-${CEREBRO_VERSION} /opt/cerebro

WORKDIR /opt/cerebro
EXPOSE 9000

COPY entrypoint.sh /entrypoint
CMD ["/entrypoint"]
