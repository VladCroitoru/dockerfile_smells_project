FROM gperry100/mule
MAINTAINER gil <gil_perry@hotmail.com>

COPY bunnyorderservice-1.0.0-SNAPSHOT.zip /opt/mule/apps/
COPY bunnyorderservice.properties.erb /build/bunnyorderservice.properties.erb
COPY start.sh start.sh
RUN chmod +x start.sh
CMD ["/tmp/start.sh"]

