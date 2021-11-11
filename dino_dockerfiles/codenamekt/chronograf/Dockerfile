FROM debian:latest

ENV CHRONOGRAF_VERSION 0.2.0

RUN apt-get update && apt-get install -y curl
RUN curl -o /tmp/chronograf_$(echo $CHRONOGRAF_VERSION)_amd64.deb https://s3.amazonaws.com/get.influxdb.org/chronograf/chronograf_$(echo $CHRONOGRAF_VERSION)_amd64.deb && \
	dpkg -i /tmp/chronograf_$(echo $CHRONOGRAF_VERSION)_amd64.deb

ADD chronograf.toml /opt/chronograf/chronograf.toml

CMD ["/opt/chronograf/chronograf", "-config=/opt/chronograf/chronograf.toml"]