FROM debian:jessie
MAINTAINER Kevin Littlejohn <kevin@littlejohn.id.au>

RUN apt-get -yq update \
  && apt-get -yq install git groff less python python-dev python-pip libyaml-dev jq libmysqlclient-dev curl \
  && pip install awscli MySQL-python boto3 \
  && curl -O -L http://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python_2.1.3-1debian8.2_all.deb \
  && dpkg -i mysql-connector-python_2.1.3-1debian8.2_all.deb \
  && rm mysql-connector-python_2.1.3-1debian8.2_all.deb

RUN aws configure set region ap-southeast-2

WORKDIR /app
