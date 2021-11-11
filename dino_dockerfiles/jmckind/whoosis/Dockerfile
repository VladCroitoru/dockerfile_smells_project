FROM python:3-alpine

LABEL maintainer="jmckind@gmail.com"

RUN apk add --no-cache \
  gcc \
  mariadb-client \
  mariadb-dev \
  musl-dev \
  openssl \
  postgresql-client \
  postgresql-dev \
  sqlite

RUN mkdir -p /opt/whoosis /etc/whoosis

COPY etc/gunicorn.conf /etc/whoosis/gunicorn.conf
COPY etc/local_settings.py.sample /etc/whoosis/local_settings.py
COPY bin/* /usr/local/bin/

RUN wget -O /tmp/whoosis.tar.gz $(wget -qO - https://api.github.com/repos/jmckind/whoosis/releases/latest | grep -o 'browser_download_url.*' | cut -d'"' -f3)
RUN pip install /tmp/whoosis.tar.gz

ENV PYTHONPATH /etc/whoosis
WORKDIR /opt/whoosis

ENTRYPOINT ["dumb-init", "--"]
CMD ["gunicorn", "--config", "/etc/whoosis/gunicorn.conf", "whoosis.wsgi"]
EXPOSE 4778
