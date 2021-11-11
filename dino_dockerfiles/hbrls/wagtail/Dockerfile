FROM python:3.8.1-slim-buster

ENV DEBIAN_FRONTEND=noninteractive

COPY appl/requirements.txt /
COPY envfile /
COPY uwsgi.yaml /

RUN \
  apt-get update && \
  apt-get install -y build-essential python-dev libpcre3 libpcre3-dev curl locales && \
  apt-get install -y default-libmysqlclient-dev && \
  echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen  && \
  echo "zh_CN.UTF-8 UTF-8" >> /etc/locale.gen  && \
  locale-gen && \
  dpkg-reconfigure locales && \
  /usr/sbin/update-locale LANG=en_US.UTF-8 && \
  pip install uwsgi && \
  pip install -r requirements.txt && \
  rm -rf /var/lib/apt/lists/* && \
  mkdir -p /var/app && chown -R www-data:www-data /var/app && \
  mkdir -p /data/log && chown -R www-data:www-data /data/log

ENV \
 LC_ALL en_US.UTF-8 \
 LANG en_US.UTF-8 \
 LANGUAGE en_US.UTF-8

WORKDIR /var/app

# USER www-data

EXPOSE 3031

CMD ["/usr/local/bin/uwsgi", "-y", "/uwsgi.yaml"]
