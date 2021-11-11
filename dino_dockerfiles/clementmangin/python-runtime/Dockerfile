#
# Python runtime Dockerfile
#
# https://github.com/clementmangin/docker-python-runtime
#
# Derived from dockerfile/python-runtime
#
# https://github.com/dockerfile/python-runtime
#

# Pull base image.
FROM python:2.7

MAINTAINER Clément Mangin <clement.mangin@gmail.com>

# Set instructions on build
ONBUILD ADD apt-requirements.txt /app/
ONBUILD RUN \
  apt-get update && \
  cat /app/apt-requirements.txt | awk -F# '{print $1}' | xargs apt-get install -y && \
  rm -rf /var/lib/apt/lists/*
ONBUILD ADD requirements.txt /app/
ONBUILD RUN pip install -r /app/requirements.txt
ONBUILD ADD . /app

# Define working directory
WORKDIR /app

# Define default entrypoint
ENTRYPOINT ["python"]