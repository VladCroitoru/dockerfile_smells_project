###########################################################
# Container that runs a micro-service for calculating
# the statistics an organization has in HDX.
###########################################################

FROM node:latest

MAINTAINER Luis Capelo <capelo@un.org>

RUN \
  git clone https://github.com/luiscape/hdx-monitor-org-stats \
  && cd hdx-monitor-org-stats \
  && make setup


WORKDIR '/hdx-monitor-org-stats'

EXPOSE 2000

CMD ["make", "run"]
