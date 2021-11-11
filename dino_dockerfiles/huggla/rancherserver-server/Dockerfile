FROM rancher/server:v1.6.10

RUN service mysql stop \
  && rm -rf /var/lib/mysql/* \
  && mv /usr/bin/entry /usr/bin/entry.org

COPY ./initdb /var/lib/mysql
COPY ./entry /usr/bin/entry

RUN chmod ugo+x /usr/bin/entry
