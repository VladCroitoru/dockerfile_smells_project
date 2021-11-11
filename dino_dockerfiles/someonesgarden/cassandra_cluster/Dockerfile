FROM cassandra:latest
MAINTAINER Daisuke Nishimura 1.0 d@someonesgarden.org
ENV container docker
#RUN apt-get update && apt-get clean all
#RUN apt-get install -y vim && apt-get clean all
RUN export TERM=xterm
COPY create_keyspace.cql /

EXPOSE 7000 7001 7199 9042 9160
