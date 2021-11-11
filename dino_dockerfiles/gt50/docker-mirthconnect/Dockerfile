FROM centos:7

# ENV MIRTH_CONNECT_VERSION 3.7.0.b2399
ENV MIRTH_CONNECT_VERSION 3.8.0.b2464


RUN yum update -y
RUN yum install -y wget
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
# RUN yum install -y monit htop
RUN yum install -y htop

WORKDIR /opt/mirthconnect

RUN yum install -y java-1.8.0-openjdk

RUN wget http://downloads.mirthcorp.com/connect/$MIRTH_CONNECT_VERSION/mirthconnect-$MIRTH_CONNECT_VERSION-linux.rpm \
    && yum install -y mirthconnect-$MIRTH_CONNECT_VERSION-linux.rpm \
    && sed -i 's/8080/80/g' /opt/mirthconnect/conf/mirth.properties \
    && sed -i 's/8443/443/g' /opt/mirthconnect/conf/mirth.properties \
    && sed -i 's/-Xmx256m/-Xmx1024m/g' /opt/mirthconnect/mcserver.vmoptions \
    && sed -i 's/-Xmx256m/-Xmx1024m/g' /opt/mirthconnect/mcservice.vmoptions \
    # Not producing the final pid
    # && sed -i '/com.mirth.connect.server.launcher.MirthLauncher  >/a\echo $! > /var/run/mcservice.pid' mcservice \
    # && sed -i '/com.install4j.runtime.launcher.UnixLauncher stop/a\rm /var/run/mcservice.pid' mcservice \ 
    && rm -f mirthconnect-$MIRTH_CONNECT_VERSION-linux.rpm

# RUN sed -i "\$acheck process mcservice with pidfile /var/run/mcservice.pid" /etc/monitrc \
#     && sed -i "\$a  start program = \"/opt/mirthconnect/mcservice start\" with timeout 60 seconds" /etc/monitrc \
#     && sed -i "\$a  stop program = \"/opt/mirthconnect/mcservice stop\"" /etc/monitrc \
#     && sed -i "\$a  if cpu > 60% for 2 cycles then alert" /etc/monitrc \
#     && sed -i "\$a  if cpu > 90% for 5 cycles then restart" /etc/monitrc

EXPOSE 80 443

# CMD /opt/mirthconnect/mcservice restart && monit && tail -F /opt/mirthconnect/logs/mirth.log
CMD /opt/mirthconnect/mcservice restart && tail -F /opt/mirthconnect/logs/mirth.log