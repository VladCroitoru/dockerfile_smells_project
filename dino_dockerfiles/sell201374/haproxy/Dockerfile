FROM ubuntu:15.04
RUN apt-get update -y
RUN apt-get install haproxy -y
#RUN apt-get install rsyslog
COPY haproxy.cfg /etc/haproxy/haproxy.cfg
COPY haproxy /etc/default/haproxy 
#working directory.
WORKDIR /etc/haproxy
# Define default command.
EXPOSE 443
CMD ["/usr/sbin/haproxy","-db", "-f", "/etc/haproxy/haproxy.cfg"]
