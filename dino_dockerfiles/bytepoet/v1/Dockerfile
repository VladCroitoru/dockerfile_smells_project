FROM ubuntu:latest
 
MAINTAINER Ryan Poniatowski <ryan@mpaktlabs.com>

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
apt-get -y upgrade && apt-get -y install unzip nginx curl openvpn vnstati vnstat fail2ban openssh-client nano iptables-persistent cronutils && crontab /tmp/config/jobs
 
#ports!
EXPOSE 80
EXPOSE 443

# Copy site into place.
ADD www /usr/share/nginx/html
ADD scripts /tmp/scripts 
ADD config /tmp/config



# run
ENTRYPOINT /tmp/scripts/start.sh

CMD /usr/sbin/nginx
