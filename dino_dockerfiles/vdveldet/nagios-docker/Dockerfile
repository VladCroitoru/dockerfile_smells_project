FROM ubuntu:14.04
ENV DEBIAN_FRONTEND noninteractive

ENV NAGIOS_HOME=/usr/local/nagios NAGIOS_USER=nagios NAGIOS_GROUP=nagios NAGIOS_CMDUSER=nagios NAGIOS_CMDGROUP=nagios
ENV NAGIOSGRAPH_HOME=/usr/local/nagiosgraph NAGIOSADMIN_USER=nagiosadmin NAGIOSADMIN_PASS=nagios
ENV APACHE_RUN_USER=www-data APACHE_RUN_GROUP=www-dataA

ENV NAGIOS_TIMEZONE UTC
ENV NAGIOS_VER nagios-4.1.1
ENV NAGIOS_PLUG_VER nagios-plugins-2.1.1
ENV DOWNURLNAGIOS https://sourceforge.net/projects/nagios/files/nagios-4.x/nagios-4.1.1/${NAGIOS_VER}.tar.gz/download
ENV DOWNURLPLUG http://nagios-plugins.org/download/${NAGIOS_PLUG_VER}.tar.gz
ENV DOWNNRPE https://sourceforge.net/projects/nagios/files/nrpe-2.x/nrpe-2.15/nrpe-2.15.tar.gz/download
ENV DOWNNRDP https://assets.nagios.com/downloads/nrdp/nrdp.zip
ENV DOWNGRAPH http://downloads.sourceforge.net/project/nagiosgraph/nagiosgraph/1.5.2/nagiosgraph-1.5.2.tar.gz


# Setup environment
RUN sed -i 's/universe/universe multiverse/' /etc/apt/sources.list
RUN apt-get update && apt-get install -y iputils-ping netcat snmp snmpd snmp-mibs-downloader php5-cli apache2 apache2-utils libapache2-mod-php5 runit bc postfix bsd-mailx openssl 
RUN apt-get install -y libgd-tools php5-gd php5-rrd librrds-perl libgd-perl libnagios-object-perl
RUN apt-get install -y build-essential unzip libssl-dev


# Create Users
RUN ( egrep -i  "^${NAGIOS_GROUP}" /etc/group || groupadd $NAGIOS_GROUP ) && ( egrep -i "^${NAGIOS_CMDGROUP}" /etc/group || groupadd $NAGIOS_CMDGROUP )
RUN ( id -u $NAGIOS_USER || useradd --system $NAGIOS_USER -g $NAGIOS_GROUP -d $NAGIOS_HOME ) && ( id -u $NAGIOS_CMDUSER || useradd --system -d $NAGIOS_HOME -g $NAGIOS_CMDGROUP $NAGIOS_CMDUSER ) && ( usermod -a -G $NAGIOS_GROUP $APACHE_RUN_USER )


# Setup Nagios
ADD $DOWNURLNAGIOS /tmp/nagios.tar.gz
RUN cd /tmp && tar -zxvf nagios.tar.gz && cd ${NAGIOS_VER}  && ./configure --prefix=${NAGIOS_HOME} --exec-prefix=${NAGIOS_HOME} --enable-event-broker --with-nagios-command-user=${NAGIOS_CMDUSER} --with-command-group=${NAGIOS_CMDGROUP} --with-nagios-user=${NAGIOS_USER} --with-nagios-group=${NAGIOS_GROUP} && make all && make install && make install-config && make install-commandmode && cp daemon-init /etc/init.d/nagios && chmod +x /etc/init.d/nagios
RUN cd /tmp/${NAGIOS_VER} && cp sample-config/httpd.conf /etc/apache2/conf-available/nagios.conf && cd /etc/apache2/conf-enabled && ln -s /etc/apache2/conf-available/nagios.conf


# Setup nagios Plugins
ADD $DOWNURLPLUG /tmp/nagios-plugins-2.1.1.tar.gz
RUN cd /tmp && tar -zxvf nagios-plugins-2.1.1.tar.gz && cd nagios-plugins-2.1.1 && ./configure --prefix=${NAGIOS_HOME} && make && make install


# Setup apache
RUN sed -i.bak 's/.*\=www\-data//g' /etc/apache2/envvars && echo "export APACHE_RUN_USER=www-data" >> /etc/apache2/envvars && \
    echo "export APACHE_RUN_GROUP=www-data" >> /etc/apache2/envvars && sed -i 's/^ULIMIT_MAX_FILES/#ULIMIT_MAX_FILES/g' /usr/sbin/apache2ctl && \
    cd /etc/apache2/mods-enabled && ln -s ../mods-available/cgi.load
RUN export DOC_ROOT="DocumentRoot $(echo $NAGIOS_HOME/share)"; sed -i "s,DocumentRoot.*,$DOC_ROOT," /etc/apache2/sites-available/000-default.conf

RUN echo "use_timezone=$NAGIOS_TIMEZONE" >> ${NAGIOS_HOME}/etc/nagios.cfg && echo "SetEnv TZ \"${NAGIOS_TIMEZONE}\"" >> /etc/apache2/conf-available/nagios.conf

RUN sed -i 's,/bin/mail,/usr/bin/mail,' ${NAGIOS_HOME}/etc/objects/commands.cfg && \
    sed -i 's,/usr/usr,/usr,' ${NAGIOS_HOME}/etc/objects/commands.cfg && \ 
    cp /etc/services /var/spool/postfix/etc/


# Setup NRPE
ADD $DOWNNRPE /tmp/nrpe.tar.gz
RUN cd /tmp && tar -zxvf nrpe.tar.gz && cd nrpe-2.15 && ./configure --with-ssl=/usr/bin/openssl --with-ssl-lib=/usr/lib/x86_64-linux-gnu --prefix=${NAGIOS_HOME} && make && make install


ENV NRDP_TOKEN "token1","token2"
# Setup NRDPE
#ADD $DOWNNRDPE /tmp/nrdp.zip
ADD nrdp.zip /tmp/
RUN cd /tmp && unzip nrdp.zip && mkdir /usr/local/nrdp/ && cd /usr/local/nrdp/ && cp -r /tmp/nrdp/* . && chown -R www-data.www-data /usr/local/nrdp && \
    cp /tmp/nrdp/nrdp.conf /etc/apache2/sites-available/ && cd /etc/apache2/conf-enabled && ln -s /etc/apache2/sites-available/nrdp.conf && \
    sed -i '/ Order allow,deny/d' /etc/apache2/conf-enabled/nrdp.conf && \
    sed -i 's/ Allow from all/Require all granted/g' /etc/apache2/conf-enabled/nrdp.conf && \
    sed -i 's/\/\/\"mysecrettoken\b.*$/${NRDP_TOKEN}/' /usr/local/nrdp/server/config.inc.php 


# Setup Nagiosgraph
ADD $DOWNGRAPH	/tmp/nagiosgraph.tar.gz
#ADD nagiosgraph-1.5.2.tar.gz /tmp/
RUN cd /tmp && tar -zxvf nagiosgraph.tar.gz && cd /tmp/nagiosgraph-1.5.2 && \
    export NG_PREFIX=${NAGIOSGRAPH_HOME} && export NG_NAGIOS_PERFDATA_FILE=${NAGIOS_HOME}/var/service-perfdata.out && ./install.pl --install && \
    cd /etc/apache2/conf-enabled && ln -s /usr/local/nagiosgraph/etc/nagiosgraph-apache.conf && \
    sed -i '/ Order allow,deny/d' /etc/apache2/conf-enabled/nagiosgraph-apache.conf && \
    sed -i 's/ Allow from all/Require all granted/g' /etc/apache2/conf-enabled/nagiosgraph-apache.conf && \
    sed -i 's/\/tmp\/perfdata.log/\/usr\/local\/nagios\/var\/service-perfdata.out/g' ${NAGIOSGRAPH_HOME}/etc/nagiosgraph.conf


# Cleanup
#RUN apt-get clean && \
#    rm -rf /tmp/* /var/tmp/* && \
#    rm -rf /var/lib/apt/lists/*

ADD start_nagios.sh /usr/local/bin/start_nagios
RUN chmod +x /usr/local/bin/start_nagios


EXPOSE 80

VOLUME ${NAGIOS_HOME}/etc
VOLUME /var/log/apache2
VOLUME ${NAGIOSGRAPH_HOME}/var/rrd/

CMD ["/usr/local/bin/start_nagios"]
