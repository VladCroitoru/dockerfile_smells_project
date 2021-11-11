FROM alpine 

RUN apk upgrade --update-cache --available
RUN apk add bash git wget tar gzip
RUN mkdir -p /opt/exporter
WORKDIR /opt/exporter
RUN wget https://releases.rancher.com/cli/v0.6.3/rancher-linux-amd64-v0.6.3.tar.gz
RUN tar -zxvf rancher-linux-amd64-v0.6.3.tar.gz
RUN mv rancher-v0.6.3/rancher /opt/exporter && rm -rf rancher-v0.6.3*
ADD exporter.sh /opt/exporter/exporter.sh
CMD ["bash","/opt/exporter/exporter.sh"]