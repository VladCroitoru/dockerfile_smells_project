
FROM python:3.7

ENV PYTHONBUFFERED=0 \
    PYTHONUNBUFFERED=1 \
    PACKAGES=cron

WORKDIR /usr/src/app

# 🤮
CMD /entrypoint.sh cron && tail -f /var/log/cron.log

RUN apt-get update \
    && apt-get -y --no-install-recommends install ${PACKAGES} \
    && touch /var/log/cron.log \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/samber/powEUr.git /usr/src/app \
    && cat /usr/src/app/crontab | crontab - \
    && cp /usr/src/app/entrypoint.sh /

RUN pip3 install -r requirements.txt
