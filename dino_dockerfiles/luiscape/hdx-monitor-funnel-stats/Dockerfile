##################################################
# Funnel Stats micro-service. Supports the
# HDX Monitor.
##################################################

FROM python:2.7.10

MAINTAINER Luis Capelo <capelo@un.org>


# Add local files and install dependencies.
ADD . /hdx-monitor-funnel-stats

WORKDIR "/hdx-monitor-funnel-stats"

RUN make setup

# Installing cron jobs.
RUN \
  apt-get update \
  && apt-get install vim cron python-virtualenv -y \
  && cp /hdx-monitor-funnel-stats/bin/daily_collection.sh /etc/cron.daily/daily_collection.sh \
  && cp /hdx-monitor-funnel-stats/bin/patch_week.sh /etc/cron.daily/patch_week.sh

EXPOSE 7000

CMD ["make", "run"]