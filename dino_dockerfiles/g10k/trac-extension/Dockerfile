# docker build -t registry.service.mm.consul:5000/trac-extension .

FROM ubuntu:14.04
MAINTAINER telminov <telminov@soft-way.biz>

EXPOSE 8080

VOLUME /data/
VOLUME /conf/
VOLUME /static/
VOLUME /node_modules/
VOLUME /logs/
VOLUME /tls/

RUN apt-get update && \
    apt-get install -y \
                    vim \
                    supervisor \
                    curl \
                    build-essential \
                    python-pip \
                   # для установки через pip lxml==3.4.4 http://stackoverflow.com/questions/5178416/pip-install-lxml-error
                    python-dev \
                    libxml2-dev \
                    libxslt1-dev \
                    zlib1g-dev

RUN curl -sL https://deb.nodesource.com/setup | sudo bash -
RUN apt-get install -y nodejs

RUN mkdir /var/log/trac_extra

# copy source
COPY . /opt/trac_extra
WORKDIR /opt/trac_extra/djtrac

RUN pip install -r requirements.txt
RUN cp djtrac/local_settings.sample.py djtrac/local_settings.py; \
    cp supervisord.conf /etc/supervisor/conf.d/trac_extra.conf

CMD test "$(ls /conf/local_settings.py)" || cp djtrac/local_settings.sample.py /conf/local_settings.py; \
    rm djtrac/local_settings.py;  ln -s /conf/local_settings.py djtrac/local_settings.py; \
    rm -rf static; ln -s /static static; \
    rm -rf node_modules; ln -s /node_modules node_modules; \
    npm install; \
    python ./manage.py migrate; \
    python ./manage.py collectstatic --noinput; \
    /usr/bin/supervisord -c /etc/supervisor/supervisord.conf --nodaemon