FROM ubuntu
MAINTAINER benediktarnold

ENV collectd_ver 5.4.2
ENV basedir /opt/collectd

ENV LOGSTASH_SERVER logstash
ENV LOGSTASH_PORT 25826
#ENV HOSTNAME -PLEASE SUPPLY!-

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends curl build-essential libcurl4-openssl-dev liblvm2-dev libxml2 libxslt-dev python python-pip python-dev && \
	cd /opt && \
  	curl http://collectd.org/files/collectd-${collectd_ver}.tar.gz | tar zx && \
  	cd collectd-${collectd_ver} && \
  	./configure --prefix=${basedir} --with-plugin=lvm && \
  	make && \
  	make install && \
  	rm -rf /opt/collectd-${collectd_ver} && \
  	apt-get remove --purge -y curl build-essential && \
  	apt-get clean && \
  	rm -rf /var/lib/apt/lists/*


#Unfortulately this will install an outdated version of collectd...
#RUN apt-get update && \
 #   DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends collectd libcurl4-openssl-dev && \
 #   apt-get clean && \
 #   rm -rf /var/lib/apt/lists/*

 #   python btrfs-tools && \


#RUN rm /etc/collectd.conf
ADD collectd.conf ${basedir}/etc/collectd.conf
ADD collectd.d ${basedir}/etc/collectd.d
#ADD btrfs-data.py ${basedir}/bin/btrfs-data.py
ADD entrypoint.sh /collectd_entrypoint.sh
RUN chmod a+x /collectd_entrypoint.sh

CMD /collectd_entrypoint.sh
