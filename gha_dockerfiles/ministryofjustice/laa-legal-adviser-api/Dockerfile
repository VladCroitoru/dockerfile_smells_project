FROM osgeo/gdal:alpine-normal-3.2.1

RUN apk upgrade --no-cache && \
    apk add --no-cache \
      bash \
      postgresql-client \
      tzdata

RUN adduser -D app && \
    cp /usr/share/zoneinfo/Europe/London /etc/localtime

# To install pip dependencies
RUN apk add --no-cache \
      build-base \
      linux-headers \
      postgresql-dev

# Remove the python3 version included by the base image; install the latest version that fixes [CVE-2021-3177]
RUN apk del python3 \
    && apk add --repository=http://dl-cdn.alpinelinux.org/alpine/v3.10/main python3-dev \
    && apk add --repository=http://dl-cdn.alpinelinux.org/alpine/v3.10/community py3-pip \
    && pip install -U setuptools pip==18.1 wheel

WORKDIR /home/app

COPY requirements/base.txt requirements/base.txt
RUN pip install -r ./requirements/base.txt

COPY . .

RUN chown -R app:app laalaa/tmp

# Kubernetes deploy does not need this as it runs it in a Job with the s3 storage backend set,
# so it can be removed once we're fully migrated
RUN python manage.py collectstatic --noinput

USER 1000
EXPOSE 8000

CMD ["docker/run.sh"]
