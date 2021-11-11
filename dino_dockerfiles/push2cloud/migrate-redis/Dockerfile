FROM node:8.11.1

RUN echo "deb http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list && \
    echo "deb-src http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list && \
    wget https://www.dotdeb.org/dotdeb.gpg && \
    apt-key add dotdeb.gpg && \
    rm dotdeb.gpg && \
    apt-get update && \
    apt-get install -y jq bash redis-tools && \
    rm -rf /var/lib/apt/lists/* && \
    npm install -g redis-command-stream-fork

COPY ./migrate.sh /migrate.sh

CMD [ "/migrate.sh" ]
