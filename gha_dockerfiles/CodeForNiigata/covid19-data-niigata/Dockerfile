FROM python:3.9-slim

RUN mkdir /app
WORKDIR /app

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN mkdir -p /usr/share/man/man1

RUN apt-get update
RUN apt-get -y install default-jdk locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

RUN pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install pipenv

ADD Pipfile Pipfile
ADD Pipfile.lock Pipfile.lock
ADD src src

RUN pipenv install

CMD pipenv run main
