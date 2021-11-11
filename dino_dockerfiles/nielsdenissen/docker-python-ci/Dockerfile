FROM python

MAINTAINER Niels Denissen <nielsdenissen@gmail.com>

# Update apt-get
RUN apt-get update \
  && apt-get -y install libpq-dev gcc

# Install requirements pip
RUN pip install pylint coverage pytest --quiet
