FROM python:3.5-slim
MAINTAINER Mopsalarm


RUN mkdir -p /app
WORKDIR /app

ONBUILD COPY . /app
ONBUILD RUN \
  if ! [ -f ./onbuild.sh ] ; then \
    echo '#!/bin/sh' > ./onbuild.sh ; \
    chmod a+x onbuild.sh; \
  fi ; \
  ./onbuild.sh prepare || exit 1 ; \
  pip install --no-cache-dir -r requirements.txt || exit 2 ; \
  ./onbuild.sh cleanup || exit 3;
