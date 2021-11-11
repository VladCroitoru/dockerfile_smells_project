FROM python:3.5.2

RUN mkdir -p /app/log/
ADD requirements.txt /app/
WORKDIR /app/
RUN pip install -r requirements.txt

ADD latinoware.py mongo.py \
    docker-entrypoint.sh /app/

EXPOSE 8080

ENTRYPOINT ["/app/docker-entrypoint.sh"]