FROM ubuntu:14.04
MAINTAINER Ben Harker (benharker@mac.com)

RUN apt-get update && apt-get install wget -y ;
RUN wget -O - http://ppa.moosefs.com/moosefs.key | apt-key add - ; echo "deb http://ppa.moosefs.com/current/apt/ubuntu/trusty trusty main" >> /etc/apt/sources.list.d/moosefs.list ; apt-get update ; apt-get install -y facter moosefs-chunkserver iftop ;

RUN sed -i '/MFSCGISERV_ENABLE=false/c\MFSCGISERV_ENABLE=true' /etc/default/moosefs-cgiserv ;

EXPOSE 9425

CMD ["/usr/sbin/mfscgiserv", "-f", "start"]
