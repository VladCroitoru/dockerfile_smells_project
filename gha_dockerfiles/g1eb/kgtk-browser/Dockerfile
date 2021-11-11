# A dockerfile for running the kgtk-browser
FROM python:3.7-stretch

RUN mkdir /src

COPY requirements.txt /src/requirements.txt

RUN pip install -r /src/requirements.txt

COPY kgtk_browser_config.py /src/
COPY kgtk_browser_app.py /src/
COPY browser/backend/ /src/browser/backend/
COPY app/ /src/app/

ARG FLASK_ENV=production
ENV FLASK_ENV=$FLASK_ENV

ARG FLASK_APP=kgtk_browser_app.py
ENV FLASK_APP=$FLASK_APP

ARG KGTK_BROWSER_CONFIG=kgtk_browser_config.py
ENV KGTK_BROWSER_CONFIG=$KGTK_BROWSER_CONFIG

WORKDIR /src
EXPOSE 5006
