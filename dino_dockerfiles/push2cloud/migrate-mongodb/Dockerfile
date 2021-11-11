FROM library/mongo:3.4.10

RUN apt-get update && \
    apt-get install -y jq && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY ./migrate.sh /migrate.sh

CMD [ "/migrate.sh" ]
