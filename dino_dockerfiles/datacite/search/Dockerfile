FROM phusion/baseimage:0.9.22
MAINTAINER Martin Fenner "mfenner@datacite.org"

# Set correct environment variables
ENV HOME /home/app
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
ENV CATALINA_HOME /usr/share/tomcat7
ENV CATALINA_BASE /var/lib/tomcat7
ENV CATALINA_PID /var/run/tomcat7.pid
ENV CATALINA_SH /usr/share/tomcat7/bin/catalina.sh
ENV CATALINA_TMPDIR /tmp/tomcat7-tomcat7-tmp
ENV DOCKERIZE_VERSION v0.6.0
ENV SOLR_HOME /data/solr
ENV SOLR_DATA /data/solr/collection1/data
ENV SHELL /bin/bash
ENV TERM xterm-256color
ENV SOLR_USER tomcat7
ENV JMX_PORT 17264

# Use baseimage-docker's init process
CMD ["/sbin/my_init"]

# Install Java, Tomcat, Maven and Nginx
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    apt-get update && apt-get install -y wget apt-utils && \
    apt-get install -yqq software-properties-common && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    apt-get install -yqq oracle-java8-installer && \
    apt-get install -yqq oracle-java8-set-default && \
    apt-get install -y mysql-client && \
    apt-get -yqq install tomcat7 maven && \
    apt-get install -y nginx nano && \
    # apt-get clean && \
    # rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    rm -rf /var/cache/oracle-jdk8-installer

# Configure Tomcat
RUN ln -s /var/lib/tomcat7/common $CATALINA_HOME/common && \
    ln -s /var/lib/tomcat7/server $CATALINA_HOME/server && \
    ln -s /var/lib/tomcat7/shared $CATALINA_HOME/shared && \
    ln -s /etc/tomcat7 $CATALINA_HOME/conf && \
    mkdir $CATALINA_HOME/temp && \
    mkdir -p $CATALINA_TMPDIR && \
    rm -rf /var/lib/tomcat7/webapps/docs* && \
    rm -rf /var/lib/tomcat7/webapps/examples* && \
    rm -rf /var/lib/tomcat7/webapps/ROOT*
COPY docker/server.xml /etc/tomcat7/server.xml

# Install dockerize
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \
    tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# Remove unused SSH service
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

# configure nginx
# forward request and error logs to docker log collector
RUN rm /etc/nginx/sites-enabled/default && \
    ln -sf /dev/stdout /var/log/nginx/access.log && \
	  ln -sf /dev/stderr /var/log/nginx/error.log
COPY docker/cors /etc/nginx/conf.d/cors

# Use Amazon NTP servers
COPY docker/ntp.conf /etc/ntp.conf

# Copy webapp folder
COPY . /home/app/
WORKDIR /home/app

# Add solr-client script
COPY scripts/solr-client /usr/local/bin/solr-client

# # Add Runit script for tomcat
RUN mkdir /data && \
    mkdir /data/solr && \
    mkdir /data/solr/collection1 && \
    chown -R $SOLR_USER:$SOLR_USER /data/solr && \
    mkdir /etc/service/tomcat

COPY docker/setenv.sh /usr/share/tomcat7/bin/setenv.sh
COPY docker/tomcat.sh /etc/service/tomcat/run

# Copy server configuration (for context path)
COPY docker/server.xml /etc/tomcat7/server.xml

# Run additional scripts during container startup (i.e. not at build time)
# Process templates using ENV variables
# Compile project
RUN mkdir -p /etc/my_init.d

COPY docker/70_templates.sh /etc/my_init.d/70_templates.sh
COPY docker/80_install.sh /etc/my_init.d/80_install.sh
COPY docker/90_nginx.sh /etc/my_init.d/90_nginx.sh

RUN echo "alias ls='ls -AlhF --color=auto'" >> ~/.bashrc

EXPOSE 80
