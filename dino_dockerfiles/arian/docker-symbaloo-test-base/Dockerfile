FROM maven:3.6

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >> /etc/apt/sources.list
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -

# update the repository sources list
# and install dependencies
RUN apt-get update \
    && apt-get install -y curl nodejs rsync \
        mysql-client tomcat7 \
    && apt-get -y autoclean

RUN npm i -g xunit-viewer

RUN curl -o /usr/bin/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
    && chmod +x /usr/bin/wait-for-it.sh

ENV PATH=$PATH:/usr/share/tomcat7/bin
ENV CATALINA_BASE=/var/lib/tomcat7
ENV CATALINA_HOME=/usr/share/tomcat7

# https://bugs.launchpad.net/ubuntu/+source/tomcat7/+bug/1232258
RUN ln -s /var/lib/tomcat7/common/ /usr/share/tomcat7/common \
    && ln -s /var/lib/tomcat7/server/ /usr/share/tomcat7/server \
    && ln -s /var/lib/tomcat7/shared/ /usr/share/tomcat7/shared \
    && ln -s /var/lib/tomcat7/conf/ /usr/share/tomcat7/conf \
    && ln -s /var/lib/tomcat7/logs/ /usr/share/tomcat7/logs \
    && mkdir /var/lib/tomcat7/temp
