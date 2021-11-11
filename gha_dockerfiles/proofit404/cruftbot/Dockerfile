FROM ubuntu:latest

ARG APP_UID

ARG APP_GID

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update

RUN apt-get install -y gcc curl git make software-properties-common

RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update

RUN apt-get install -y python3.9 python3.9-venv python3.9-dev

RUN ln -s /usr/bin/python3.9 /usr/local/sbin/python3.9

RUN ln -s /usr/bin/python3.9 /usr/local/sbin/python3

RUN ln -s /usr/bin/python3.9 /usr/local/sbin/python

RUN curl -fsSL https://deb.nodesource.com/setup_15.x | bash -

RUN apt-get install -y nodejs

RUN curl -fsSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/usr/local/poetry python

RUN chmod go+x /usr/local/poetry/bin/poetry

RUN ln -s /usr/local/poetry/bin/poetry /usr/local/bin/poetry

RUN npm install -g npm

RUN mkdir /app/

WORKDIR /app/

RUN groupadd --gid ${APP_GID} app

RUN useradd --uid ${APP_UID} --gid app --create-home app

USER app

RUN mkdir -p $HOME/.cache/pypoetry/virtualenvs
