FROM debian:latest

ENV TELEGRAF_VERSION 0.1.9

RUN apt-get update && apt-get install -y curl
RUN curl -o /tmp/telegraf_$(echo $TELEGRAF_VERSION)_amd64.deb https://s3.amazonaws.com/get.influxdb.org/telegraf/telegraf_$(echo $TELEGRAF_VERSION)_amd64.deb && \
	dpkg -i /tmp/telegraf_$(echo $TELEGRAF_VERSION)_amd64.deb

ADD telegraf.toml /opt/telegraf/telegraf.toml

CMD ["/opt/telegraf/telegraf", "-config=/opt/telegraf/telegraf.toml"]