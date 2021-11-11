# chamerling/glassfish4sirocco
#
# VERSION               1.0

FROM ubuntu:latest
MAINTAINER Christophe Hamerling "christophe.hamerling@gmail.com"

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update


# Set the mysql configuration to avoid prompts
RUN echo "mysql-server-5.5 mysql-server/root_password password root123" | debconf-set-selections
RUN echo "mysql-server-5.5 mysql-server/root_password_again password root123" | debconf-set-selections
RUN echo "mysql-server-5.5 mysql-server/root_password seen true" | debconf-set-selections
RUN echo "mysql-server-5.5 mysql-server/root_password_again seen true" | debconf-set-selections

RUN apt-get install -y software-properties-common python-software-properties
RUN add-apt-repository ppa:webupd8team/java -y
RUN apt-get update
RUN echo "oracle-java7-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections

RUN apt-get install -y zip wget curl build-essential mysql-server-5.5 git-core oracle-java7-installer

ADD resources/cfgmysql.sh /tmp/
RUN chmod +x /tmp/cfgmysql.sh
RUN /tmp/cfgmysql.sh
RUN rm /tmp/cfgmysql.sh

ADD resources/glassfish.sh /tmp/
RUN chmod +x /tmp/glassfish.sh
RUN /tmp/glassfish.sh
RUN rm /tmp/glassfish.sh

RUN git clone https://github.com/ow2-sirocco/sirocco.git
RUN cp /sirocco/etc/glassfish_config/* /opt/glassfish4/glassfish/domains/domain1/config

ADD resources/sirocco_sql.sh /tmp/sirocco_sql.sh
RUN chmod +x /tmp/sirocco_sql.sh
RUN /tmp/sirocco_sql.sh

# Scripts...

# MySQL client with root password injected on the container if needed...
ADD resources/mysqlclient.sh /

ENV GF_HOME /opt/glassfish4
ENV PATH $PATH:$GF_HOME/bin
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle/jre/

# Expose public and admin ports
EXPOSE 3306 4848 8080 8181 8686 7676 3700 3820 3920

ADD resources/start.sh /
RUN chmod +x /start.sh
CMD ["/start.sh"]
