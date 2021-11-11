# djpodcaster
FROM thinkwhere/gdal-python

MAINTAINER gaolei gaolei@liheran.com

WORKDIR /data/src

COPY ./requirements.txt /data/src/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /data/src

COPY docker-entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
