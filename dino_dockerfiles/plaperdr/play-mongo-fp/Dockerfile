FROM java:latest
MAINTAINER Pierre Laperdrix

ADD website /opt/tmp/
WORKDIR /opt/tmp/
RUN ./activator stage && cp -r target/universal/stage/ /opt/website/ && rm -r /opt/tmp/ /root/.sbt/ /root/.ivy2/
WORKDIR /opt/website/

ENTRYPOINT ["./bin/website"]
