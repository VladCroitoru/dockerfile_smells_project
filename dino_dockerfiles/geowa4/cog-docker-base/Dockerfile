FROM python:3.5-alpine
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY cog-command /usr/bin/cog-command
ONBUILD COPY . /usr/src/app
ONBUILD RUN pip install -U pip && pip install --no-cache-dir .
