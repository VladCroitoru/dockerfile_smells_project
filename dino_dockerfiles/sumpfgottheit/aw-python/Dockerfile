FROM python:3.6-alpine3.6
MAINTAINER florian.sachs@gmx.at
ENV version=1


RUN apk update 
RUN apk add bash openblas-dev openblas musl-dev postgresql-client postgresql-dev git curl linux-headers tzdata jq zlib-dev jpeg-dev
RUN cp /usr/share/zoneinfo/Europe/Vienna /etc/localtime
RUN pip install numpy 
RUN pip install psycopg2 
RUN pip install flask sqlalchemy docopt ipython click logdna requests records colorama uwsgi pytest tabulate flask-cors pyjwt passlib python-dateutil pytz imaplib2
COPY adapt_user.sh /
COPY entrypoint.sh /
RUN rm -fr /tmp/* /var/cache/apk/*
ENTRYPOINT /entrypoint.sh


