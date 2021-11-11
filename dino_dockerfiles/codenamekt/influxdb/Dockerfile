FROM debian:latest

ENV INFLUXDB_VERSION 0.9.4.2

RUN apt-get update && apt-get install -y curl
RUN curl -o /tmp/influxdb_$(echo $INFLUXDB_VERSION)_amd64.deb https://s3.amazonaws.com/influxdb/influxdb_$(echo $INFLUXDB_VERSION)_amd64.deb && \
	dpkg -i /tmp/influxdb_$(echo $INFLUXDB_VERSION)_amd64.deb

ADD influxdb.toml /opt/influxdb/influxdb.toml

CMD ["/opt/influxdb/influxd", "-config=/opt/influxdb/influxdb.toml"]