FROM library/centos:7
MAINTAINER Markos Chandras <hwoarang@gentoo.org>
RUN yum update -y && yum install -y vsftpd && yum install -y openssl
ADD vsftpd.conf.template /etc/vsftpd/vsftpd.conf
ADD wrap_vsftpd.sh /bin/

# This is for our listen port and the passive port range.
# If the defaults are not good enough for you, set these variables
# when creating your container using --env or --env-file
ENV PASV_MIN="2000" PASV_MAX="2100" LISTEN="21"

# Execute the wrapper which will create the certificate and
# users for us. Please read the script to understand how it works
CMD ["wrap_vsftpd.sh"]

EXPOSE ${PASV_MIN}-${PASV_MAX} ${LISTEN}
