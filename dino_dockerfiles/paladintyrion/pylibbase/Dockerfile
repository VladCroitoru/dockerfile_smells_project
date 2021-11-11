# dockerfile for python lib
FROM python:3.6.5-slim-jessie
MAINTAINER PaladinTyrion "paladintyrion@gmail.com"

WORKDIR /usr/src/app
ENV DEBIAN_FRONTEND noninteractive
COPY ./requirements.txt ./
RUN set -ex \
    && mkdir -p /workplace/lib \
    && apt-get update \
    && apt-get install -y apt-utils dialog libreadline6

RUN apt-get install -y --allow-unauthenticated apt-utils tzdata bash procps vim wget curl tar mlocate lrzsz pkg-config python-dev gcc libfreetype6-dev libpng12-0 \
    && apt-get install -y subversion git \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && pip install --no-cache-dir --upgrade setuptools \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y --purge subversion git \
    && apt-get autoremove -y \
    && apt-get autoclean -y \
    && apt-get remove -y \
    && apt-get clean -y

WORKDIR /workplace/lib
VOLUME [ "/workplace/lib" ]

CMD [ "/bin/bash" ]
