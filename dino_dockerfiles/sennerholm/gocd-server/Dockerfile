FROM dockerfile/java
MAINTAINER Mikael Sennerholm <mikael@sennerholm.net>
# Partly from: https://github.com/gocd/gocd-docker and old projects

ADD scripts/go-common-scripts.sh /usr/local/bin/
ADD scripts/go-server-start.sh /usr/local/bin/

# Download an install Go-server
RUN wget -q -O /tmp/go-server.deb http://download.go.cd/gocd-deb/go-server-14.2.0-377.deb && dpkg -i /tmp/go-server.deb && rm -f /tmp/go-server.deb
RUN sed -i -e 's/DAEMON=Y/DAEMON=N/' /etc/default/go-server

EXPOSE 8153 8154
CMD ["/usr/local/bin/go-server-start.sh"]