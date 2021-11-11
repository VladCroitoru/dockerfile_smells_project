FROM alpine:latest
MAINTAINER zeagler

RUN apk add --no-cache --update \
            ca-certificates \
            gcc \
            docker \
            musl-dev \
            postgresql-dev \
            python3 \
            python3-dev \
            tzdata \
    && python3 -m ensurepip \
    && rm -r /usr/lib/python*/ensurepip \
    && pip3 install --upgrade pip\
                   boto3 \
                   cattle \
                   cherrypy \
                   croniter \
                   docker-py \
                   mako \
                   psycopg2 \
                   pyyaml \
    && apk del --purge gcc musl-dev python3-dev \
    && rm -rf /root/.cache
    
RUN mkdir /tangerine

COPY *.py README.md /tangerine/
COPY static /tangerine/static
CMD ["python3", "tangerine.py"]
WORKDIR /tangerine