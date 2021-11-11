#################################################
# Debian with added vsftpd Server.
# Uses anonymous only for DL.
#################################################

# Using latest debian image as base
FROM debian:latest

MAINTAINER hihouhou < hihouhou@hihouhou.com >


# install dependancies
RUN apt-get update && apt-get install -y vsftpd

#configure vsftpd.conf
RUN echo "listen=YES\n\
local_enable=NO\n\
anonymous_enable=YES\n\
write_enable=NO\n\
anon_root=/var/ftp\n\
" > /etc/vsftpd.conf


RUN mkdir -p /var/run/vsftpd/empty && mkdir /var/ftp

# startup
CMD vsftpd

EXPOSE 21/tcp
