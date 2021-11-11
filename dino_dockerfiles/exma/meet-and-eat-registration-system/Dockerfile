FROM python:2.7

MAINTAINER "Jan Losinski <losinski@wh2.tu-dresden.de>"

ADD requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update && \
    apt-get -y install --no-install-recommends locales && \
    sed -i -r 's/# de_DE(.*)/de_DE\1/' /etc/locale.gen && \
    locale-gen && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
ENV LANG=de_DE.UTF-8 LC_ALL=de_DE.UTF-8

ADD entrypoint.sh /entryoint
ADD config_example.yaml /config.yaml
ADD uwsgi.ini /uwsgi.ini
ADD src /app

ENV CONFIG_FILE_PATH "/config.yaml"

VOLUME ["/data"]
EXPOSE 8080

WORKDIR /app

ENTRYPOINT ["/entryoint"]
