FROM node:9.11.1

RUN npm install jscpd@0.6.17 -g

RUN set -x \
  && curl -s -LO "https://github.com/jpmens/jo/releases/download/v1.1/jo-1.1.tar.gz" > jo-1.1.tar.gz \
  && tar xvzf jo-1.1.tar.gz \
  && cd jo-1.1 \
  && ./configure \
  && make check \
  && make install \
  && cd ../ \
  && rm jo-1.1.tar.gz


RUN set -x \
  && curl -s -LO "https://github.com/stedolan/jq/releases/download/jq-1.5/jq-1.5.tar.gz" \
  && tar -xvzf jq-1.5.tar.gz \
  && cd jq-1.5 \
  && ./configure \
  && make \
  && make install \
  && cd ../ \
  && rm jq-1.5.tar.gz

ADD ccchkr.sh /usr/local/bin/ccchkr.sh
