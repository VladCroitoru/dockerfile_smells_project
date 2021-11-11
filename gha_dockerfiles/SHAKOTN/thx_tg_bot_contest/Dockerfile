FROM python:3.8.7

ENV PYTHONUNBUFFERED 1

ENV APP_HOME /thx_bot
WORKDIR $APP_HOME
COPY . ./

RUN pip install --upgrade pip
RUN pip install -r ./thx_bot/requirements/requirements.txt -r ./thx_bot/requirements/dev-requirements.txt
