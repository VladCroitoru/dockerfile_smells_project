FROM ubuntu:bionic

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -yq rsync pigz gnupg2
RUN mkdir -p ~/.gnupg && echo "disable-ipv6" >> ~/.gnupg/dirmngr.conf
RUN apt-key adv --keyserver keys.gnupg.net --homedir ~/.gnupg --recv-keys 9334A25F8507EFA5
RUN echo "deb http://repo.percona.com/apt squeeze main" >> /etc/apt/sources.list
RUN apt-get update && apt-get install -yq percona-xtradb-cluster-server-5.7 xtrabackup

EXPOSE 3306 4567 4568

ADD entrypoint.sh /
RUN chmod 755 /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["start"]
