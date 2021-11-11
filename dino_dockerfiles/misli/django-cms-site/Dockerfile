FROM ubuntu:bionic

LABEL name="django CMS"
LABEL maintainer="Jakub Dorňák <jakub.dornak@misli.cz>"

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# install requirements and generate czech locale
RUN apt-get update \
 && apt-get -y upgrade \
 && apt-get -y --no-install-recommends install \
    build-essential \
    gcc \
    git \
    libmysqlclient-dev \
    locales \
    libicu-dev \
    mariadb-client \
    memcached \
    nginx \
    postgresql-client \
    python3-dev \
    python3-pip \
    python3-setuptools \
    sqlite3 \
    supervisor \
 && apt-get -y autoremove \
 && apt-get -y clean \
 && pip3 install --upgrade pip \
 && ln -s /usr/bin/python3 /usr/local/bin/python \
 && echo cs_CZ.UTF-8 UTF-8 > /etc/locale.gen && locale-gen
ENV LC_ALL cs_CZ.UTF-8

# install required packages
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

# patch installed packages
COPY patch /app/patch
RUN patch /usr/local/lib/python3.6/dist-packages/cmsplugin_filer_folder/cms_plugins.py patch/cmsplugin_filer_folder-cms_plugins.patch \
 && rm -r patch

# install cms_site
COPY . /src
RUN pip install --no-cache-dir /src \
 && cp -a /src/translations/* /usr/local/lib/python3.6/dist-packages/ \
 && cp -a /src/conf /src/bin /src/startup ./ \
 && rm -r /src \
 && mkdir -p data htdocs/media htdocs/static run \
 && django-cms collectstatic --no-input \
 && rm data/db.sqlite3 \
 && chown www-data:www-data data htdocs/media run

CMD ["/app/bin/run-supervisord"]
