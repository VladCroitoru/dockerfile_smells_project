#####################################################
# Docker container for the download search service.
# Based in a Python container.
#####################################################

FROM python:2.7.10

USER root

RUN \
  apt-get update \
  && apt-get upgrade \
  && apt-get install -y git

RUN \
  git clone https://github.com/luiscape/hdx-monitor-download-search \
  && cd hdx-monitor-download-search \
  && make setup

WORKDIR "/hdx-monitor-download-search"

EXPOSE 1000

CMD ["make", "run"]
