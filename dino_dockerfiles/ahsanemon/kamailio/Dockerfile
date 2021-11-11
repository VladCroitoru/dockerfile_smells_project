FROM ubuntu:16.04 
 
ENV DBHOST=${DBHOST} 
ENV SIP_DOMAIN=${SIP_DOMAIN}
ENV DBROOTUSER=${DBROOTUSER}
ENV DBROOTPASS=${DBROOTPASS}

# Install the required packages 
RUN apt-get update && apt-get -y install \ 
git \ 
gcc \ 
flex \ 
bison \ 
libmysqlclient-dev \ 
make \ 
libssl-dev \ 
libcurl4-openssl-dev \ 
libxml2-dev \ 
libpcre3-dev \ 
mysql-client \ 
nano \ 
&& rm -rf /var/lib/apt/lists/* 
 
# Getting source code from GIT 
RUN mkdir -p /usr/local/src/kamailio-4.4 
RUN git -C /usr/local/src/kamailio-4.4 clone --depth 1 --no-single-branch https://github.com/kamailio/kamailio kamailio 
RUN git -C /usr/local/src/kamailio-4.4/kamailio checkout -b 4.4 origin/4.4 
 
# Compile the source code and install Kamailio 
RUN make -C /usr/local/src/kamailio-4.4/kamailio cfg 
RUN make -C /usr/local/src/kamailio-4.4/kamailio include_modules="db_mysql dialplan" cfg 
RUN make -C /usr/local/src/kamailio-4.4/kamailio all 
RUN make -C /usr/local/src/kamailio-4.4/kamailio install 
 
RUN PATH=$PATH:/usr/local/sbin && export PATH 
 
# To use MYSQL as DB 
RUN sed -i 's/# DBENGINE=MYSQL/DBENGINE=MYSQL/g' /usr/local/etc/kamailio/kamctlrc 
 
# DB access 
#RUN sed -i 's/# DBROOTUSER="root"/DBROOTUSER="root"\nPW="root"/g' /usr/local/etc/kamailio/kamctlrc 
RUN sed -i 's/# DBRWUSER="kamailio"/DBRWUSER="kamailio"/g' /usr/local/etc/kamailio/kamctlrc 
RUN sed -i 's/# DBRWPW="kamailiorw"/DBRWPW="kamailiorw"/g' /usr/local/etc/kamailio/kamctlrc 
RUN sed -i 's/# DBROUSER="kamailioro"/DBROUSER="kamailioro"/g' /usr/local/etc/kamailio/kamctlrc 
RUN sed -i 's/# DBROPW="kamailioro"/DBROPW="kamailioro"/g' /usr/local/etc/kamailio/kamctlrc 
 
RUN sed -i 's/# INSTALL_EXTRA_TABLES=ask/INSTALL_EXTRA_TABLES=yes/g' /usr/local/etc/kamailio/kamctlrc 
RUN sed -i 's/# INSTALL_DBUID_TABLES=ask/INSTALL_DBUID_TABLES=yes/g' /usr/local/etc/kamailio/kamctlrc 
RUN sed -i 's/# INSTALL_PRESENCE_TABLES=ask/INSTALL_PRESENCE_TABLES=yes/g' /usr/local/etc/kamailio/kamctlrc 
 
# DB IP 
###RUN sed -i 's/# DBHOST=localhost/DBHOST=192.168.225.12/g' /usr/local/etc/kamailio/kamctlrc 
 
# To access DB from any host 
RUN sed -i 's/# DBACCESSHOST=192.168.0.1/DBACCESSHOST=%/g' /usr/local/etc/kamailio/kamctlrc 

# Create kamailio schema in the DB 
# /usr/local/sbin/kamdbctl create 
 
# To enable usage of MySQL 
RUN sed -i -e '1i#!define WITH_MYSQL\' /usr/local/etc/kamailio/kamailio.cfg 
RUN sed -i -e '2i#!define WITH_AUTH\' /usr/local/etc/kamailio/kamailio.cfg 
RUN sed -i -e '3i#!define WITH_USRLOCDB\' /usr/local/etc/kamailio/kamailio.cfg 
 
# To use init.d script for starting/stoping the Kamailio server 
RUN cp /usr/local/src/kamailio-4.4/kamailio/pkg/kamailio/deb/debian/kamailio.init /etc/init.d/kamailio 
RUN chmod 755 /etc/init.d/kamailio 
RUN sed -i 's/DAEMON=\/usr\/sbin\/kamailio/DAEMON=\/usr\/local\/sbin\/kamailio/g' /etc/init.d/kamailio 
RUN sed -i 's/CFGFILE=\/etc\/$NAME\/kamailio.cfg/CFGFILE=\/usr\/local\/etc\/kamailio\/kamailio.cfg/g' /etc/init.d/kamailio 
 
RUN cp /usr/local/src/kamailio-4.4/kamailio/pkg/kamailio/deb/debian/kamailio.default /etc/default/kamailio 
RUN sed -i 's/#RUN_KAMAILIO=yes/RUN_KAMAILIO=yes/g' /etc/default/kamailio 
RUN sed -i 's/#CFGFILE=\/etc\/kamailio\/kamailio.cfg/CFGFILE=\/usr\/local\/etc\/kamailio\/kamailio.cfg/g' /etc/default/kamailio 
RUN sed -i 's/#USER=kamailio/USER=kamailio/g' /etc/default/kamailio 
RUN sed -i 's/#GROUP=kamailio/GROUP=kamailio/g' /etc/default/kamailio 
 
# Default setting is to run Kamailio as user “kamailio” and group “kamailio” 
RUN mkdir -p /var/run/kamailio 
RUN adduser --quiet --system --group --disabled-password --shell /bin/false --gecos "Kamailio" --home /var/run/kamailio kamailio 
RUN chown kamailio:kamailio /var/run/kamailio 
 
COPY kamailio-config.sh / 
RUN chmod +x /kamailio-config.sh 
ENTRYPOINT ["/kamailio-config.sh"] 

EXPOSE 5060 

# Start the service 
CMD ["/etc/init.d/kamailio","start"] 
