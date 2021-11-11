FROM debian:jessie
MAINTAINER Daniel Dent (https://www.danieldent.com/)
RUN DEBIAN_FRONTEND=noninteractive apt-get update -q \
    && DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y python3-urllib3 python3-yaml \
    && rm -Rf /var/lib/apt /var/cache/apt
COPY rancher-metadata-dumper.py /
RUN chmod +x /rancher-metadata-dumper.py
VOLUME /rancher-metadata-dumper
WORKDIR /rancher-metadata-dumper
ENTRYPOINT ["/rancher-metadata-dumper.py"]
