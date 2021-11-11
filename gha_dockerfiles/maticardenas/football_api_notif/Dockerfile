FROM python:3.8

LABEL maintainer "Matias Cardenas"
LABEL description	"Python 3.8 image containing Football Notifications APP"

USER root
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean \
&& apt-get install cron -y

ADD football_notif_crontab /etc/cron.d/football_notif_crontab
RUN chmod 777 /etc/cron.d/football_notif_crontab
RUN crontab /etc/cron.d/football_notif_crontab
RUN touch /var/log/cron_log.log
RUN pip install pipenv

WORKDIR /usr/football_api

COPY ./config ./config
COPY ./dev_scripts ./dev_scripts
COPY ./src ./src
COPY ./tests ./tests
COPY ./Pipfile ./Pipfile
COPY ./Pipfile.lock ./Pipfile.lock
COPY team_fixture_notifier.py .

RUN python -m pipenv install

CMD cron && tail -f /var/log/cron_log.log
