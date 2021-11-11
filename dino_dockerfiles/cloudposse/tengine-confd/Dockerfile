FROM cloudposse/library:tengine

ENV ETCD_HOST 172.17.42.1
ENV ETCD_PORT 4001
ENV CONFD_INTERVAL 60
ENV CONFD_VERSION 0.9.0
ENV CONFD_PREFIX /nginx
ENV NGINX_NAME nginx
ENV NGINX_PATH /nginx
ENV DOCKER_DNS 8.8.8.8
ENV GA_TRACKING_ID -

ADD https://github.com/kelseyhightower/confd/releases/download/v$CONFD_VERSION/confd-$CONFD_VERSION-linux-amd64 /usr/bin/confd
ADD confd/ /etc/confd
ADD reload.sh /opt/reload.sh

RUN chmod 755 /usr/bin/confd

VOLUME /etc/nginx

# This environment variable needs to be passed in for etcd
#CMD /usr/bin/confd -prefix=$CONFD_PREFIX -interval=$CONFD_INTERVAL -node=http://$ETCD_HOST:$ETCD_PORT -watch
CMD /usr/bin/confd -prefix=$CONFD_PREFIX -interval=$CONFD_INTERVAL -node=http://$ETCD_HOST:$ETCD_PORT
