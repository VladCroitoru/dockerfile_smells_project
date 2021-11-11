FROM node:10

# AWS CLI needs the PYTHONIOENCODING environment varialbe to handle UTF-8 correctly:
ENV PYTHONIOENCODING=UTF-8

RUN apt-get update && apt-get install -y \
    python3-pip python3-setuptools \
    --no-install-recommends \
    && python3 -m pip install --upgrade --force-reinstall pip

RUN pip3 install awscli

## Install Serverless
WORKDIR /app
RUN npm -g install serverless@1

RUN apt-get install -y locales locales-all
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
