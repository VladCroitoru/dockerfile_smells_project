FROM debian:jessie
MAINTAINER miurahr@osmf.jp

ENV PATH /usr/local/bin:${PATH}

## security upgrade and install dependencies
RUN apt-get update && apt-get upgrade -y --no-install-recommends && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential make g++ gcc libc6-dev git vim \
    curl libcurl3 libcurl3-nss \
    libssl-dev libyaml-dev libffi-dev \
    ca-certificates software-properties-common yui-compressor \
    libpq5 sqlite3 libmysqlclient18 \
    libpcre3 libxml2 libxslt1.1 \
    libreadline5 libyaml-0-2\
    libmysqlclient-dev libsqlite3-dev libpq-dev \
    libcurl4-openssl-dev libpcre3-dev libxml2-dev libxslt-dev \
    libreadline-gplv2-dev \
    python2.7 python2.7-minimal python2.7-dev python-nose python-coverage \
    python-pysqlite2 libfreetype6-dev \
    libjpeg-dev zlib1g-dev liblcms2-dev libwebp-dev && \
    apt-get clean

## install pip and node/npm
RUN curl -sL https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python - && \
    curl -sL https://deb.nodesource.com/setup | bash - && apt-get install -y nodejs

## workaround and update npm
RUN ln -s /usr/include/freetype2 /usr/local/include/freetype && \
    npm install -g npm@latest && \
    npm install -g less

## install website source
RUN mkdir -p /opt/pyapp/
WORKDIR /opt/pyapp
RUN git clone https://github.com/osmfj/sotmjp-website.git
WORKDIR /opt/pyapp/sotmjp-website

## install requirements for dev
RUN mkdir -p /root/.pip && cp misc/pip.conf /root/.pip/pip.conf
RUN pip install -r requirements/dev.txt

ENV DEBUG True

# init db for dev
# in DEBUG mode, it force use sqlite
#
RUN python manage.py syncdb --noinput
RUN python manage.py migrate
RUN python manage.py loaddata \
      fixtures/auth_user.json \
      fixtures/conference.json \
      fixtures/database_constance.json \
      fixtures/boxes.json \
      fixtures/proposals.json \
      fixtures/sitetree.json \
      fixtures/sotmjp.json \
      fixtures/sponsorship.json \
      fixtures/schedule.json \
      fixtures/teams.json \
      fixtures/restcms_page.json

RUN python ./manage.py compress --force
RUN ./utils/build-css.sh
RUN python ./manage.py collectstatic --noinput

RUN chmod +x utils/docker-init.sh

ENTRYPOINT ["/opt/pyapp/sotmjp-website/utils/docker-init.sh"]
CMD ["app:debug"]

EXPOSE 8000
