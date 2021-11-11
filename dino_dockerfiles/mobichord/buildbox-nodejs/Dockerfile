FROM node:latest

RUN mkdir -p /var/mobichord/logs/ \
    && apt-get update \
    && apt-get install apt-transport-https software-properties-common ca-certificates curl zip python-pip libpython-dev python-dev jq -y --no-install-recommends \
    && curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - \
    && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian jessie stable" \
    && apt-get update \
    && apt-get install docker-ce -y \
    && python --version \
    && pip install boto3 argparse awscli
