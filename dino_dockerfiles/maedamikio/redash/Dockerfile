FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    curl \
    postgresql \
    redis-server \
    sudo \
    wget \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

RUN service postgresql start && service redis-server start && curl -sL https://raw.githubusercontent.com/getredash/redash/master/setup/ubuntu/bootstrap.sh | bash

EXPOSE 80

CMD service nginx start && \
    service postgresql start && \
    service redis-server start && \
    service supervisor start && \
    tail -f /dev/null
