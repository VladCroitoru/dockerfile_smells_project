
FROM krallin/ubuntu-tini:14.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y wget && \
    wget https://packagecloud.io/install/repositories/scalr/scalr-server-oss/script.deb -O /opt/script.deb && \
    bash /opt/script.deb && \
    apt-get install -y scalr-server && \
    apt-get clean all 

ADD docker-entrypoint.sh /

RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/usr/local/bin/tini", "--", "/docker-entrypoint.sh"]
CMD ["scalr-server"]

EXPOSE 80 8080
