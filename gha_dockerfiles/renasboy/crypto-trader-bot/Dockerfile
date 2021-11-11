FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /crypto-trader-bot
WORKDIR /crypto-trader-bot
ADD . /crypto-trader-bot/
RUN pip install -r requirements.txt
ENTRYPOINT [ "/crypto-trader-bot/docker-entrypoint.sh" ]
