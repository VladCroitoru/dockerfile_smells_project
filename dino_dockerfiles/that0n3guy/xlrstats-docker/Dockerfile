FROM tutum/apache-php

RUN apt-get update && apt-get install -yq git && rm -rf /var/lib/apt/lists/*
RUN rm -fr /app

ENV xlrversion v3.0.0-beta.10

RUN git clone https://github.com/XLRstats/xlrstats-web-v3.git /app
RUN cd /app && git checkout $xlrversion
RUN mkdir -p /app/app/tmp/cache/models && touch /app/app/tmp/cache/models/empty
RUN mkdir -p /app/app/tmp/cache/persistent && touch /app/app/tmp/cache/persistent/empty
RUN chown -R www-data:www-data /app

EXPOSE 80
VOLUME /app/app/Config
