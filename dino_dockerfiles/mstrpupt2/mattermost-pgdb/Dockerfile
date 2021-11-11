FROM postgres:9.6.1

ENV POSTGRES_USER=mmuser \
    POSTGRES_PASSWORD=mmuser_password \
    POSTGRES_DB=mattermost

RUN apt-get update \
    && apt-get install -y python-dev lzop pv daemontools curl build-essential \
    && curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | python \
    #&& pip install 'wal-e<1.0.0' \
    && apt-get remove -y build-essential python-dev \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#ADD make_db.sh /docker-entrypoint-initdb.d/
#ADD setup-wale.sh /docker-entrypoint-initdb.d/
#COPY docker-entrypoint.sh /
#RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["postgres"]
