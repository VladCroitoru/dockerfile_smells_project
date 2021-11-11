FROM python:2
MAINTAINER Anthony Monthe (ZuluPro) <anthony.monthe@gmail.com>


ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8
ENV LC_CTYPE ISO-8859-1

ENV PYTHONIOENCODING=UTF-8
ENV PYTHONUNBUFFERED 1
ENV JARDINFAQ_CONFIG_FILE /conf/jardinfaq.cfg

RUN apt-get update && apt-get install -y \
    git \
    libxml2-dev \
    python \
    build-essential \
    make \
    gcc \
    python-dev \
    locales \
    mysql-client

RUN dpkg-reconfigure locales && \
    locale-gen C.UTF-8 && \
    /usr/sbin/update-locale LANG=C.UTF-8
RUN useradd -ms /bin/bash jardinfaq

ENV repo_dir /jardinfaq/
ADD . $repo_dir
WORKDIR $repo_dir
RUN chown -R jardinfaq $repo_dir

RUN pip install -r requirements.txt MySQL-Python uwsgi -U

USER jardinfaq

CMD ["uwsgi", "--ini", "./uwsgi.ini"]

EXPOSE 3031
