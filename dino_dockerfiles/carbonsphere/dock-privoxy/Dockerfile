############################################################
# Dockerfile: CentOS6 & Privoxy
############################################################
FROM carbonsphere/dock-centos6-epel-base:v1

MAINTAINER CarbonSphere <CarbonSphere@gmail.com>

RUN yum -y install privoxy wget; yum -y clean all

ADD run.sh /usr/local/bin/run.sh
RUN /bin/sed -i "s/listen-address  127.0.0.1/listen-address  0.0.0.0/g" /etc/privoxy/config
ADD privoxy-blist.sh /usr/local/bin/privoxy-blist.sh
ADD privoxy-blist.conf /usr/local/bin/privoxy-blist.conf

EXPOSE 8118

CMD ["run.sh"]