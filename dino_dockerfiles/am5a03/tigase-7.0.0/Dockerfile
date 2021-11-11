# Ubuntu/precise is the main distribution
FROM debian:7

# auto validate license
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections

# setup java ppa
RUN rm -rvf /var/lib/apt/lists/*
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
RUN apt-get update
RUN apt-get install ca-certificates -y
RUN apt-get install --no-install-recommends -y libssl1.0.0 openssl postgresql-client
RUN apt-get install --no-install-recommends -y software-properties-common python-software-properties
RUN apt-get install oracle-java7-installer -y

# add wget
RUN apt-get update
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get install --no-install-recommends -y wget oracle-java7-installer

# download and install tigase
RUN wget 'http://projects.tigase.org/attachments/download/2321/tigase-server-7.0.0-b3802-dist-max.tar.gz' -O /tmp/tigase-server.tar.gz
RUN tar -xC /opt -zf /tmp/tigase-server.tar.gz
RUN mv /opt/tigase-server* /opt/tigase-server

# setup tigase
ADD tigase.conf /opt/tigase-server/etc/tigase.conf
ADD init.properties /opt/tigase-server/etc/init.properties
RUN cd /opt/tigase-server; test -d ./scripts/admin || cp -r ./src/main/groovy/tigase/admin ./scripts/admin 
RUN echo "call TigAddUserPlainPw('admin@tigase.net', '123456');" >> /opt/tigase-server/database/derby-schema-5-1.sql
RUN cd /opt/tigase-server; ./scripts/db-create-derby.sh tigasedb; cat derby-db-create.txt

# run tigase
CMD cd /opt/tigase-server; java -version; ./scripts/tigase.sh run etc/tigase.conf; wait $!
EXPOSE 5222 5223 5269 5270 5290

