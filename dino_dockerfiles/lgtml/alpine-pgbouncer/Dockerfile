FROM gliderlabs/alpine:3.2

RUN \
  apk --update add autoconf autoconf-doc automake c-ares c-ares-dev curl gcc libc-dev libevent libevent-dev libtool make man openssl-dev pkgconfig yaml python py-pip sqlite-dev && \
  curl -o  /tmp/pgbouncer-1.7.2.tar.gz -L https://pgbouncer.github.io/downloads/files/1.7.2/pgbouncer-1.7.2.tar.gz && \
  cd /tmp && \
  tar xvfz /tmp/pgbouncer-1.7.2.tar.gz && \
  cd pgbouncer-1.7.2 && \
  ./configure --prefix=/usr && \
  make && \
  cp pgbouncer /usr/bin && \
  mkdir -p /etc/pgbouncer /var/log/pgbouncer /var/run/pgbouncer && \
  cp etc/pgbouncer.ini /etc/pgbouncer/ && \
  cp etc/userlist.txt /etc/pgbouncer/ && \
  adduser -D -S pgbouncer && \
  chown pgbouncer /var/run/pgbouncer && \
  pip install jinja2 && \
  mkdir -p /templates && \
  cd /tmp && \
  rm -rf /tmp/pgbouncer*  && \
  rm -f /etc/pgbouncer/pgbouncer.ini && \
  apk del --purge autoconf autoconf-doc automake c-ares-dev curl gcc libc-dev libevent-dev libtool make man openssl-dev pkgconfig sqlite-dev py-pip
ADD templates/* /templates/
RUN chown -R pgbouncer /etc/pgbouncer && chown -R pgbouncer /templates
ADD bin/start.sh /start.sh
ADD bin/generate_config.py /generate_config.py
USER pgbouncer
VOLUME /etc/pgbouncer
EXPOSE 6432
CMD /start.sh
