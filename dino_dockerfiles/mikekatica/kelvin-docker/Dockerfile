from debian:9

ARG KELVIN_VERSION="0.0.8"

RUN apt-get update -y && apt-get install -y wget

RUN cd /tmp && wget https://github.com/stefanwichmann/kelvin/releases/download/v$KELVIN_VERSION/kelvin-linux-amd64-v$KELVIN_VERSION.tar.gz && tar -zxvf *.tar.gz && rm -rf *.tar.gz && mv -v kelvin* /opt/kelvin

ENTRYPOINT [ "/opt/kelvin/kelvin" ]
