FROM node:6-slim
MAINTAINER Gabriel Trabanco Llano <gtrabanco@users.noreply.github.com> (https://gabi.io)

ENV VERSION 0.3.6

RUN groupadd user \
    && useradd --create-home --home-dir /home/user -g user user \
    && apt-get update \
    && apt-get install -y git --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \

RUN npm cache clean && npm install --global dynhost

USER user

WORKDIR /home/user
VOLUME /home/user/.env

CMD ["/usr/bin/dynhost"]
