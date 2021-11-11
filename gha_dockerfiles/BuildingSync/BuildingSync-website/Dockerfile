# VERSION 0.1
# AUTHOR:           Nicholas Long <nicholas.long@nrel.gov>
# DESCRIPTION:      Dockerfile for running BuildingSync Data Selection Tool
# TO_BUILD_AND_RUN: docker-compose build && docker-compose up
FROM alpine:3.8

RUN apk add --no-cache python3 \
        python3-dev \
        postgresql-dev \
        alpine-sdk \
        pcre \
        pcre-dev \
        libxslt-dev \
        linux-headers \
        bash \
        bash-completion \
        git \
        nginx && \
    ln -sf /usr/bin/python3 /usr/bin/python && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    ln -sf /usr/bin/pip3 /usr/bin/pip && \
    pip install --upgrade pip setuptools && \
    pip install git+https://github.com/Supervisor/supervisor@837c159ae51f3 && \
    mkdir -p /var/log/supervisord/ && \
    rm -r /root/.cache && \
    addgroup -g 1000 uwsgi && \
    adduser -G uwsgi -H -u 1000 -S uwsgi && \
    mkdir -p /run/nginx && \
    echo "daemon off;" >> /etc/nginx/nginx.conf && \
    rm -f /etc/nginx/conf.d/default.conf && \
    echo "gem: --no-rdoc --no-ri" > /etc/gemrc

## Note on some of the commands above:
##   - create the uwsgi user and group to have id of 1000
##   - copy over python3 as python
##   - pip install --upgrade pip overwrites the pip so it is no longer a symlink
##   - install supervisor that works with Python3.

WORKDIR /srv/selection-tool
COPY /requirements.txt /srv/selection-tool/requirements.txt
RUN pip install -r requirements.txt

WORKDIR /srv/selection-tool
### Copy over the remaining part of the application and some helpers
COPY . /srv/selection-tool/

### Copy the wait-for-it command to /usr/local
COPY /docker/wait-for-it.sh /usr/local/wait-for-it.sh

# nginx configurations - alpine doesn't use the sites-available directory. Put the selection tool
# configuration file into the /etc/nginx/conf.d/ folder.
COPY /docker/nginx.conf /etc/nginx/conf.d/selection_tool.conf
# Supervisor looks in /etc/supervisor for the configuration file.
COPY /docker/supervisord.conf /etc/supervisor/supervisord.conf

# entrypoint sets some permissions on directories that may be shared volumes
COPY /docker/selection-tool-entrypoint.sh /usr/local/bin/selection-tool-entrypoint
RUN chmod 775 /usr/local/bin/selection-tool-entrypoint
ENTRYPOINT ["selection-tool-entrypoint"]

CMD ["supervisord"]

EXPOSE 80
