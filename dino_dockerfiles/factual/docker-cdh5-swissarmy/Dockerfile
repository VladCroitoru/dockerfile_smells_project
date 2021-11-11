FROM factual/docker-cdh5-base

# for mongo 3 tools
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
RUN echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list

#postgres
ENV PG_VERSION=9.5
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ "$(lsb_release -sc)"-pgdg main" >> /etc/apt/sources.list.d/pgdg.list
RUN curl -s https://www.postgresql.org/media/keys/ACCC4CF8.asc |  apt-key add -

RUN apt-get update && apt-get install -y sudo git-core postgresql-client-$PG_VERSION mysql-client mongodb-org-shell mongodb-org-tools redis-tools

RUN apt-get clean

ADD https://dl.influxdata.com/influxdb/releases/influxdb-1.2.2_linux_amd64.tar.gz /tmp/influxdb.tar.gz
RUN cd /tmp/ && tar xvfz /tmp/influxdb.tar.gz 
RUN cp /tmp/influxdb-1.2.2-1/usr/bin/influxd /usr/local/bin/ 
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
ADD scripts /root/scripts
ADD bootstrap.sh /etc/my_init.d/099_bootstrap
