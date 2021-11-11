FROM debian:jessie
MAINTAINER Alex Brandt <alunduil@alunduil.com>

ENV APTGET_UPDATED 20150421.1

RUN apt-get update -qq
RUN apt-get install -qq build-essential locales python3-dev python3-pip python3-setuptools

RUN sed -e '/en_US.UTF-8/s/^# \+//' -i /etc/locale.gen && locale-gen
ENV LANG en_US.UTF-8

RUN useradd -c 'added by docker for muniments' -d / -r muniments

ENV CONFIGURATION_FILE_PATH /usr/local/src/muniments/conf/muniments.ini
ENV LOGGING_CONFIGURATION_FILE_PATH /usr/local/src/muniments/conf/logging.ini

EXPOSE 5000

RUN pip3 install --compile -U pip
RUN pip3 install --compile -U crumbs tornado

ADD . /usr/local/src/muniments
RUN pip3 install --compile file:///usr/local/src/muniments#egg=muniments

USER muniments

ENTRYPOINT [ "/usr/local/bin/muniments" ]
CMD []
