from ubuntu:latest
MAINTAINER Charlie Lewis <charliel@lab41.org>

ENV REFRESHED_AT 2016-09-13
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y build-essential \
                       git \
                       libffi-dev \
                       libpq-dev \
                       libssl-dev \
                       python-dev \
                       python-setuptools \
                       rsyslog

RUN easy_install pip

ADD requirements.txt /try41/requirements.txt
ADD patch /try41/patch
ADD static /try41/static
ADD templates /try41/templates

RUN pip install -r /try41/requirements.txt

ADD patch/base.html /usr/local/lib/python2.7/dist-packages/flask_user/templates/base.html
ADD patch/emails /usr/local/lib/python2.7/dist-packages/flask_user/emails

RUN mkdir /try41/templates/flask_user
RUN cp -R /usr/local/lib/python2.7/dist-packages/flask_user/emails /try41/templates/flask_user/

# add rsyslog
RUN sed 's/#\$ModLoad imudp/\$ModLoad imudp/' -i /etc/rsyslog.conf
RUN sed 's/#\$UDPServerRun 514/\$UDPServerRun 514/' -i /etc/rsyslog.conf

# use non root user
RUN groupadd docker
RUN useradd -g docker docker
RUN touch /etc/rsyslog.d/50-default.conf
RUN echo "docker ALL=NOPASSWD: /etc/init.d/rsyslog start" >> /etc/sudoers

ADD api.py /try41/api.py
RUN chown -R docker /try41 /etc/rsyslog.d/50-default.conf

EXPOSE 5000

WORKDIR /try41
CMD printf "*.*\t@$REMOTE_HOST" >> /etc/rsyslog.d/50-default.conf; \
    /etc/init.d/rsyslog start; \
    logger started try41 container $PARENT_HOST; \
    sed -i "s/127.0.0.1/$SUBDOMAIN/g" /try41/api.py; \
    sed -i "s/localhost/$REDIS_HOST/g" /try41/api.py; \
    sed -i "s/rsyslog/$REMOTE_HOST/g" /try41/api.py; \
    sed -i "s/parent/$PARENT_HOST/g" /try41/api.py; \
    sed -i "s/secret/$SECRET_KEY/g" /try41/api.py; \
    sed -i "s|postgresql|$POSTGRESQL_URI|g" /try41/api.py; \
    sed -i "s/smtp/$MAIL_HOST/g" /try41/api.py; \
    sed -i "s/sender/$SENDER/g" /try41/api.py; \
    sed -i "s/USERS=False/USERS=$USERS/g" /try41/api.py; \
    sed -i "s/SSL=False/SSL=$SSL/g" /try41/api.py; \
    sed -i "s/try41-uid/$COOKIE/g" /try41/api.py; \
    python api.py
