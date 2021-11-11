from node:6

maintainer panthro.rafael@gmail.com

env NODE_ENV prod

RUN apt-get update && apt-get install -y unzip && rm -rf /var/lib/apt/lists/*

workdir /app

RUN cd /tmp && wget -qO- -O tmp.zip https://github.com/mallocator/Elasticsearch-Exporter/archive/master.zip && unzip tmp.zip && rm tmp.zip \
&& cp -r Elasticsearch-Exporter-master/. /app && rm -rf Elasticsearch-Exporter-master

RUN npm install --production

ENTRYPOINT node exporter.js
