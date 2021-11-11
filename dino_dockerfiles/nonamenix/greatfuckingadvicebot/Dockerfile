FROM python:3.5.2-slim
MAINTAINER Danil Ivanov

ENV PYTHONBUFFERED 1

ENV BOT_LOCAL_SRC ./bot/
ENV BOT_HOME /home/bot
ENV BOT_SRC /home/bot/app/src

RUN mkdir -p $BOT_HOME/logs \
    $BOT_HOME/app/src

WORKDIR $BOT_SRC

ADD $BOT_LOCAL_SRC $BOT_SRC
RUN pip3 install -r requirements.txt

HEALTHCHECK --interval=30s --timeout=3s CMD true  # need for condo

CMD [ "python3", "./main.py"]
