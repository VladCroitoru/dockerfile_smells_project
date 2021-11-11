FROM dtank/core:latest

MAINTAINER benharker@mac.com

RUN wget -O - http://ppa.moosefs.com/moosefs.key | apt-key add - && echo "deb http://ppa.moosefs.com/current/apt/ubuntu/trusty trusty main" >> /etc/apt/sources.list.d/moosefs.list ;
RUN apt-get update ; apt-get install -y moosefs-chunkserver nano sed ; rm -rf /var/lib/apt/lists/* && mv /etc/mfs/mfschunkserver.cfg.sample /etc/mfs/mfschunkserver.cfg ; mv /etc/mfs/mfshdd.cfg.sample /etc/mfs/mfshdd.cfg ; echo "/home/chunks/ -5GiB" >> /etc/mfs/mfshdd.cfg ; /bin/sed s/# LABELS =/LABELS = D/g /etc/mfs/mfschunkserver.cfg ; /bin/echo "LABELS = Z" >> /etc/mfs/mfschunkserver.cfg ; 

RUN /bin/mkdir /home/chunks ; /bin/chmod -R 777 /home/chunks ; 

EXPOSE 9419
EXPOSE 9420
EXPOSE 9421
EXPOSE 9422

CMD ["/usr/sbin/mfschunkserver -f start"]
