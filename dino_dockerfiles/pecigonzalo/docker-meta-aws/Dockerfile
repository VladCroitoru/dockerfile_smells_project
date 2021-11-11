FROM debian:stretch-slim
MAINTAINER Gonzalo Peci <pecigonzalo@outlook.com>

ARG DEBIAN_FRONTEND=noninteractive

ENV AWS_REGION ''
ENV MANAGER_SECURITY_GROUP_ID ''
ENV WORKER_SECURITY_GROUP_ID ''

EXPOSE 5000

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        jq \
        libltdl-dev \
        python-setuptools \
        python-wheel \
        python-pip \
        wget && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

RUN pip install -U pip && \
    pip install --no-cache-dir awscli

COPY ./app /app
WORKDIR /app

RUN pip install -r requirements.txt

COPY entry.sh /

CMD ["/entry.sh"]
