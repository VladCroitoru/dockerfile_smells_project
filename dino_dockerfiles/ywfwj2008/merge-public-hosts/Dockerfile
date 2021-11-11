FROM node:latest
MAINTAINER malaohu <tua@live.cn>

RUN buildDeps='git' \
    && apt-get update \
    && apt-get install -y $buildDeps \
    && git clone https://github.com/malaohu/Merge-Public-Hosts.git /app \
    && cd /app \
    && npm install \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge -y --auto-remove $buildDeps

EXPOSE 3000

CMD npm start
