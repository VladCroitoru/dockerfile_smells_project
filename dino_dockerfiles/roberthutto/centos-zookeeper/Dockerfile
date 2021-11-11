FROM roberthutto/centos-jdk

RUN curl -fL http://apache.mirror.digitalpacific.com.au/zookeeper/stable/zookeeper-3.4.6.tar.gz | tar xzf - -C /opt && \
mv /opt/zookeeper-3.4.6 /opt/zookeeper

COPY docker-entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

VOLUME /data/zookeeper

WORKDIR /opt/zookeeper/bin

# client port=2181, connect to leader=2888, leader election=3888
EXPOSE 2181 2888 3888

ENTRYPOINT ["/entrypoint.sh"]
CMD ["./zkServer.sh", "start-foreground"]