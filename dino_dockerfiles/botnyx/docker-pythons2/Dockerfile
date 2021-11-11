FROM python:3.6-alpine

# Install redis
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.1/main" >> /etc/apk/repositories && \
    apk add --update redis=3.2.11-r0 && \
    rm -rf /var/cache/apk/* && \
    mkdir /data && \
    chown -R redis:redis /data && \
    echo -e "include /etc/redis-local.conf\n" >> /etc/redis.conf

# Add the files
#ADD root /

VOLUME ["/data"]

# Expose the ports for redis
EXPOSE 6379



RUN apk add --update --no-cache postgresql-dev gcc python3-dev musl-dev

RUN pip3 install s2sphere
RUN pip3 install pymongo
RUN pip3 install pymysql
RUN pip3 install redis
RUN pip3 install pdo
RUN pip3 install cassandra-driver
RUN pip3 install elasticsearch
RUN pip3 install pytz
RUN pip3 install psycopg2
RUN pip3 install requests
RUN pip3 install crate
RUN pip3 install bz2file



CMD [ "python", "/app/parser/json-processor.py" ]
