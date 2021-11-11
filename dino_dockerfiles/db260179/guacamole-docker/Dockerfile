### Dockerfile for guacamole
### Includes the mysql authentication module preinstalled

# Use phusion/baseimage as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.
FROM phusion/baseimage:0.9.22
LABEL maintainer "taddeusz@gmail.com"

# Set correct environment variables.
ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Configure user nobody to match unRAID's settings
RUN usermod -u 99 nobody && \
    usermod -g 100 nobody && \
    usermod -d /home nobody && \
    chown -R nobody:users /home

# Disable SSH
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8 && \
    add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://nyc2.mirrors.digitalocean.com/mariadb/repo/10.2/ubuntu xenial main'

### Don't let apt install docs or man pages
COPY excludes /etc/dpkg/dpkg.cfg.d/excludes
### Install packages and clean up in one command to reduce build size
RUN apt-get update && \
    apt-get install -y --no-install-recommends libcairo2-dev libpng12-dev freerdp-x11 libssh2-1 \
    libfreerdp-dev libvorbis-dev libssl-dev gcc libssh-dev libpulse-dev tomcat8 tomcat8-admin \
    libpango1.0-dev libssh2-1-dev autoconf wget libossp-uuid-dev libtelnet-dev libvncserver-dev \
    build-essential software-properties-common pwgen mariadb-server \
    libavcodec-dev libavutil-dev libswscale-dev libwebp-dev libfreerdp-plugins-standard && \


    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
                            /usr/share/man /usr/share/groff /usr/share/info \
                            /usr/share/lintian /usr/share/linda /var/cache/man && \
    (( find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true )) && \
    (( find /usr/share/doc -empty|xargs rmdir || true ))

### Install the authentication extensions in the classpath folder
### and the client app in the tomcat webapp folder
### Version of guacamole to be installed
ENV GUAC_VER 0.9.13-incubating
### Version of mysql-connector-java to install
ENV MCJ_VER 5.1.43
### config directory and classpath directory
RUN mkdir -p /config/guacamole /var/lib/guacamole/ldap-schema /var/lib/guacamole/lib /var/lib/guacamole/extensions /etc/firstrun

# Tweak my.cnf

RUN sed -i -e 's#\(bind-address.*=\).*#\1 127.0.0.1#g' /etc/mysql/my.cnf && \
    sed -i -e 's#\(log_error.*=\).*#\1 /config/databases/mysql_safe.log#g' /etc/mysql/my.cnf && \
    sed -i -e 's/\(user.*=\).*/\1 nobody/g' /etc/mysql/my.cnf && \
    echo '[mysqld]' > /etc/mysql/conf.d/innodb_file_per_table.cnf && \
    echo 'innodb_file_per_table' >> /etc/mysql/conf.d/innodb_file_per_table.cnf

### Install LDAP Authentication Module
RUN cd /tmp && \
    wget -q --span-hosts http://downloads.sourceforge.net/project/guacamole/current/extensions/guacamole-auth-ldap-${GUAC_VER}.tar.gz && \
    tar -zxf guacamole-auth-ldap-${GUAC_VER}.tar.gz && \
    mv -f guacamole-auth-ldap-${GUAC_VER}/guacamole-auth-ldap-${GUAC_VER}.jar /var/lib/guacamole/extensions && \
    mv -f guacamole-auth-ldap-${GUAC_VER}/schema/* /var/lib/guacamole/ldap-schema &&\
    rm -Rf /tmp/*

### Install Duo Authentication Module
RUN cd /tmp && \
    wget -q --span-hosts http://downloads.sourceforge.net/project/guacamole/current/extensions/guacamole-auth-duo-${GUAC_VER}.tar.gz && \
    tar -zxf guacamole-auth-duo-${GUAC_VER}.tar.gz && \
    mv -f guacamole-auth-duo-${GUAC_VER}/guacamole-auth-duo-${GUAC_VER}.jar /var/lib/guacamole/extensions && \
    rm -Rf /tmp/*

    ### Install CAS Authentication Module
RUN cd /tmp && \
    wget -q --span-hosts http://downloads.sourceforge.net/project/guacamole/current/extensions/guacamole-auth-cas-${GUAC_VER}.tar.gz && \
    tar -zxf guacamole-auth-cas-${GUAC_VER}.tar.gz && \
    mv -f guacamole-auth-cas-${GUAC_VER}/guacamole-auth-cas-${GUAC_VER}.jar /var/lib/guacamole/extensions && \
    rm -Rf /tmp/*

### Install MySQL Authentication Module
RUN cd /tmp && \
    wget -q --span-hosts http://downloads.sourceforge.net/project/guacamole/current/extensions/guacamole-auth-jdbc-${GUAC_VER}.tar.gz && \
    tar -zxf guacamole-auth-jdbc-${GUAC_VER}.tar.gz && \
    mv -f guacamole-auth-jdbc-${GUAC_VER}/mysql/guacamole-auth-jdbc-mysql-${GUAC_VER}.jar /var/lib/guacamole/extensions && \
    mv -f guacamole-auth-jdbc-${GUAC_VER}/mysql/schema/* /root &&\
    rm -Rf /tmp/*

### Install dependancies for mysql authentication module
RUN cd /tmp && \
    wget -q --span-hosts http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${MCJ_VER}.tar.gz && \
    tar -zxf mysql-connector-java-$MCJ_VER.tar.gz && \
    mv -f `find . -type f -name '*.jar'` /var/lib/guacamole/lib && \
    rm -Rf /tmp/*

### Install precompiled client webapp
RUN cd /var/lib/tomcat8/webapps && \
    rm -Rf ROOT && \
    wget -q --span-hosts http://sourceforge.net/projects/guacamole/files/current/binary/guacamole-${GUAC_VER}.war && \
    ln -s guacamole-$GUAC_VER.war ROOT.war && \
    ln -s guacamole-$GUAC_VER.war guacamole.war

### Compile and install guacamole server
RUN cd /tmp && \
    wget -q --span-hosts http://sourceforge.net/projects/guacamole/files/current/source/guacamole-server-${GUAC_VER}.tar.gz && \
    tar -zxf guacamole-server-$GUAC_VER.tar.gz && \
    cd guacamole-server-$GUAC_VER && \
    ./configure --with-init-dir=/etc/init.d && \
    make && \
    make install && \
    update-rc.d guacd defaults && \
    ldconfig && \
    rm -Rf /tmp/*

### Compensate for GUAC-513
RUN ln -s /usr/local/lib/freerdp/guacsnd-client.so /usr/lib/x86_64-linux-gnu/freerdp/ && \
    ln -s /usr/local/lib/freerdp/guacdr-client.so /usr/lib/x86_64-linux-gnu/freerdp/

### Configure Service Startup
COPY rc.local /etc/rc.local
COPY mariadb.sh /etc/service/mariadb/run
COPY firstrun.sh /etc/my_init.d/firstrun.sh
COPY configfiles/. /etc/firstrun/
RUN chmod a+x /etc/rc.local && \
    chmod +x /etc/service/mariadb/run && \
    chmod +x /etc/my_init.d/firstrun.sh && \
    chown -R nobody:users /config && \
    chown -R nobody:users /var/log/mysql* && \
    chown -R nobody:users /var/lib/mysql && \
    chown -R nobody:users /etc/mysql && \
    chown -R nobody:users /var/run/mysqld && \
    ln -s /config/guacamole /usr/share/tomcat8/.guacamole

EXPOSE 8080

VOLUME ["/config"]

### END
### To make this a persistent guacamole container, you must map /config of this container
### to a folder on your host machine.
###
