# Builds an OpenSuse 12 based docker with a fully working Synthese server using MySQL

FROM flavio/opensuse-12-3
MAINTAINER Bastien Noverraz (TL)

# Update
RUN zypper --non-interactive --no-gpg-checks update -y --auto-agree-with-licenses

# Install necessary librairies
RUN \
zypper --non-interactive --no-gpg-checks install -y --auto-agree-with-licenses wget gdb bzip2 pv unzip sed mysql libopenssl0_9_8 subversion glibc-locale && \
zypper --non-interactive --no-gpg-checks install -y --auto-agree-with-licenses python-setools python-pip python-xml

# Install supervisord
RUN \
pip install supervisor && \
mkdir -p /etc/supervisord.d /var/log/supervisor && \
cd /etc && \
wget --no-check-certificate https://extranet.rcsmobility.com/attachments/21282/supervisord.conf && \
mkdir -p supervisor/conf.d && \
cd supervisor/conf.d && \
wget --no-check-certificate https://extranet.rcsmobility.com/attachments/21575/synthese_supervisor.conf && \
wget --no-check-certificate https://extranet.rcsmobility.com/attachments/21576/synthese_proxy_supervisor.conf && \
cd /etc/init.d && \
wget --no-check-certificate https://extranet.rcsmobility.com/attachments/21285/supervisord && \
chmod +x supervisord && \
chkconfig -a supervisord

# SYNTHESE core installation
RUN \
wget http://ci.rcsmobility.com/~build/synthese/lin/release/trunk/latest/synthese.tar.bz2 -O /tmp/synthese.tar.bz2 && \
tar jxf /tmp/synthese.tar.bz2 -C /opt/

# Manual installation of old versions of libs (not available in the repositories)
RUN \
mkdir -p /opt/lib && \
cd /opt/lib && \
wget --no-check-certificate https://extranet.rcsmobility.com/attachments/21281/synthese_libs_opensuse.zip && \
unzip synthese_libs_opensuse.zip && \
rm synthese_libs_opensuse.zip && \
cp -r * /opt/synthese/lib/

# Set rights
RUN \
useradd synthese && \
touch /var/log/synthese.log && \
chown synthese:users /var/log/synthese.log

# MySQL setup & UDF plugin
RUN \
/etc/init.d/mysql start && \
mysql -u root -e "CREATE DATABASE synthese;" && \
mysql -u root -e "CREATE DATABASE bdsi;" && \
mysql -u root -e "grant all privileges on *.* to synthese@localhost identified by 'synthese';" && \
mysql -u root -e "grant all privileges on *.* to root@'%';" && \
mysql -u root -e "UPDATE mysql.user SET Password=PASSWORD('synthese_root') WHERE User='root'; FLUSH PRIVILEGES;" && \
cp /opt/synthese/lib/mysql_udf_plugin/libsynthese_mysql_udf.so /usr/lib64/mysql/plugin/synthese_mysql_udf.so && \
mysql -u root -psynthese_root mysql < /opt/synthese/share/synthese/mysql_udf_plugin/trigger_udf.sql && \
ln -s /var/run/mysql/mysql.sock /var/lib/mysql/mysql.sock && \
/etc/init.d/mysql stop

# Add synthese bin to the path
ENV PATH $PATH:/opt/synthese/bin

# Add our starter
ADD env.sh /opt/bin/env.sh

# Use our starter by default
ENTRYPOINT ["/opt/bin/env.sh"]


