FROM python:3.10-slim

SHELL ["/bin/bash", "-ex", "-o", "pipefail", "-c"]

WORKDIR /mnt
VOLUME /mnt

EXPOSE 5000

ENV PATH=/root/.local/bin:$PATH

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    curl \
    inotify-tools \
    openjdk-17-jre \
    rsync \
    silversearcher-ag \
 && curl -sL https://deb.nodesource.com/setup_16.x | bash -ex \
 && apt-get install -y --no-install-recommends \
    nodejs \
 && pip install --no-cache-dir --user pipenv \
 && curl -sSL https://www.antlr.org/download/antlr-4.9-complete.jar > /root/antlr-4.jar \
 && apt-get purge -y \
    curl \
 && apt-get autoremove -y \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

COPY package-lock.json \
     package.json \
     Pipfile \
     Pipfile.lock \
     ./
RUN pipenv sync -d --pre \
 && npm ci \
 && mv node_modules /tmp

ENTRYPOINT ["./entrypoint.sh"]
