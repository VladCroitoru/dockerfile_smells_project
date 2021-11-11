FROM ubuntu:18.04

RUN  apt-get update \
  && apt-get install -y wget \
     gnupg2

RUN wget -qO - https://www.mongodb.org/static/pgp/server-3.4.asc | apt-key add -

RUN echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.4.list

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.6 \
    python3-pip \
    libpython3.6 \
    jq \
    mongodb-org \
    locales \
    locales-all \
    python3-setuptools \
    g++ \
    python3-dev \
    npm \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /src

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

COPY requirements.txt /src/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt --proxy=${HTTP_PROXY}
RUN npm install elasticdump -g

COPY . /src
