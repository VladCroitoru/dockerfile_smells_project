FROM buildpack-deps:jessie-curl
MAINTAINER vrlo <vrovro@gmail.com>

RUN echo "deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti" \
  > /etc/apt/sources.list.d/ubnt.list \
  && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv C0A52C50 \
  && apt-get update && apt-get install -y --no-install-recommends \
    unifi \
  && rm -rf /var/lib/apt/lists/*

VOLUME ["/var/lib/unifi", "/var/log/unifi"]
EXPOSE 8080 8443 8880 8843

WORKDIR /usr/lib/unifi

ENTRYPOINT ["/usr/bin/java", "-Xmx1024M", "-jar", "lib/ace.jar"]
CMD ["start"]
