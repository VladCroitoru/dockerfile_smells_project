FROM ubuntu:latest
MAINTAINER boogy <theboogymaster@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update \
    && apt-get upgrade -yq \
    && apt-get install -yq git python-dev python-pip python-openssl python-cryptography \
    && pip install --upgrade pip

RUN git clone https://github.com/adaptivethreat/Empire.git /opt/Empire \
    && cd /opt/Empire/setup \
    && export STAGING_KEY="" \
    && bash install.sh

EXPOSE 80 443 8080
WORKDIR /opt/Empire


ENTRYPOINT ["/bin/bash", "-i", "-c"]
CMD ["./empire"]
