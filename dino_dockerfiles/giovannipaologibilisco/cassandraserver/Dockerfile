FROM cassandra:latest

RUN \
  echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee /etc/apt/sources.list.d/webupd8team-java.list && \
  echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list && \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 && \
  apt-get update && \
  echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections && \
  apt-get install oracle-java8-installer netcat-openbsd -y

COPY setup_tables.txt /setup_tables.txt
COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY cassandra-env.sh /etc/cassandra/cassandra-env.sh
COPY jvm.options /etc/cassandra/jvm.options
RUN chown -R cassandra: /etc/cassandra
RUN chmod +x /docker-entrypoint.sh
RUN mkdir -p /usr/share/cassandra/logs
RUN chmod 777 /usr/share/cassandra/logs

USER cassandra
CMD ["cassandra"]
ENTRYPOINT ["/docker-entrypoint.sh"]
