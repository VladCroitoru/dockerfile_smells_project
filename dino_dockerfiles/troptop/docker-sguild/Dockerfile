FROM ubuntu

RUN apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-client git vim tcpflow wireshark p0f wget tzdata python-jinja2

# Compile tcl without multithread
# apt-get install -y devscripts dpkg-dev zlib1g-dev debhelper
# apt-get source tcl8.6 ; apt-get build-dep tcl 
# vim debian/rules ; replace --enable-threads by --disable-threads
# vim debian//libtcl8.6.symbols ; remove Tcl_GetMemoryInfo and notifierInitMutex@Base 8.6.5 and  notifierMutex@Base 8.6.5
# debuild -us -uc
# cd .. ; dpkg -i tcl*
WORKDIR /opt/
COPY ./libtcl8.6_8.6.5+dfsg-2_amd64.deb /opt/
COPY ./tcl8.6_8.6.5+dfsg-2_amd64.deb /opt/
RUN /usr/bin/dpkg --install /opt/libtcl8.6_8.6.5+dfsg-2_amd64.deb /opt/tcl8.6_8.6.5+dfsg-2_amd64.deb

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y  tcl-tls tcllib tclx mysqltcl

RUN git clone https://github.com/bammv/sguil.git && cd /opt/sguil/server
# Database Configuration
# Create database sguildb;
# GRANT ALL PRIVILEGES ON sguildb.* TO 'sguil'@'%' IDENTIFIED BY 'sgu1lp@sswd';
# FLUSH PRIVILEGES;
# mysql -u $DBUSER -p -h $DBHOST sguildb < sql_scripts/create_sguildb.sql

#  openssl req -newkey rsa:2048 -nodes -keyout /etc/sguild/certs/sguild.key -x509 -days 365 -out /etc/sguild/certs/sguild.pem -subj "/C=UK/ST=Warwickshire/L=Leamington/O=OrgName/OU=IT Department/CN=example.com"
RUN mkdir -p /etc/sguild/certs && cp /opt/sguil/server/sguild.* /etc/sguild/
ENV MYSQL_ADMIM  ""
ENV MYSQL_ADMINPASS ""
ENV MYSQL_HOST ""
ENV MYSQL_DBNAME ""
ENV MYSQL_PASSWORD ""
ENV MYSQL_USER ""
ENV CERT_INFO "/C=UK/ST=Warwickshire/L=Leamington/O=OrgName/OU=IT Department/CN=example.com"
ENV MYSQL_HOST "localhost"
ENV MYSQL_PORT "3306"
ENV MYSQL_DBNAME "sguildb"
ENV MYSQL_USER "sguil"
ENV MYSQL_PASSWORD "sguil"
ENV INSTALL false 
WORKDIR /opt/
EXPOSE 7734
COPY jinja-sguild-conf.py .
COPY sguild-template.conf .
COPY entrypoint.sh /opt/
WORKDIR /opt/sguil/server/
RUN chmod +x /opt/entrypoint.sh
ENTRYPOINT ["/opt/entrypoint.sh"]
#ENV SMTP_SERVER "localhost"
#ENV  EMAIL_RCPT_TO "root@localhost,admin@localhost,sguild@example.com"
#ENV  EMAIL_FROM "root@localhost"

