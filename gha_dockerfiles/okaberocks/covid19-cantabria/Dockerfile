FROM python:3.7.2-slim
LABEL maintainer="lca16890"

ARG HTTP_PROXY
ARG HTTPS_PROXY
ARG NO_PROXY

ARG FIREBASE_CREDS_PATH

ENV HTTPS_PROXY=${HTTPS_PROXY}
ENV HTTP_PROXY=${HTTP_PROXY}
ENV NO_PROXY=${NO_PROXY}
ENV https_proxy=${HTTPS_PROXY}
ENV http_proxy=${HTTP_PROXY}
ENV no_proxy=${NO_PROXY}

ENV FIREBASE_CREDS_PATH=${FIREBASE_CREDS_PATH}

ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT 1
ENV PIP_NO_CACHE_DIR=off

WORKDIR /covid19
COPY . .

RUN ls

RUN apt-get update && apt-get install --yes gcc

RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget libpq-dev python3-dev

RUN pip install --upgrade pip pipenv wheel setuptools

RUN pipenv install --system --deploy

CMD [ "python", "./launcher.py" ]
