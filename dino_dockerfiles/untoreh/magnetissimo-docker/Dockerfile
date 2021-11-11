FROM alpine

COPY ./*.sh /usr/local/bin/

RUN apk add $(apk --update search -q erlang) elixir postgresql openrc git libressl nodejs-npm
RUN openrc && \
  touch /run/openrc/softlevel && \
  rm /lib/rc/sh/rc-cgroup.sh && \
  /etc/init.d/postgresql start && \
  git clone https://github.com/sergiotapia/magnetissimo.git && \
  cd magnetissimo && \
  echo -e 'Y\nY\n' | mix deps.get && \
  createdb.sh && \
  config.sh && \
  echo -e 'Y\nY\n' | mix ecto.create && \
  echo -e 'Y\nY\n' | mix ecto.migrate && \
  npm install && \
  /etc/init.d/postgresql stop && \
  rm -rf /var/cache/apk/*

EXPOSE 4000
VOLUME ["/var/lib/postgresql"]

CMD ["/bin/sh", "-c", "openrc -o default; /etc/init.d/postgresql restart; cd /magnetissimo && exec mix phoenix.server"]




