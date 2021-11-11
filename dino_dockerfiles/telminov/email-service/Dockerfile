# docker build -t telminov/email-service .
FROM ubuntu:16.04

RUN apt-get clean && apt-get update && \
    apt-get install -y \
                    vim curl locales wget gcc \
                    supervisor software-properties-common python-software-properties

RUN add-apt-repository -y ppa:jonathonf/python-3.6 && \
    apt-get update && apt-get install -y python3.6 python3.6-dev python3.6-venv && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python3.6 get-pip.py && \
    ln -s /usr/bin/python3.6 /usr/local/bin/python3

RUN locale-gen ru_RU.UTF-8
ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU:ru
ENV LC_ALL ru_RU.UTF-8

# setup filebeat
RUN curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-5.4.0-amd64.deb
RUN dpkg -i filebeat-5.4.0-amd64.deb
RUN rm filebeat-5.4.0-amd64.deb

RUN pip3 install django==1.11.3 \
        sw-python-email-devino==0.0.1 \
        djangorestframework==3.6.3 \
        jsonfield==2.0.2 \
        django-bootstrap3==9.0.0 \
        gunicorn==19.6.0 \
        ipython \
        raven==6.1.0 \
        psycopg2==2.7.1

RUN mkdir /var/log/app

# copy source
COPY . /opt/app
WORKDIR /opt/app

RUN cp project/local_settings.sample.py project/local_settings.py

COPY supervisor/prod.conf /etc/supervisor/conf.d/app.conf

EXPOSE 80

VOLUME /data/
VOLUME /conf/
VOLUME /static/
VOLUME /tls/


CMD test "$(ls /conf/local_settings.py)" || cp project/local_settings.py /conf/local_settings.py; \
    test "$(ls /conf/filebeat.yml)" || cp /etc/filebeat/filebeat.yml /conf/filebeat.yml; \
    rm project/local_settings.py; ln -s /conf/local_settings.py project/local_settings.py; \
    rm /etc/filebeat/filebeat.yml; ln -s /conf/filebeat.yml /etc/filebeat/filebeat.yml; \
    rm -rf static; ln -s /static static; \
    service filebeat start; \
    python3 ./manage.py migrate; \
    python3 ./manage.py collectstatic --noinput; \
    /usr/bin/supervisord