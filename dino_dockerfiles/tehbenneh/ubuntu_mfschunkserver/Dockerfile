FROM ubuntu:14.04
MAINTAINER Ben Harker (benharker@mac.com)

RUN apt-get update && apt-get install wget -y ;
RUN wget -O - http://ppa.moosefs.com/moosefs.key | apt-key add - ; echo "deb http://ppa.moosefs.com/current/apt/ubuntu/trusty trusty main" >> /etc/apt/sources.list.d/moosefs.list ; apt-get update ; apt-get install -y facter moosefs-chunkserver iftop ;

RUN mkdir -p /mnt/sdb1 ;

RUN echo "/mnt/sdb1 10GiB" >> /etc/mfs/mfshdd.cfg ;
RUN mv /etc/mfs/mfschunkserver.cfg.sample /etc/mfs/mfschunkserver.cfg ;
RUN sed -i '/# LABELS =/c\LABELS = D' /etc/mfs/mfschunkserver.cfg ;
RUN sed -i '/MFSCHUNKSERVER_ENABLE=false/c\MFSCHUNKSERVER_ENABLE=true' /etc/default/moosefs-chunkserver ;
RUN chmod -R 777 /mnt/sdb1 ;

EXPOSE 9419
EXPOSE 9420
EXPOSE 9422

RUN chmod -R 777 /mnt/sdb1 ;

CMD ["/usr/sbin/mfschunkserver", "-f", "start"]
