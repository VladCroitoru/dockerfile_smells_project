FROM elasticsearch:5.3.1
#ADD ./docker-entrypoint.sh /docker-entrypoint.sh

#ADD ./config /default-config
USER root
#RUN chown -R elasticsearch:elasticsearch /default-config
#USER elasticsearch

ADD ./ping 	/usr/bin/ping 
ADD ./confd	 /confd
RUN chmod +x /confd

ADD ./elasticsearch-conf/conf.d /etc/confd/conf.d
ADD ./elasticsearch-conf/templates /etc/confd/templates
ADD ./elasticsearch-conf/run.sh /run.sh
ADD ./elasticsearch-conf/dockerentry.sh /rancher-dockerentry.sh

RUN mkdir -p /opt/rancher/bin/
RUN chown -R elasticsearch /opt/rancher/bin/
RUN rm /usr/share/elasticsearch/config/elasticsearch.yml
#VOLUME /data/confd
#VOLUME /opt/rancher/bin
#VOLUME /usr/share/elasticsearch/config

USER elasticsearch
EXPOSE 9200
EXPOSE 9300

ENTRYPOINT ["/rancher-dockerentry.sh"]
CMD ["--backend", "rancher", "--prefix", "/2015-07-25"]


