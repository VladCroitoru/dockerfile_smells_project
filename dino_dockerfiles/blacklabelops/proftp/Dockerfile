# Using CentOS as base container
FROM blacklabelops/centos
MAINTAINER Steffen Bleul <blacklabelops@itbleul.de>

# Copy  scripts and configs
COPY  ftpscripts/*.sh /

# Sources for proftpd
ENV PROFTP_FTPASSWD_URL http://www.castaglia.org/proftpd/contrib/ftpasswd
ENV PROFTP_FTPQOUTA_URL http://www.castaglia.org/proftpd/contrib/ftpquota
ENV PROFTP_URL ftp://ftp.proftpd.org/distrib/source/proftpd-1.3.5.tar.gz

#mod_quotatab:mod_quotatab_file:
# Update container, Install ProFTPd and other needed
RUN yum update -y && yum install tar  perl sudo gcc make -y ;\
    \
    \
    cd /usr/local/src;\
    curl ${PROFTP_URL} | tar zx && cd proftpd* ;\
    ./configure --with-modules=mod_quotatab:mod_quotatab_file --sysconfdir=/etc && make && make install ;\
    \
    \
    rm /etc/proftpd.conf;\
    curl ${PROFTP_FTPASSWD_URL} > /usr/bin/ftpasswd ; \
    curl ${PROFTP_FTPQOUTA_URL} > /usr/bin/ftpquota ;\
    chmod +x /usr/bin/ftpasswd ; chmod +x /usr/bin/ftpquota; \
    chmod +x /usr/bin/ftpasswd /usr/bin/ftpquota ;\
    mkdir -p  /var/ftp/ftpuser ; mkdir /var/ftp/user_keys ;\
    umask 0057;\
    echo 'ftpuser:$1$3CWChbUT$nl5TzKmPkBBk2HinHYKR30:99:99::/var/ftp/ftpuser:/sbin/nologin' > /var/ftp/ftpd.passwd;\
    umask 0022;\
    chown -R  nobody:nobody /var/ftp;\
    ln -s /ftpuser.sh /usr/bin/addftpuser;\
    ln -s /ftpuser.sh /usr/bin/removeftpuser;\
    ln -s /ftpuser.sh /usr/bin/disableftpuser;\
    ln -s /ftpuser.sh /usr/bin/enableftpuser;\
    ln -s /ftpuser.sh /usr/bin/chpassftpuser;\
    ln -s /ftpuser.sh /usr/bin/quotaftpset;\
    ln -s /ftpuser.sh /usr/bin/addtechuser;\
    chmod +x /entrypoint.sh;\
	  ftpquota --create-table --type=limit --table-path /var/ftp/ftpquota.limittab;\
	  ftpquota --create-table --type=tally --table-path /var/ftp/ftpquota.tallytab

#Copy config
COPY  configuration/ftp.conf /root/
#Specify volume
VOLUME /var/ftp
EXPOSE 21

# Set entrypoint script
ENTRYPOINT ["/entrypoint.sh"]

# Set default start command
CMD ["proftpd","--nodaemon"]
